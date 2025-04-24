import os
from datetime import datetime, timedelta
import webbrowser

# ----------------------------------------
# Web + System Tools
# ----------------------------------------

def open_browser():
    """Opens default web browser"""
    webbrowser.open("https://www.google.com")

def google_search(query):
    """Opens a google search for the given query"""
    search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    webbrowser.open(search_url)

def show_current_datetime():
    """Returns the current date and time"""
    now = datetime.now()
    return f"Today's date is: {now.strftime('%Y-%m-%d')}\nCurrent time is: {now.strftime('%H:%M:%S')}"

# ----------------------------------------
# File Management
# ----------------------------------------

def create_text_file(file_name):
    """Creates a blank text file with the given name"""
    file_path = "data/" + file_name if file_name.endswith(".txt") else "data/" + file_name + ".txt"
    open(file_path, "w").close()

def write_text_file(file_name):
    """Writes text to an already existing text file"""
    print("Start writing your text, type 'done' to start a new line and 'exit' to finish")
    new_lines = []
    curr_line_words = []
    file_path = "data/" + file_name if file_name.endswith(".txt") else "data/" + file_name + ".txt"

    if not os.path.exists(file_path):
        response = input("File doesn't exist, would you like me to create it? (yes/no): ")
        if response == "yes":
            create_text_file(file_name)
            print(f"Created file: {file_name}")
        else:
            print("Very well, sir. Standing by for your next command.")
            return

    while True:
        new_line = input()
        if new_line.strip().lower() == "exit":
            break
        elif new_line.strip().lower() == "done":
            new_lines.append(" ".join(curr_line_words))
            new_lines.append("")
            curr_line_words.clear()
        else:
            curr_line_words.extend(new_line.split())
            while len(curr_line_words) >= 25:
                line = " ".join(curr_line_words[:25])
                new_lines.append(line)
                curr_line_words = curr_line_words[25:]

    new_lines.append(" ".join(curr_line_words))

    with open(file_path, "a") as file:
        file.write("\n".join(new_lines) + "\n")
    print(f"Your text has been added to {file_name}")

def read_text_files(file_name):
    """Reads user specified text files and prints the content"""
    file_path = "data/" + file_name if file_name.endswith(".txt") else "data/" + file_name + ".txt"
    if not os.path.exists(file_path):
        print("Sir, I couldn't find the file you requested.")
    else:
        with open(file_path, "r") as file:
            content = file.read()
            print("Sir, Here is the content of the file you requested.")
            print(content)

def list_files():
    """Lists all files in the data directory"""
    files = os.listdir("data/")
    txt_files = [file for file in files if file.endswith(".txt")]
    if not txt_files:
        print("I couldn’t locate any .txt files in the archive, sir.")
        return

    print("Filename".ljust(30), "Size (KB)".ljust(12), "Last Modified")
    print("-" * 60)
    for file in txt_files:
        file_path = os.path.join("data", file)
        size_kb = round(os.path.getsize(file_path) / 1024, 2)
        modified_time = datetime.fromtimestamp(os.path.getmtime(file_path)).strftime("%Y-%m-%d %H:%M")
        print(file.ljust(30), f"{size_kb:.2f}".ljust(12), modified_time)

    print(f"\nSir, you currently have {len(txt_files)} file(s) in the data directory.")

def rename_file(new_name, old_name):
    """Renames an existing file within the data dictionary"""
    old_path = "data/" + old_name if old_name.endswith(".txt") else "data/" + old_name + ".txt"
    new_path = "data/" + new_name if new_name.endswith(".txt") else "data/" + new_name + ".txt"

    if not os.path.exists(old_path):
        print("I'm afraid I couldn't find the file you want to rename, sir.")
        return

    if os.path.exists(new_path):
        print("A file with the new name already exists, sir.")
        return

    os.rename(old_path, new_path)
    print(f"{old_name} has undergone a full identity transformation — now known as {new_name}, sir.")
    print("File rebranding complete. Anything else you'd like me to polish, sir?")

def delete_file(file_name):
    """Deletes user specified file from the data directory"""
    file_path = "data/" + file_name if file_name.endswith(".txt") else "data/" + file_name + ".txt"
    if not os.path.exists(file_path):
        print("I'm afraid that file doesn't exist, sir.")
        return

    confirmation = input(f"Are you sure you want me to delete {file_name}, sir? (yes/no): ").strip().lower()
    if confirmation != "yes":
        print("Deletion cancelled, sir.")
        return

    os.remove(file_path)
    print(f"{file_name} has been deleted from the system, sir.")

# ----------------------------------------
# File Cleanup Tools
# ----------------------------------------

def delete_empty_files():
    """Scans and deletes empty .txt files in the data directory after confirmation"""
    file_list = os.listdir("data/")
    empty_files = []

    for file in file_list:
        if file.endswith(".txt"):
            file_path = os.path.join("data", file)
            if os.path.getsize(file_path) == 0:
                empty_files.append(file)

    if not empty_files:
        print("Sir, There are no empty text files in the data directory.")
        return

    print("I’ve detected the following empty files, sir:")
    for file in empty_files:
        print(file)

    confirmation = input("Shall I delete them all, sir? (yes/no): ").strip().lower()
    if confirmation != "yes":
        print("Very well, sir. No files were harmed.")
        return

    for file in empty_files:
        os.remove(os.path.join("data", file))
    print("The unnecessary has been eliminated, sir. Archive status: pristine.")

def show_old_files(days=730):
    """Lists .txt files older than N days in the data directory"""
    file_list = os.listdir("data/")
    current_datetime = datetime.now()
    cutoff_datetime = current_datetime - timedelta(days=days)
    old_files = []

    for file in file_list:
        if file.endswith(".txt"):
            file_path = os.path.join("data", file)
            modified_datetime = datetime.fromtimestamp(os.path.getmtime(file_path))
            if modified_datetime < cutoff_datetime:
                old_files.append((file, modified_datetime))

    if not old_files:
        print(f"No files older than {days} days were found in the archive, sir.")
        return

    print("Scanning the archive for long-forgotten files, sir...")
    print(f"The following files haven't been modified in the last {days} days, sir:")
    for file, mtime in old_files:
        print(f" - {file} (last modified: {mtime.strftime('%Y-%m-%d')})")

    confirm = input("Would you like me to delete all of them, sir? (yes/no): ").strip().lower()
    if confirm != "yes":
        print("Understood, sir. No files were deleted.")
        return

    for file in old_files:
        os.remove(os.path.join("data", file[0]))
    print("The past has been purged, sir. The archive is immaculate once again.")
    
# ----------------------------------------
# Productivity Tools
# ----------------------------------------

def income_tax_calc(yearly_income, c_deductions, d_self, d_parents, home_loan_interest):
    """Calculates income tax based based on income slab"""
    standard_rebate = 50000
    taxable_income = yearly_income - standard_rebate
    total_deductions = c_deductions+d_self+d_parents+home_loan_interest
    taxable_income-=total_deductions
    slabs=[(300001,600000,0.05),(600001,900000,0.10),(900001,1200000,0.15),(1200001,1500000,0.20)]
    tax=0
    if taxable_income<=300000:
        return "No tax applicable"
    if taxable_income<=700000:
        return "Tax is ₹0 due to rebate under Section 87A"
    for lower, upper, rate in slabs:
        if taxable_income>lower:
            slab_income=min(taxable_income,upper)-lower
            tax+=slab_income*rate
    if taxable_income>1500000:
        tax+=(taxable_income-1500000)*0.30
        
    return f"Total tax on income ₹{yearly_income:,} is ₹{int(tax):,}"
    