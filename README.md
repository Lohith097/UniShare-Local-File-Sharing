# 🚀 UniShare Local Hub

A lightweight, local Wi-Fi file-sharing hub built for university classrooms. Turn any projector-connected desktop into a local server where students can instantly upload and download presentations, PDFs, and project files—no internet or USB drives required.

## ⚡ Quick Start (Classroom Setup)

### Option 1: The One-Line Command (Fastest)
If the classroom PC has Git and Python installed, open Command Prompt (`cmd`) and paste this single line to download and run the hub instantly:

```cmd
git clone [https://github.com/Lohith097/UniShare-Local-File-Sharing.git](https://github.com/Lohith097/UniShare-Local-File-Sharing.git) && cd UniShare-Local-File-Sharing && run_hub.bat
```

### Option 2: The Flash Drive / ZIP Method
If you have Python installed but don't want to use the terminal:
1. Click the green **Code** button and select **Download ZIP**.
2. Extract the folder to the desktop.
3. Double-click `run_hub.bat`. 

*The script will automatically check for Python, install the required QR code library, find the local Wi-Fi IP, and display a giant QR code on the projector.*

### Option 3: Standalone Executable (No Python Required)
If the classroom PC is locked down or does not have Python installed, use the pre-built executable.
1. Go to the [Releases](https://github.com/Lohith097/UniShare-Local-File-Sharing/releases) page and download `server.exe`.
2. Download `index.html` from the main repository.
3. Place both files in the exact same folder on your flash drive or desktop.
4. Double-click `server.exe` to launch the hub instantly.
