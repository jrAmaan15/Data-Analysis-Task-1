# Task 1 – Data Cleaning: VS Code Setup Guide

## 1. Folder structure
Create a project folder and put these three files in it together:
```
task1-data-cleaning/
├── clean_data.py
├── Mall_Customers.csv
└── requirements.txt
```
(Use your original raw `Mall_Customers.csv` — the script will generate the cleaned output itself.)

## 2. Open in VS Code
- Open VS Code → **File > Open Folder** → select `task1-data-cleaning`
- If prompted, install the **Python extension** (by Microsoft) from the Extensions tab (`Ctrl+Shift+X`, search "Python")

## 3. Create a virtual environment (recommended)
Open a terminal in VS Code (`` Ctrl+` ``) and run:

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

VS Code may pop up "Select Interpreter" — choose the one inside `venv`.
(You can also select it manually: `Ctrl+Shift+P` → "Python: Select Interpreter" → pick `venv`)

## 4. Install dependencies
```bash
pip install -r requirements.txt
```

## 5. Run the script
```bash
python clean_data.py
```
Or just click the ▶️ "Run Python File" button in the top-right of VS Code while `clean_data.py` is open.

## 6. Output
After running, you'll see two new files appear in the folder:
- `Mall_Customers_cleaned.csv` – the cleaned dataset
- `cleaning_summary.txt` – a log of every change made

## Troubleshooting
- **"python not found"** → Install Python from python.org and check "Add to PATH" during install, then restart VS Code.
- **"No module named pandas"** → Make sure your venv is activated (you should see `(venv)` in the terminal prompt) and re-run `pip install -r requirements.txt`.
- **FileNotFoundError for CSV** → Make sure `Mall_Customers.csv` is in the same folder as `clean_data.py`, and that VS Code's terminal is opened at that folder (check with `pwd` / `cd`).
