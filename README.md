# PYTHON SCRIPT FOR LOGGING FILE IN A DIRECTORY
# File Monitoring Script

## Overview
This Python script scans a target directory and logs details about all files found in that directory.  
It records the filename, file size (in KB), and last modified timestamp, then writes the results to a `log.txt` file.

---

## How to run the script
### 1. Requirements
- Python 3.x installed
- No external libraries required (uses only built-in modules)

---

### 2. Clone repo
```bash
git clone https://github.com/AmoahEmmanuelLarbi/devops-internship-assignment.git
```
### 3. Navigate to project folder
- Open a terminal
```bash
cd path/to-project-folder/
```
### 4. Run the script
- Open a terminal in the project folder and run:

```bash
python monitor.py
```

#### Output

- `log.txt` is created/overwritten in the project root.
- Each row contains: file name, size (KB), and last modified timestamp.
- `log.txt` itself is skipped so it does not appear in its own output.


### Assumptions Made
- The script assumes the target directory is the same folder where the script is located.
- Only the files in the target directory are scanned.