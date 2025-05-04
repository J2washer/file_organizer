
# 🗂️ File Organizer 

This Python script automatically organizes files in your **Downloads** folder into categorized subfolders based on file type (Images, Documents, Music, Videos, Archives, and Others).  
It's designed to work on **Windows, macOS, and Linux** with no manual path editing required.

## 📂 What it does

- Automatically detects your system's `Downloads` folder
- Sorts files into folders like:
  - `Images/` (.jpg, .png, etc.)
  - `Documents/` (.pdf, .docx, .txt, etc.)
  - `Videos/` (.mp4, .mov, etc.)
  - `Music/` (.mp3, .wav, etc.)
  - `Archives/` (.zip, .tar, etc.)
  - `Others/` for anything uncategorized

## 🛠️ How to Use

1. **Clone the repo:**

   ```bash
   git clone https://github.com/your-username/file-organizer.git
   cd file-organizer
    ````

2. **Run the script:**

   ```bash
   python organizer.py
   ```

   > Use `python3` if required on your system.

3. Sit back and watch your `Downloads` folder get organized!

## 📦 Requirements

This script uses only built-in Python libraries (`os`, `shutil`, and `pathlib`). No extra installation is needed.

## ✅ Features

* Cross-platform support
* Automatically creates folders if they don't exist
* Sorts files by extension
* Categorizes uncaught files into an `Others` folder

## ✨ Future Improvements (Pull Requests Welcome)

* Add subfolder scanning
* Support for user-defined custom categories
* Scheduled auto-runs (e.g. daily)

---

Made with 💻 by J2washer

