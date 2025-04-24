# Ghostframe: A Command-Line Personal Assistant
**GhostFrame** is a Python-based personal assistant inspired by J.A.R.V.I.S., designed to operate via the command line. It helps with tasks ranging from basic file operations to income tax calculations and expense tracking.

***
## Features

### Basic Tools
- `open browser` - Opens Google in your default browser
- `google search` or `search <query>` - Initiates a Google search
- `create text` - Creates a blank .txt file
- `write text` - Appends formatted text to a file
- `read file` - Displays contents of a specified file
- `list files` - Lists all .txt files in the `data/` folder
- `delete <filename>` - Deletes a specified file
- `rename file old_name to new_name` - Renames a file
- `delete empty files` - Deletes all empty text files
- `show old files` - Lists files not modified in 2 years with delete option

### Memory Tools
- `remember key value` - Stores a key-value pair
- `recall <key>` - Retrieves the value
- `forget <key>` - Removes the key-value pair

### Income Tax Assistant
- `calculate tax` - Asks for annual income and deductions (80C, 80D, home loan) to compute tax based on India's new tax regime slabs

### Expense Tracker
- `add expense` - Logs an expense by category, amount, date, time and description
- `view expense` - Displays all logged expenses, category wise
- `set budget` - Sets category-wise budget with overwrite confirmation
- `view budget` - Displays budget (all/specific category)
- `edit expense` - Edit any field of an expense entry
- `delete expense` - Delete a specific entry
- `manage category` - Clear entries or delete an entire category
- `delete budget category` - Removes a category from budgets
- `reset monthly expense` - Archives all old expenses into `archives/` and resets `expenses.json`

### Automation
- Monthly auto-archive on first run of a new month using memory_reset.py

***

## Folder Structure
```
├── agents/
│   └── llm_agent.py (LLM integration placeholder)
├── data/
│   └── *.txt files (created or modified by user)
├── memory/
│   ├── memory.py (expense, tax, budget logic)
│   ├── memory_reset.py (monthly archiver)
│   ├── archives/ (archived monthly expense snapshots)
├── tools/
│   └── basic_tools.py (file utilities, browser, etc.)
├── main.py (entry point)
├── requirements.txt
```
***

## Requirements
- Python 3.8+
- No external dependencies (built-in libraries only)
***

## To Run
```python
python main.py
```
***

## Roadmap
- GUI Integration
- LLM-based natural command recognition
- Email, document and folder automation
- Mobile-friendly app
***

## Suggested .gitignore
```
__pycache__/
data/*.txt
memory/expenses.json
memory/budgets.json
memory/last_reset.txt
memory/archives/
```
***

Ghostframe is a quiet sentinel - productive, efficient, and always ready to assist

***

**Developed** by: Rahul Dutta


