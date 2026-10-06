# 📱 PhoneTransfer — LocalDrop

> **Fast, private, and simple phone-to-PC file transfer over your local network.**

PhoneTransfer is a lightweight Windows-based file transfer utility that lets you send files from your **Android/iPhone browser directly to your Windows PC**.

The PC creates a temporary local transfer session and displays a **QR code**. Scan the QR code with your phone, select your files, and send them directly to the PC.

**No cloud storage. No account. No USB cable.**

---

## ✨ Features

- 📱 **Phone → PC file transfer**
- 🔳 **QR code pairing**
- 🌐 **Local network transfer**
- ☁️ **No cloud upload**
- 📁 **Multiple file selection**
- ⚡ **Direct browser-based transfer**
- 📊 **Upload progress**
- 🎨 **Modern responsive UI**
- 🔐 **Temporary session token**
- 🛡️ **Windows Firewall support**
- 📂 Automatic `Received_Files` folder
- 🚀 Simple `.bat` launcher
- 🐍 Powered by Python + Flask

---

## 🖥️ How It Works

```text
                    SAME LOCAL NETWORK
                           │
             ┌─────────────┴─────────────┐
             │                           │
             ▼                           ▼
       💻 WINDOWS PC                 📱 PHONE
             │                           │
             │ Start LocalDrop           │
             │                           │
             ▼                           │
       Local Flask Server                │
             │                           │
             ▼                           │
       Generate QR Code                  │
             │                           │
             └──────────────┐            │
                            │            │
                            ▼            ▼
                         🔳 QR CODE ← Scan
                                         │
                                         ▼
                                  Phone Browser
                                         │
                                         ▼
                                  Select Files
                                         │
                                         ▼
                                    SEND FILES
                                         │
                                         │ HTTP
                                         ▼
                              💻 LocalDrop Server
                                         │
                                         ▼
                                  Received_Files/
```

The files travel directly between the phone and PC through the local network.

---

# 🚀 Quick Start

## 1. Download the Project

Clone the repository:

```bash
git clone https://github.com/rsamwilson2323-cloud/PhoneTransfer.git
```

Enter the project:

```bash
cd PhoneTransfer
```

---

## 2. Start PhoneTransfer

Double-click:

```text
PhoneTransfer.bat
```

The launcher will:

1. Check Python
2. Install required packages
3. Start the LocalDrop server
4. Detect the PC's local IP address
5. Configure the local firewall rule
6. Start the transfer server
7. Open the LocalDrop dashboard in Chrome

---

# 📱 Using PhoneTransfer

### Step 1 — Connect to the Same Network

Connect both:

```text
💻 PC
   +
📱 Phone
```

to the **same Wi-Fi/LAN network**.

---

### Step 2 — Start LocalDrop

Run:

```text
PhoneTransfer.bat
```

Chrome will open the LocalDrop dashboard.

---

### Step 3 — Scan the QR Code

The PC dashboard displays a QR code.

Use your phone camera to scan it.

The phone will automatically open the LocalDrop transfer page.

---

### Step 4 — Select Files

On your phone:

```text
📁 Select Files
```

You can select one or multiple files.

For example:

```text
📷 photo.jpg
🎥 video.mp4
📄 document.pdf
📦 project.zip
```

---

### Step 5 — Send

Tap:

```text
SEND FILES TO PC
```

The upload progress will be displayed on your phone.

---

### Step 6 — Find Your Files

Transferred files are saved automatically inside:

```text
Received_Files/
```

Example:

```text
PhoneTransfer/
│
├── PhoneTransfer.bat
├── localdrop.py
├── README.md
├── LICENSE
│
└── Received_Files/
    ├── photo.jpg
    ├── video.mp4
    ├── document.pdf
    └── project.zip
```

---

# 🎨 User Interface

## PC Dashboard

The PC interface provides:

- LocalDrop branding
- QR code
- Local network address
- Connection instructions
- Transfer status
- Privacy information

Example:

