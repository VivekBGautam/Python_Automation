# 🕒 Scripts on Scheduler

## 📌 Aim
To automate the execution of scripts at specific times or intervals using a scheduler, reducing manual effort and improving efficiency.

---

## 📖 Description
Scripts on Scheduler is a Python-based project that allows users to schedule and run scripts automatically. It helps in executing repetitive tasks like data backups, system monitoring, notifications, and more without manual intervention.

---

## ⚙️ Features
- Schedule scripts at fixed times
- Run tasks at regular intervals
- Simple and easy-to-use Python implementation
- Supports multiple scripts
- Logging and output tracking

---

## 🛠️ Technologies Used
- Python 3.x
- schedule library
- time module

---

## 📁 File Structure
scripts-on-scheduler/
│── scheduler.py
│── tasks/
│   ├── task1.py
│   ├── task2.py
│── logs/
│   └── scheduler.log
│── requirements.txt
│── README.md

---

## 🚀 Installation

1. Clone the repository:
git clone https://github.com/vivekbgautam/scripts-on-scheduler.git

2. Navigate to the project folder:
cd scripts-on-scheduler

3. Install dependencies:
pip install -r requirements.txt

---

## ▶️ Usage

Run the scheduler:
python scheduler.py

---

## 🧾 Example Code

import schedule
import time

def job():
    print("Task is running...")

schedule.every(10).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

---

## 📌 Use Cases
- Automated backups
- Sending reminders
- Running daily reports
- System maintenance tasks

---

## 🔮 Future Enhancements
- GUI-based scheduler
- Email/Notification integration
- Database support
- Advanced cron-like scheduling

---

## 👨‍💻 Author
Vivek Gautam  
Email: vivekbgautam@gmail.com  
GitHub: https://github.com/vivekbgautam  
LinkedIn: https://www.linkedin.com/in/vivek-b-gautam/
