# 🧠 Script on Input, Output & Exception Handling (Python Automation)

## 📌 Aim
 
To create Python scripts that handle **user input**, **formatted output**, and **exception handling**, making automation scripts more robust, user-friendly, and error-resistant.

---

## 📂 Project Overview

This project demonstrates how to:

* Take dynamic input from users
* Display clean and structured output
* Handle runtime errors using exception handling
* Build reliable automation scripts

---

## 🛠️ Technologies Used

* Python 3.x

---
<!--
## 📁 File Structure

```
script-on-input-output-exception/
│
├── program01_input.py
├── program02_output.py
├── program03_exception_basic.py
├── program04_multiple_exceptions.py
├── program05_custom_exception.py
└── README.md
```

---
-->
## 🚀 Programs Description

### 🔹 program01_input.py

* Demonstrates taking input from user
* Uses `input()` function
* Converts input into required data types

👉 Example:

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("Hello", name, "Age:", age)
```

---

### 🔹 program02_output.py

* Shows formatted output techniques
* Uses f-strings and formatted printing

👉 Example:

```python
name = "Vivek"
age = 21
print(f"My name is {name} and I am {age} years old.")
```

---

### 🔹 program03_exception_basic.py

* Basic exception handling using `try-except`
* Handles common errors like division by zero

👉 Example:

```python
try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

---

### 🔹 program04_multiple_exceptions.py

* Handles multiple exceptions in one program
* Uses multiple `except` blocks

👉 Example:

```python
try:
    num = int(input("Enter number: "))
    result = 10 / num
    print(result)
except ValueError:
    print("Invalid input! Enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

---

### 🔹 program05_custom_exception.py

* Demonstrates user-defined exceptions
* Improves control over error handling

👉 Example:

```python
class NegativeValueError(Exception):
    pass

try:
    num = int(input("Enter a number: "))
    if num < 0:
        raise NegativeValueError("Negative value not allowed!")
except NegativeValueError as e:
    print(e)
```

---

## 🎯 Key Concepts Covered

* Input Handling (`input()`)
* Output Formatting (f-strings)
* Exception Handling (`try-except-finally`)
* Multiple Exception Handling
* Custom Exceptions

---

## 💡 Real-World Use Cases

* CLI tools
* Automation scripts
* Data validation systems
* Error-proof applications

---

## ▶️ How to Run

1. Install Python (if not installed)
2. Open terminal or command prompt
3. Navigate to project folder
4. Run any program:

```bash
python program01_input.py
```

---

## 🔗 Connect with Me

* 📧 Email: [vivekbgautam@gmail.com](mailto:vivekbgautam@gmail.com)
* 💻 GitHub: https://github.com/vivekbgautam
* 🔗 LinkedIn: https://www.linkedin.com/in/vivek-b-gautam/

---

## ⭐ Conclusion

This project builds a strong foundation in **handling user interaction and errors**, which is essential for creating **reliable Python automation scripts**.

---