```text
┌─────────────────────────────────────────────┐
│                                             │
│   📱 LocalDrop          SCAN TO CONNECT     │
│                                             │
│   Phone → PC              ┌───────────┐     │
│                           │           │     │
│   ✓ Local Network         │ QR CODE   │     │
│   ✓ No Cloud              │           │     │
│   ✓ Multiple Files        └───────────┘     │
│                                             │
│   1. Connect to same Wi-Fi                 │
│   2. Scan QR code                          │
│   3. Select files                          │
│   4. Send                                  │
│                                             │
│           🟢 Waiting for phone...           │
│                                             │
└─────────────────────────────────────────────┘
```

---

# 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| 🪟 Windows Batch | Application launcher |
| 🐍 Python | Backend server |
| 🌐 Flask | Local HTTP server |
| 🔳 QRCode | QR generation |
| 🖼️ Pillow | QR image processing |
| 🌐 HTML | Web interface |
| 🎨 CSS | UI design |
| ⚡ JavaScript | Upload handling |
| 📡 HTTP | Local file transfer |

---

# 📂 Project Structure

```text
PhoneTransfer/
│
├── 📄 PhoneTransfer.bat
│
├── 🐍 localdrop.py
│
├── 📄 README.md
│
├── 📄 LICENSE
│
└── 📁 Received_Files/
       └── Your transferred files
```

### `PhoneTransfer.bat`

The Windows launcher.

It starts the application and prepares the required environment.

### `localdrop.py`

The main Flask server responsible for:

- Creating the local transfer server
- Generating the QR code
- Serving the phone interface
- Receiving uploaded files
- Saving files locally
- Handling transfer sessions

### `Received_Files/`

Destination folder for files transferred from the phone.

---

# 🔐 Privacy

PhoneTransfer is designed for **local network transfers**.

Files are transferred directly:

```text
📱 Phone
   │
   │ Local Network
   ▼
💻 Your PC
```

There is no project-specific cloud storage or remote file server involved.

Your files are saved locally in:

```text
Received_Files/
```

> **Important:** Your network itself still needs to be trusted. Anyone who can access the local transfer endpoint and obtain the active session URL/token may potentially interact with the transfer service.

---

# 🔳 QR Code Pairing

Instead of manually typing the PC's IP address, LocalDrop creates a temporary QR code.

Example:

```text
http://192.168.x.x:8765/?token=XXXXXXXX
```

The phone scans the QR code and opens the transfer interface.

This makes the connection process:

```text
Start
  ↓
QR Generated
  ↓
Scan
  ↓
Select Files
  ↓
Upload
  ↓
Complete
```

---

# 📊 Upload Progress

PhoneTransfer supports browser-based upload progress.

During transfer, the phone displays:

```text
Uploading... 45%
████████████░░░░░░░░
```

After successful transfer:

```text
✅ Files sent successfully!
```

---

# 🛡️ Security

The application uses a temporary transfer token for the active session.

The transfer URL contains a token such as:

```text
?token=XXXXXXXX
```

This prevents a random request without the valid session token from directly uploading through the protected upload endpoint.

For additional security:

- Use PhoneTransfer only on trusted networks
- Avoid exposing port `8765` to the public internet
- Do not port-forward the application
- Close the application after completing the transfer
- Use a trusted/private Wi-Fi network

---

# ⚙️ Requirements

### PC

- Windows 10 or Windows 11
- Python 3.9+
- Internet connection for initial Python package installation
- Chrome or another modern browser
- Local Wi-Fi/LAN connection

### Phone

No dedicated application is required.

A modern mobile browser and camera are sufficient.

Supported workflow:

```text
Android
   +
Chrome
   +
Camera
```

or

```text
iPhone
   +
Safari
   +
Camera
```

---

# 📦 Python Dependencies

The application uses:

```text
Flask
QRCode
Pillow
```

The BAT launcher installs them automatically with:

```bash
python -m pip install flask qrcode pillow
```

You normally don't need to install them manually.

