# sort-photos

**sort-photos** is a minimalist, dependency-free image sorting tool written in pure Python. It scans a directory full of image files and organizes them into a structured folder system based on either **creation date** or **file type**.

> **Tidy up your photos with ease — sort by date or type, preview results before making changes, and enjoy a clutter-free photo archive.**

---

## ⚡ sort-photos Features

- 📅 **Sort by Date**  
  Organizes images by creation date into a clean year/month/day folder structure.

- 🗂️ **Sort by Type**  
  Groups files by image type (`.jpg`, `.png`, etc.).

- 👀 **Dry Run Mode**  
  Preview changes before committing.

- 🧰 **Pure Python**  
  No external libraries required — simple and fast.

- 💡 **Zero Setup**  
  Just point to a folder and sort.

---

## 📁 Supported File Types

- `.png`
- `.jpg` / `.jpeg`
- `.gif`
- `.bmp`

---

## 🚀 Running sort-photos

Update the `DATA_PATH` variable in `main.py` to the folder you want to sort.

```python
# Example in main.py
DATA_PATH = "/path/to/your/image/folder"

```
Run the script from your terminal:

bash
Copy
Edit
# Sort by Date
python main.py -d
# or
python main.py --date

# Sort by Type
python main.py -t
# or
python main.py --type
🔒 Dry Run Mode is enabled by default.
You'll see a simulated folder structure before any changes are made, and be prompted to continue.

🏗️ Example Output
Sorting by Date:

yaml
Copy
Edit
📁 Sorted_Photos/
├── 2024/
│   ├── 03/
│   │   ├── 22/
│   │   │   ├── IMG_001.jpg
│   │   │   └── beach_day.png
Sorting by Type:

css
Copy
Edit
📁 Sorted_Photos/
├── jpg/
│   ├── IMG_001.jpg
│   └── selfie.jpg
├── png/
│   └── beach_day.png
├── gif/
│   └── animation.gif
🔗 Inspirations and References
Local File Organizer by QiuYannnn

Naztech Automated Data Sorting Tools

FileWizardAI by AIxHunter


# 🛠️ Artisan AI Suite

**Artisan AI Suite** is a powerful, lightweight collection of AI-powered tools designed for artists, content creators, and portfolio managers.

Launched in **November 2024**, Artisan AI Suite makes it easy to sort and manage art portfolios, automate social media posting, and generate intelligent blog content suggestions — all using **local AI models** for privacy and control.

---

## 🧠 Overview

Artisan AI Suite provides:

- 📂 **Portfolio Organization**  
  Automatically sort and clean up art archives by type, creation date, or custom categories.

- 📣 **Social Media Automation**  
  Generate AI-powered post captions and schedule uploads across platforms.

- 📝 **Content Suggestion Engine**  
  Get intelligent blog topic ideas based on your portfolio, recent works, or social trends — no cloud connection required.

Artisan AI Suite is built for speed, simplicity, and full user control — without depending on external servers or APIs.

---