# 📘 Assignment_31 – Directory Automation Scripts (Python)

---

## 📌 Aim

To design and implement automation scripts in Python that perform various directory operations such as:

- Searching files by extension  
- Renaming file extensions  
- Copying all files from one directory to another  
- Copying files with specific extensions  

The scripts follow robust programming practices including command line argument handling, validation, exception handling, modular design, and logging.

---

## 📂 File Structure
  
```
Assignment_31/
│
├── DirectoryFileSearch.py   // Display files with given extension
├── DirectoryRename.py       // Rename files from one extension to another
├── DirectoryCopy.py         // Copy all files from source to destination
├── DirectoryCopyExt.py      // Copy files with specific extension
└── DirectoryLog.txt         // Log file generated at runtime
```

---

## 📝 Program Details

---

### 🔹 DirectoryFileSearch.py

**Description:**  
Accepts directory name and file extension from user and displays all files with that extension.

**Usage:**  
```
python DirectoryFileSearch.py Demo .txt
```

**Result:**  
All `.txt` files from `Demo` directory are recorded in `DirectoryLog.txt`.

---

### 🔹 DirectoryRename.py

**Description:**  
Accepts directory name and two file extensions.  
Renames all files with first extension to the second extension.

**Usage:**  
```
python DirectoryRename.py Demo .txt .doc
```

**Result:**  
All `.txt` files in `Demo` directory are renamed to `.doc`.

---

### 🔹 DirectoryCopy.py

**Description:**  
Accepts two directory names.  
Copies all files from source directory to destination directory.  
Destination directory is created at runtime.

**Usage:**  
```
python DirectoryCopy.py Demo Temp
```

**Result:**  
All files from `Demo` directory are copied into `Temp` directory.

---

### 🔹 DirectoryCopyExt.py

**Description:**  
Accepts two directory names and one file extension.  
Copies only files with specified extension from source directory to destination directory.  
Destination directory is created at runtime.

**Usage:**  
```
python DirectoryCopyExt.py Demo Temp .exe
```

**Result:**  
All `.exe` files from `Demo` directory are copied into `Temp` directory.

---

## ⚙️ Features Implemented

- Command line argument handling  
- Directory validation before operation  
- Extension validation  
- Separate function for each task  
- Log file based output (no console printing)  
- Runtime directory creation  
- Robust exception handling  
- Modular and structured programming approach  

---

## 📄 Output

All operation details, success messages, and error messages are stored inside:

```
DirectoryLog.txt
```

---

## 🛠️ Technologies Used

- Python 3.x  
- sys module  
- os module  
- shutil module  
- logging module  

---

## 🎯 Learning Outcomes

- Practical understanding of file and directory handling in Python  
- Usage of `os.walk()` for directory traversal  
- Safe file path handling using `os.path.join()`  
- Working with `shutil` module for file copying  
- Implementing logging for professional automation scripts  
- Exception handling for robust applications  

---

## 👨‍💻 Author

**Vivek Bhauraj Gautam**  
📅 Assignment No: 31  

---

## 🔗 Connect with Me

📧 Email: vivekbgautam@gmail.com 
 
💻 GitHub: https://github.com/vivekbgautam  

---



