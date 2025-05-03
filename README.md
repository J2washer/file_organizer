File Organizer
A simple and efficient file organizer that automatically sorts files in a directory into categorized folders based on file types. Ideal for cleaning up your Downloads folder or desktop.

Features
Automatically moves files into folders (e.g., Images, Documents, Videos, etc.)

Customizable file type categories

Easy to set up and run

Cross-platform (Windows, macOS, Linux)

Getting Started
Prerequisites
Make sure you have Python 3 installed on your system. You can check by running:

bash
Copy
Edit
python --version
Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/J2washer/file_organizer.git
cd file_organizer
(Optional) Create a virtual environment:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies (if any):

bash
Copy
Edit
pip install -r requirements.txt
Usage
Run the script with:

bash
Copy
Edit
python organiser.py
You can edit the script to point to any directory you want to organize.

Customization
You can change the file type categories or target directory directly in the script:

python
Copy
Edit
# Example inside organiser.py
target_folder = "/path/to/your/folder"
file_types = {
    "Images": [".jpg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mov"],
    # Add your own categories
}
License
This project is licensed under the MIT License - see the LICENSE file for details.

