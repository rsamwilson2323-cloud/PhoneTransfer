from flask import Flask, request, render_template_string
import os, socket, secrets, qrcode, base64
from io import BytesIO
from werkzeug.utils import secure_filename

app = Flask(__name__)
BASE = os.path.dirname(os.path.abspath(__file__))
FOLDER = os.path.join(BASE, "Received_Files")
os.makedirs(FOLDER, exist_ok=True)
PORT = 8765
TOKEN = secrets.token_urlsafe(16)

def local_ip():
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.connect(("8.8.8.8",80))
        ip=s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"

IP=local_ip()
URL=f"http://{IP}:{PORT}/?token={TOKEN}"

qr=qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=9,border=4)
qr.add_data(URL); qr.make(fit=True)
im=qr.make_image(fill_color="#111827",back_color="white")
buf=BytesIO(); im.save(buf,format="PNG")
QR=base64.b64encode(buf.getvalue()).decode()

PC=r"""<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>LocalDrop</title><style>
*{box-sizing:border-box}body{margin:0;min-height:100vh;font-family:Arial,sans-serif;color:#fff;background:radial-gradient(circle at 15% 10%,#1e3a8a,transparent 35%),radial-gradient(circle at 90% 90%,#4c1d95,transparent 35%),#020617;display:flex;align-items:center;justify-content:center;padding:25px}.wrap{width:min(1050px,100%);display:grid;grid-template-columns:1fr 1fr;gap:22px}.card{background:rgba(15,23,42,.82);border:1px solid rgba(255,255,255,.1);border-radius:28px;padding:32px;box-shadow:0 25px 80px #0008;backdrop-filter:blur(18px)}.logo{font-size:34px;width:66px;height:66px;border-radius:20px;display:grid;place-items:center;background:linear-gradient(135deg,#38bdf8,#8b5cf6)}h1{font-size:42px;margin:18px 0 6px}.muted{color:#94a3b8}.qr{text-align:center}.qr img{width:min(310px,90%);background:#fff;padding:16px;border-radius:20px;margin:18px auto}.url{font-family:monospace;color:#7dd3fc;background:#ffffff0a;padding:13px;border-radius:12px;word-break:break-all}.status{margin-top:22px;padding:14px;border-radius:13px;background:#22c55e14;color:#86efac}.dot{display:inline-block;width:10px;height:10px;background:#22c55e;border-radius:50%;box-shadow:0 0 12px #22c55e;margin-right:8px}.step{display:flex;gap:13px;margin:18px 0;color:#cbd5e1}.n{min-width:32px;height:32px;border-radius:50%;background:#38bdf81c;color:#7dd3fc;display:grid;place-items:center;font-weight:bold}@media(max-width:760px){.wrap{grid-template-columns:1fr}h1{font-size:34px}}</style></head><body><div class="wrap"><div class="card"><div class="logo">📱</div><h1>LocalDrop</h1><p class="muted">Phone → PC local file transfer</p><div class="step"><span class="n">1</span><span>Connect your phone and PC to the same Wi-Fi.</span></div><div class="step"><span class="n">2</span><span>Scan the QR code with your phone camera.</span></div><div class="step"><span class="n">3</span><span>Select one or more files.</span></div><div class="step"><span class="n">4</span><span>Press SEND FILES TO PC.</span></div><div class="status"><span class="dot"></span>Waiting for phone...</div></div><div class="card qr"><h2>Scan to Connect</h2><p class="muted">Open your phone camera and scan</p><img src="data:image/png;base64,{{qr}}"><div class="url">{{url}}</div><p class="muted">🔒 Direct local-network transfer</p></div></div></body></html>"""

