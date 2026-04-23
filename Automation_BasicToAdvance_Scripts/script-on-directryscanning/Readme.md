# 📁 Directory Scanner Automation Script (Python)

## 🚀 Overview

The **Directory Scanner Automation Script** is a Python-based utility designed to scan directories, analyze file structures, and generate useful insights such as file counts, sizes, and file types. It’s especially useful for automation, storage analysis, and system organization.

---

## 🎯 Aim

To develop a Python script that automatically scans a directory and provides detailed information about files and folders.

---

## 🧠 Features

* 🔍 Recursively scans directories and subdirectories
* 📊 Counts total files and folders
* 📁 Identifies file types
* 💾 Calculates total directory size
* ⚡ Fast and efficient
* 🔧 Easily extendable for automation tasks

---

## 🗂️ File Structure

```
DirectoryScanner/
│── directory_scanner.py
│── README.md
```

---

## 🧾 Requirements

* Python 3.x
* Built-in modules only (`os`)

---

## 🛠️ How It Works

1. User inputs a directory path
2. Script traverses all subdirectories
3. Collects:

   * File count
   * Folder count
   * File sizes
4. Displays results clearly

---

## 💻 Sample Code

```python
import os

def scan_directory(path):
    total_size = 0
    file_count = 0
    folder_count = 0

    for root, dirs, files in os.walk(path):
        folder_count += len(dirs)
        file_count += len(files)

        for file in files:
            file_path = os.path.join(root, file)
            if os.path.exists(file_path):
                total_size += os.path.getsize(file_path)

    print(f"Scanned Directory: {path}")
    print(f"Total Files: {file_count}")
    print(f"Total Folders: {folder_count}")
    print(f"Total Size: {total_size / (1024*1024):.2f} MB")

# Run the script
directory_path = input("Enter directory path: ")
scan_directory(directory_path)
```

---

## ▶️ How to Run

```bash
python directory_scanner.py
```

---

## 📌 Example Output

```
Enter directory path: C:/Users/Vivek/Documents

Scanned Directory: C:/Users/Vivek/Documents
Total Files: 120
Total Folders: 15
Total Size: 45.67 MB
```

---

## 🔧 Future Enhancements

* Export results (CSV / JSON)
* GUI version
* File filtering (size, type, date)
* Auto-cleanup feature
* Logging system

---

## 📎 Use Cases

* Storage analysis
* Automation tasks
* File organization
* Backup verification

---

## 👨‍💻 Author

**Vivek Gautam**
📧 Email: [vivekbgautam@gmail.com](mailto:vivekbgautam@gmail.com)
🔗 GitHub: https://github.com/vivekbgautam
🔗 LinkedIn: https://www.linkedin.com/in/vivek-b-gautam/

---

## ⭐ Conclusion

A simple yet powerful automation script to scan and analyze directories. Great for learning and real-world use!