---

# 🧪 Example

Suppose the PC has this local IP:

```text
192.168.1.105
```

LocalDrop starts on:

```text
http://192.168.1.105:8765
```

The PC dashboard can be opened at:

```text
http://192.168.1.105:8765/pc
```

The phone scans the generated QR code.

Then:

```text
📱 Phone
    │
    │ Select photo.jpg
    │ Select video.mp4
    │
    ▼
 SEND FILES
    │
    ▼
💻 PC
    │
    ▼
Received_Files/
    ├── photo.jpg
    └── video.mp4
```

---

# ❗ Troubleshooting

## Chrome doesn't open

Open the dashboard manually:

```text
http://127.0.0.1:8765/pc
```

---

## Phone cannot connect

Check that:

```text
💻 PC ────────┐
              │
           SAME Wi-Fi
              │
📱 Phone ─────┘
```

Both devices must be on the same local network.

---

## Windows Firewall blocks the connection

Allow Python/LocalDrop through Windows Defender Firewall when Windows asks.

The application uses TCP port:

```text
8765
```

---

## `python` is not recognized

Install Python and make sure:

```text
Add Python to PATH
```

is enabled during installation.

Then restart Command Prompt.

---

## Files are not appearing

Check:

```text
Received_Files/
```

inside the PhoneTransfer project directory.

The application creates this folder automatically.

---

# 💡 Why LocalDrop?

Traditional file transfer often requires:

```text
USB cable
    or
Cloud storage
    or
Third-party application
```

LocalDrop simplifies this to:

```text
📱 Scan QR
      ↓
📁 Select Files
      ↓
📤 Send
      ↓
💻 PC
```

Fast, simple, and convenient.

---

# 🔮 Future Improvements

Possible future features:

- [ ] PC → Phone transfer
- [ ] Drag-and-drop uploads
- [ ] Download files from PC
- [ ] File preview
- [ ] Image preview
- [ ] Video preview
- [ ] Transfer history
- [ ] Transfer speed display
- [ ] Remaining time
- [ ] Cancel transfer
- [ ] Pause/resume
- [ ] Multiple simultaneous devices
- [ ] Automatic session expiration
- [ ] Custom transfer port
- [ ] Dark/light themes
- [ ] Password-protected sessions
- [ ] HTTPS support
- [ ] Desktop GUI
- [ ] Standalone `.exe`
- [ ] Automatic startup option
- [ ] Phone → PC and PC → Phone two-way transfer

---

# 🚀 Roadmap

### Version 1.0

```text
✓ Local server
✓ QR pairing
✓ Phone upload
✓ Multiple files
✓ Upload progress
✓ Modern UI
```

### Version 2.0

```text
□ Two-way transfer
□ File browser
□ Download from PC
□ Transfer history
□ Better security
```

### Version 3.0

```text
□ Standalone Windows EXE
□ Multi-device support
□ Advanced transfer controls
□ Native desktop interface
```

---

# 👨‍💻 Author

## Sam Wilson

**B.E. CSE — Artificial Intelligence & Machine Learning**

GitHub:

[rsamwilson2323-cloud](https://github.com/rsamwilson2323-cloud?utm_source=chatgpt.com)

---

# ⭐ Repository

**PhoneTransfer**

[PhoneTransfer GitHub Repository](https://github.com/rsamwilson2323-cloud/PhoneTransfer?utm_source=chatgpt.com)

If you find the project useful, consider giving the repository a ⭐.

---

# 📜 License

This project is released under the **MIT License**.

See [`LICENSE`](LICENSE) for details.

---

## ⚡ Quick Start

```bash
git clone https://github.com/rsamwilson2323-cloud/PhoneTransfer.git

cd PhoneTransfer
```

Then run:

```text
PhoneTransfer.bat
```

Scan the QR code with your phone, select your files, and send them directly to your PC.

---

### 📱 Phone → 🔳 QR → 💻 PC

**No cloud. No USB. Just local transfer.**
