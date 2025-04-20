# DevOps Python Assignment

This repository contains solutions for Python DevOps assignment tasks. Each script demonstrates core concepts useful in DevOps automation and monitoring.

---

## 🔧 Question 1: Password Strength Checker

**File:** `password_checker.py`

- Checks if a password is strong based on:
  - Minimum 8 characters
  - Contains uppercase, lowercase, digits, and special characters
- Provides user-friendly feedback

Run with:

```bash
python password_checker.py
```

---

## 📊 Question 2: CPU Usage Monitor

**File:** `cpu_monitor.py`

- Continuously monitors CPU usage using `psutil`
- Displays alert if CPU usage exceeds 80%
- Stops safely with `Ctrl+C`

Install dependencies:

```bash
pip install psutil
```

Run with:

```bash
python cpu_monitor.py
```

---

## ⚙️ Question 3: Configuration File Parser & API

**Files:** 
- `config_parser.py` (Flask app)
- `config.ini` (sample configuration)

- Parses `.ini` configuration files
- Outputs data to `output.json`
- Serves a GET API on `/config`

Install dependencies:

```bash
pip install flask
```

Run with:

```bash
python config_parser.py
```

Access API:

```
GET http://localhost:5000/config
```

---

## 🗂️ Question 4: File Backup Script

**File:** `backup.py`

- Backs up files from a source to a destination directory
- Adds a timestamp to avoid overwriting existing files

Run with:

```bash
python backup.py /path/to/source /path/to/destination
```

---

## 🧪 Notes

- Scripts include error handling and clear output.
- Code is optimized and well-commented.

---

## 📁 Repository Structure

```
.
├── password_checker.py
├── cpu_monitor.py
├── config_parser.py
├── config.ini
├── output.json
├── backup.py
└── README.md
```
