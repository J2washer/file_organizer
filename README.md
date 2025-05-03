
# 📁 File Organizer

**Automatically sort and organize your messy folders with ease!**  
A Python-based tool that categorizes files into folders based on their file types—perfect for tidying up directories like Downloads or Desktop.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/Python-3.6%2B-blue.svg)](https://www.python.org/downloads/)

---

## ✨ Features

- ✅ Organizes files into folders by type (Images, Documents, Videos, etc.)
- 🔧 Fully customizable file-type categories
- ⚙️ Lightweight and fast
- 🖥️ Works on Windows, macOS, and Linux

---

## 🚀 Getting Started

### 📦 Prerequisites

Make sure Python 3 is installed. To check:

```bash
python --version
````

### 📥 Installation

1. **Clone this repository:**

```bash
git clone https://github.com/J2washer/file_organizer.git
cd file_organizer
```

2. **(Optional) Create and activate a virtual environment:**

```bash
# Linux/macOS
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

---

## ⚡ Usage

Simply run the script:

```bash
python organiser.py
```

The script will organize the default directory, or you can customize it.

---

## 🛠️ Customization

Edit the script to set your target directory and file type categories:

```python
# organiser.py

target_folder = "/path/to/your/folder"
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Archives": [".zip", ".tar", ".gz"],
    # Add more categories as needed
}
```

---

## 📄 License

This project is licensed under the **MIT License**.
See the [LICENSE](LICENSE) file for more details.

---

## 🤝 Contributing

Feel free to fork the repo, submit pull requests, or open issues!
Any feedback or improvements are welcome.

