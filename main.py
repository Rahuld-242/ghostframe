from tools.basic_tools import (
    open_browser,
    create_text_file,
    show_current_datetime,
    google_search, 
    write_text_file, 
    list_files, 
    read_text_files, 
    delete_file, 
    rename_file, 
    delete_empty_files,
    show_old_files,
    income_tax_calc
)
from memory.memory import (
    remember,
    recall,
    forget,
    add_expenses,
    view_expenses,
    set_budget,
    view_budget,
    edit_expense,
    delete_expense,
    manage_category_deletion,
    delete_budget_category,
    reset_monthly_expense
    )
from datetime import datetime
from memory.memory_reset import check_and_reset_monthly_expense

check_and_reset_monthly_expense()

print("Hello! I am Jarvis, at your service")

exit_commands = ["exit", "quit", "close", "stop"]

while True:
    user_input = input("Enter your command: ").strip().lower()
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open("data/log.txt", "a") as log_file:
        log_file.write(f"[{current_datetime}] User typed: {user_input}\n")

    # ----------------------------
    # System and Web Commands
    # ----------------------------

    if user_input == "open browser":
        open_browser()

    elif user_input == "current date and time":
        print(show_current_datetime())

    elif user_input.startswith("search "):
        query = user_input.replace("search ", " ")
        google_search(query)

    elif user_input == "search":
        query = input("What would you like me to search for? ")
        google_search(query)

    # ----------------------------
    # File Management Commands
    # ----------------------------

    elif user_input == "create text":
        file_name = input("Enter the file name: ")
        create_text_file(file_name)
        print(f"Created blank file: {file_name}")

    elif user_input in ["write text", "write text to file", "add notes"]:
        file_name = input("Which file would you like to write to? ")
        write_text_file(file_name)

    elif user_input.startswith("read file"):
        file_name = input("Which file would you like me to read? ")
        read_text_files(file_name)

    elif user_input == "list files":
        list_files()
        print("As per your request, sir, I have scanned the archive.")

    elif user_input.startswith("rename file"):
        parts = user_input.replace("rename file", "").strip().split(" to ")
        if len(parts) == 2:
            old_name, new_name = parts[0].strip(), parts[1].strip()
            rename_file(new_name, old_name)
        else:
            print("Please use the format: rename file old_name to new_name, sir.")

    elif user_input.startswith("delete file"):
        parts = user_input.split(maxsplit=2)
        if len(parts) == 3:
            key = parts[2]
            delete_file(key)
        else:
            print("Please specify the file you want me to delete, sir.")

    # ----------------------------
    # File Cleanup Tools
    # ----------------------------

    elif user_input in ["delete empty files", "delete_empty_files", "delete_empty_file"]:
        delete_empty_files()

    elif user_input == "show old files":
        print("Initiating archival integrity scan, sir...")
        show_old_files()

    # ----------------------------
    # Memory Commands
    # ----------------------------

    elif user_input.startswith("remember"):
        parts = user_input.split(maxsplit=2)
        if len(parts) == 3:
            key, value = parts[1], parts[2]
            remember(key, value)
            print(f"I'll remember that your {key} is {value}, sir.")
        else:
            print("Please specify what I should remember, sir.")

    elif user_input.startswith("recall"):
        parts = user_input.split()
        key = parts[-1]
        value = recall(key)
        if value:
            print(f"Your {key} is: {value}, sir.")
        else:
            print(f"I'm afraid, I don't know your {key} yet, sir.")

    elif user_input.startswith("forget"):
        parts = user_input.split(maxsplit=1)
        if len(parts) == 2:
            key = parts[1]
            success = forget(key)
            if success:
                print(f"I've erased the memory of your {key}, sir.")
            else:
                print(f"I don't recall anything about your {key}, sir.")
        else:
            print("Please specify what you'd like me to forget, sir.")
            
    # ----------------------------
    # Income Tax calculator
    # ----------------------------
    elif user_input in ["calculate tax", "calculate income tax", "income tax calculator"]:
        try:
            income = int(input("Please enter your total annual income **in numbers only** (e.g., 800000): ").replace(",", ""))
            lic=int(input("Enter 80C deductions (LTC, ELSS, etc.), max ₹1,50,000: "))
            lic=min(lic,150000)
            
            med_self=int(input("Medical insurance for self/family (max ₹25,000): "))
            med_self=min(med_self, 25000)
            
            med_parents=int(input("Medical insurance for parents (max ₹50,000): "))
            med_parents=min(med_parents, 50000)
            
            loan=int(input("Home loan interest (max ₹2,00,000): "))
            loan=min(loan, 200000)
            if income<0:
                print("Income cannot be negative, sir. Please try again.")
            else:
                result=income_tax_calc(income, lic, med_self, med_parents, loan)
                print("Here's your tax breakdown, sir:")
                print(result)
        except ValueError:
            print("That doesn't appear to be a valid number, sir")
                
    # ----------------------------
    # Expense Tracker
    # ----------------------------
    elif user_input in ["track my expense", "add expenses", "add expense"]:
        add_expenses()
        
    elif user_input in ["view expenses", "show expenses", "show my expenses", "view my expenses"]:
        print("Here is your expense log, sir.")
        view_expenses()
                
    elif user_input == 'set budget':
        
        while True:
            category = input("Which category shall I assign the budget to, sir? ")
            try:
                
                budget = float(input("And the budget limit for this category, if I may ask? ₹"))
                if budget < 0:
                    print("Sir, a budget cannot be negative. Kindly provide a positive value.")
                else:
                    set_budget(category, budget)
                    break
            except ValueError:
                print("That doesn't appear to be a valid number, sir. Please try again.")
            
    elif user_input in ["view budget", "show budget", "show my budget", "view my budget"]:
        print("Here is your budget, sir.")
        view_budget()
        
    elif user_input in ["edit my expenses", "edit expenses", "edit expense"]:
        print("Very well, Sir")
        edit_expense()
        
    elif user_input in ["delete my expense", "delete expense"]:
        print("Very well, sir. Locating the specified entry...")
        print("Entry locked. Preparing for surgical deletion.")
        delete_expense()
        
    elif user_input in [
        "delete expense category",
        "manage category deletion",
        "clear category",
        "remove expense category",
        "delete all expenses in category"
    ]:
        print("Initiating category management protocol, sir...")
        manage_category_deletion()
        
    elif user_input in ["delete budget", "remove budget category", "clear my budget"]:
        print("Initiating budget deletion sequence, sir. I assume this is intentional and not a moment of fiscal panic.")
        delete_budget_category()

    # ----------------------------
    # Exit Command
    # ----------------------------

    elif user_input in exit_commands:
        print("Goodbye Sir!")
        break

    # ----------------------------
    # Fallback
    # ----------------------------

    else:
        print(f"Sorry Sir, I didn't understand the command: {user_input}")