PHONE=r"""<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>LocalDrop</title><style>
*{box-sizing:border-box}body{margin:0;min-height:100vh;font-family:Arial,sans-serif;color:#fff;background:radial-gradient(circle at top,#172554,transparent 45%),#020617;padding:22px}.wrap{max-width:520px;margin:auto}.head{text-align:center;margin:20px 0}.icon{width:75px;height:75px;margin:auto;border-radius:22px;display:grid;place-items:center;font-size:38px;background:linear-gradient(135deg,#38bdf8,#8b5cf6)}h1{margin:16px 0 5px}.muted{color:#94a3b8}.card{background:#0f172ae6;border:1px solid #ffffff1a;border-radius:24px;padding:24px;box-shadow:0 20px 60px #0008}.drop{display:block;text-align:center;border:2px dashed #38bdf855;border-radius:18px;padding:35px 15px;cursor:pointer}.drop b{font-size:18px}.big{font-size:45px}input{display:none}.file{background:#ffffff0a;padding:12px;border-radius:10px;margin-top:8px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}button{width:100%;border:0;border-radius:14px;padding:16px;margin-top:20px;font-size:16px;font-weight:bold;background:linear-gradient(135deg,#38bdf8,#818cf8);color:#020617}button:disabled{opacity:.5}.progress{display:none;margin-top:18px}progress{width:100%;height:10px}.foot{text-align:center;color:#64748b;font-size:13px;margin-top:18px}</style></head><body><div class="wrap"><div class="head"><div class="icon">📤</div><h1>LocalDrop</h1><div class="muted">Send files directly to your PC</div></div><div class="card"><form id="f"><label class="drop" for="files"><div class="big">📁</div><b>Select Files</b><p class="muted">Tap here to choose files</p><input id="files" type="file" multiple></label><div id="list"></div><button id="send">SEND FILES TO PC</button><div class="progress" id="box"><progress id="bar" max="100" value="0"></progress><p id="msg">Uploading...</p></div></form></div><div class="foot">🔒 Files stay on your local network. No cloud upload.</div></div><script>
const i=document.getElementById('files'),l=document.getElementById('list'),f=document.getElementById('f'),b=document.getElementById('send'),box=document.getElementById('box'),bar=document.getElementById('bar'),msg=document.getElementById('msg');
i.onchange=()=>{l.innerHTML='';[...i.files].forEach(x=>{let d=document.createElement('div');d.className='file';d.textContent='📄 '+x.name;l.appendChild(d)});b.disabled=!i.files.length};
f.onsubmit=e=>{e.preventDefault();if(!i.files.length)return;let d=new FormData();[...i.files].forEach(x=>d.append('files',x));b.disabled=true;box.style.display='block';let x=new XMLHttpRequest();x.open('POST','/upload/{{token}}');x.upload.onprogress=e=>{if(e.lengthComputable){let p=Math.round(e.loaded/e.total*100);bar.value=p;msg.textContent='Uploading... '+p+'%'}};x.onload=()=>{if(x.status==200){bar.value=100;msg.textContent='✅ Transfer complete!';b.disabled=false;b.textContent='SEND MORE FILES';i.value='';l.innerHTML=''}else{msg.textContent='❌ Upload failed';b.disabled=false}};x.onerror=()=>{msg.textContent='❌ Connection failed';b.disabled=false};x.send(d)};
</script></body></html>"""

@app.get("/")
def phone():
    if request.args.get("token") != TOKEN:
        return "<h2 style='font-family:Arial;text-align:center;margin-top:20%'>Invalid or expired LocalDrop session.</h2>",403
    return render_template_string(PHONE,token=TOKEN)

@app.get("/pc")
def pc():
    return render_template_string(PC,qr=QR,url=URL)

@app.post("/upload/<token>")
def upload(token):
    if token != TOKEN: return "Invalid token",403
    count=0
    for f in request.files.getlist("files"):
        if f and f.filename:
            name=secure_filename(f.filename)
            if not name: continue
            stem,ext=os.path.splitext(name); n=1
            path=os.path.join(FOLDER,name)
            while os.path.exists(path):
                name=f"{stem}_{n}{ext}"; n+=1; path=os.path.join(FOLDER,name)
            f.save(path); count+=1
    return {"success":True,"count":count}

if __name__=="__main__":
    print(f"\nLocalDrop: http://{IP}:{PORT}/pc\nPhone: {URL}\nFiles: {FOLDER}\n")
    app.run(host="0.0.0.0",port=PORT,debug=False,threaded=True)
