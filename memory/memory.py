import os
import json
from datetime import datetime

def remember(key, value):
    # Define a path to the memory file
    memory_file="memory/memory.json"
 
    # Load current memory (if file exists)
    if os.path.exists(memory_file):
        with open(memory_file, "r") as file:
            data=json.load(file)
    else:
        data={}

    # Update memory
    data[key] = value 

    # Save back to Json
    with open(memory_file, "w") as file:
        json.dump(data, file, indent=4)
        
def recall(key):
    # Define the memory file path
    memory_file="memory/memory.json"
    
    # Check if the file exists
    if not os.path.exists(memory_file):
        return None
    
    # Load the file
    with open(memory_file,"r") as file:
        data=json.load(file)
    
    # Return the requested file
    return data.get(key)
        
def forget(key):
    memory_file="memory/memory.json"
    
    if not os.path.exists(memory_file):
        return False
    
    with open(memory_file,"r") as file:
        data=json.load(file)
        
    if key in data:
        del data[key]
        with open(memory_file, "w") as file:
            json.dump(data, file, indent=4)
        return True
    
    else:
        return False
    
def add_expenses():
    """Adds daily expenses to an expense tracker file"""
    expense_file="memory/expenses.json"
    
    if not os.path.exists(expense_file):
        with open(expense_file, "w") as file:
            json.dump({}, file, indent=4)
            expenses={}
    else:
        with open(expense_file,"r") as file:
            expenses=json.load(file)
    
    category=input("Enter the category of the expense: ")
    try:
        amount=float(input("Enter the amount spent: "))
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
        return
    description=input("Enter a description of the expense: ")
    date=input("Enter the date of the expense (YYYY-MM-DD): ")
    time=input("Enter the time of the expense (HH:MM): ")
    
    if not date:
        date=datetime.now().strftime("%Y-%m-%d")
    if not time:
        time=datetime.now().strftime("%H:%M")
    
    if category not in expenses:
        expenses[category]=[]
        
    expense={
        "amount": amount,
        "description": description,
        "date": date,
        "time": time
    }
    
    expenses[category].append(expense)
        
    with open(expense_file, "w") as file:
        json.dump(expenses, file, indent=4)
    print(f"Logged ₹{amount} under '{category}' for '{description}' on {date} at {time}, sir.")
    
    budgets_file="memory/budgets.json"
    with open(budgets_file, "r") as file:
        budgets=json.load(file)
            
    categorical_expenditure=0
    tot_expenditure=0
    
    for items in expenses[category]:
        categorical_expenditure+=items.get("amount", 0)
    print(f"Sir, Your total expenditure for {category} is ₹{categorical_expenditure:.2f}")
    
    for entries in expenses.values():
        for entry in entries:
            tot_expenditure+=entry.get("amount", 0)
        
    budget_limit=budgets.get(category, 0)
    
    if budget_limit is not None:
        if categorical_expenditure>budget_limit:
            print(f"Status : Over budget by ₹{categorical_expenditure-budget_limit:.2f}\n")
        else:
            print(f"Status : ₹{budget_limit-categorical_expenditure:.2f} remaining\n")
    else:
        print(f"Sir, you haven't set a budget for {category} yet.")
        
    print(f"Sir, Your total expenditure is ₹{tot_expenditure:.2f}")
    
def view_expenses():
    """Displays the logged expenses in the expense tracker"""
    expenses_file="memory/expenses.json"
    
    if not os.path.exists(expenses_file):
        print("Sir, I am afraid you have not logged any expenses yet.")
        return
    
    with open(expenses_file, "r") as file:
        expenses=json.load(file)
        
    for category, entry in expenses.items():
        print(f"\n {category} ")
        if not entry:
            print("No expenses logged in this category.")
        else:
            for expense in entry:
                amount=expense.get("amount", "")
                description=expense.get("description", "")
                date=expense.get("date", "")
                time=expense.get("time", "")
                print(f"  - ₹{amount:.2f} | {description} | {date} @ {time}")
        
def set_budget(category, budget):
    """Sets a budget for the specified category"""
    budget_file="memory/budgets.json"
    
    if not os.path.exists(budget_file):
        with open(budget_file, "w") as file:
            json.dump({}, file, indent=4)
            budgets={}
    else:
        with open(budget_file, "r") as file:
            budgets=json.load(file)
            
    budget=float(budget)
    
    if category in budgets:
        choice=input("Sir, you have already set a budget for this category, would you like to update it? (yes/no): ").strip().lower()
        if choice != "yes":
            print("Very well, sir. The budget remains unchanged")
            return
    budgets[category]=budget
    
    with open(budget_file, "w") as file:
        json.dump(budgets, file, indent=4)
    
    print(f"Sir, a budget of ₹{budget} has been set for {category}")
    
def view_budget():
    """Displays the set budgets"""
    budget_file="memory/budgets.json"
    
    if not os.path.exists(budget_file):
        print("Sir, I am afraid you have not set any budgets yet.")
        return
        
    with open(budget_file, "r") as file:
        budgets=json.load(file)
    
    
    while True:  
        choice=input("Would you like to see all budgets or a specific category? (all/specific): ").strip().lower()    
        if choice == "all":  
            print("\nSir, here are your allocated budgets:\n")
            # Header
            print("Category".ljust(20) + "| " + "Budget".rjust(12))
            print("-" * 35)
            
            for category in budgets:
                budget=budgets[category]
                print(f"{category.title().ljust(20)}| ₹{budget:>11.2f}")   
                
            # Footer
            print("-" * 35)
            print(f"Total Budget: ₹{len(budgets)}\n")
    
        elif choice == "specific":
            specific_category=input("Which category budget would you like to view? ")
            if specific_category in budgets:
                print(f"Sir, the budget you've set for '{specific_category.title()}' is ₹{budgets[specific_category]:,.2f}.")
            else:
                print(f"I'm afraid I couldn't locate a budget for '{specific_category}', sir.")
        
        elif choice == "done":
            print("Exiting budget view")
            break
        else:
            print("Apologies, sir. I didn't quite catch that. Please type 'all' or 'specific'.")

def edit_expense():
    """Lets the user edit his logged expenses"""
    expense_file="memory/expenses.json"
    
    if not os.path.exists(expense_file):
        print("Sir, I am afraid you have not logged any expenses yet.")
        return
    
    with open(expense_file, "r") as file:
        expenses=json.load(file)
    
    print("The available categories are:")
    for category in expenses:
        print(category)
        
    choice=input("Which category would you like to edit? ").strip()
    if choice not in expenses:
        print("Sir, I am afraid I couldn't locate that category.")
        return
    print(f"Sir, here are the logged expenses under '{choice}':")
    for i, expense in enumerate(expenses[choice], start=1):
        amount=expense.get("amount", "")
        description=expense.get("description", "")
        date=expense.get("date", "")
        time=expense.get("time", "")
        print(f"{i}. ₹{amount:.2f} | {description} | {date} @ {time}")
            
    try:
        entry_choice=int(input("Which entry would you like to edit? "))
        if entry_choice < 1 or entry_choice > len(expenses[choice]):
            print("That doesn't seem to be a valid entry, please try again.")
            return
    except ValueError:
        print("The value you entered doesn't appear to be a number, please try again.")
        return
            
    index=entry_choice-1
    selected_entry=expenses[choice][index]   
    field_choice=input("Which field would you like to edit? (amount/description/date/time): ").strip()
    if field_choice not in ["amount", "description", "date", "time"]:
        print("Sorry sir, that's not a valid field.")
        return
    new_value=input(f"Please enter the new {field_choice}: ")
    if field_choice == "amount":
        try:
            new_value=float(new_value)
        except ValueError:
            print("That doesn't appear to be a valid number, sir.")
            return
    selected_entry[field_choice] = new_value
            
    with open(expense_file, "w") as file:
        json.dump(expenses, file, indent=4)
                
    print(f"Sir, the {field_choice} for entry {entry_choice} has been successfully updated.")
    
def delete_expense():
    """Deletes a specific expense entry"""
    expense_file="memory/expenses.json"
    
    if not os.path.exists(expense_file):
        print("Sir, I am afraid you have not logged any expenses yet.")
        return
    
    with open(expense_file, "r") as file:
        expenses=json.load(file)
    
    print("The available categories are: ")   
    for category in expenses:
        print(category)
        
    cat_choice=input("Which category would you like to delete an entry from? (Type 'cancel' to exit) ").strip()
    if cat_choice.lower() == "cancel":
        print("Understood sir, Deletion aborted")
        return
    if cat_choice not in expenses:
        print("Sir, I am afraid I couldn't locate that category.")
        return
    print(f"Sir, here are the logged expenses under '{cat_choice}':")
    for i, expense in enumerate(expenses[cat_choice], start=1):
        amount=expense.get("amount", "")
        description=expense.get("description", "")
        date=expense.get("date", "")
        time=expense.get("time", "")
        print(f"{i}. ₹{amount:.2f} | {description} | {date} @ {time}")
        
    entry_choice=input("Which entry would you like to delete? (Type 'cancel' to exit) ")
    if entry_choice.lower() == "cancel":
        print("Understood sir, Deletion aborted")
        return
    try:
        entry_choice=int(entry_choice)
        if entry_choice < 1 or entry_choice > len(expenses[cat_choice]):
            print("That doesn't seem to be a valid entry, please try again.")
            return
    except ValueError:
        print("The value you entered doesn't appear to be a number, please try again.")
        return
    
    confirm=input("Are you sure you want to delete this entry? (yes/no): ").strip().lower()
    if confirm != "yes":
        print("Very well, sir, deletion cancelled")
        return
    expenses[cat_choice].pop(entry_choice-1)
    with open(expense_file, "w") as file:
        json.dump(expenses, file, indent=4)
        
    print("Removal complete. The record no longer exists.")
    
def manage_category_deletion():
    """Manages the deletion of a category from the expense tracker"""
    expense_file="memory/expenses.json"
    if not os.path.exists(expense_file):
        print("Sir, I am afraid you have not logged any expenses yet. ")
        return
    with open(expense_file, "r") as file:
        expenses=json.load(file)
        
    print("The available categories are: ")
    for category in expenses:
        print(category)
        
    cat_choice=input("Which category would you like me to manage? (Type 'cancel' to exit) ").strip()
    if cat_choice.lower() == "cancel":
        print("Understood sir, Deletion process aborted")
        return
    cat_or_ent=input(f"Shall I clear all entries in '{cat_choice}', or delete the entire category?\n"
    "Type 'clear' to empty the category or 'delete' to remove it completely: (Type 'cancel' to exit) ").strip().lower()
    if cat_or_ent == "cancel":
        print("Understood sir, Deletion process aborted")
        return
    if cat_or_ent == "clear":
        if not expenses[cat_choice]:
            print(f"Sir, the category '{cat_choice}' is already empty.")
            return
        expenses[cat_choice] = []
        print(f"All entries in '{cat_choice}' have been cleared, sir.")
    elif cat_or_ent == "delete":
        del expenses[cat_choice]
        print(f"The category '{cat_choice}' has been deleted from the archive, sir.")
    else:
        print("I didn't understand that request, sir. No changes made.")
        return
    with open(expense_file, "w") as file:
        json.dump(expenses, file, indent=4)
    
def delete_budget_category():
    budget_file="memory/budgets.json"
    
    if not os.path.exists(budget_file):
        print("Sir, I am afraid you have not set any budgets yet.")
        return
    
    with open(budget_file, "r") as file:
        budgets=json.load(file)
        
    print("Sir, Here are your budget categories: ")
    for category in budgets:
        print(category)
        
    cat_choice=input("Which category would you like to delete? (Type 'cancel' to exit) ").strip()
    if cat_choice.lower() == "cancel":
        print("Understood sir, Deletion process aborted")
        return
    
    if cat_choice not in budgets:
        print("I'm afraid I couldn't find that category in your budgets, sir.")
        return
    
    confirmation=input(f"Are you absolutely certain you wish to remove the budget for '{cat_choice}', sir? (yes/no): ").strip().lower()
    if confirmation != "yes":
        print("Very well, sir. Deletion protocol canceled.")
        return
    del budgets[cat_choice]
    with open(budget_file, "w") as file:
        json.dump(budgets, file, indent=4)
    print(f"The budget for '{cat_choice}' has been removed, sir.")
    
def reset_monthly_expense():
    """Resets the expense every month"""
    expense_file="memory/expenses.json"
    
    if not os.path.exists(expense_file):
        print("Sir, I am afraid you have not logged any expenses yet.")
        return
    
    with open(expense_file, "r") as file:
        expenses=json.load(file)
        
    monthly_archives={}
    
    for categories, entries in expenses.items():
        for entry in entries:
            date=entry.get("date", "")
            year_month=datetime.strptime(date, "%Y-%m-%d").strftime("%Y-%m")
            
            if year_month not in monthly_archives:
                monthly_archives[year_month] = {}
                
            if categories not in monthly_archives[year_month]:
                monthly_archives[year_month][categories] = []
                
            monthly_archives[year_month][categories].append(entry)
    
    current_month=datetime.now().strftime("%Y-%m")
            
    for date in monthly_archives:
        archive_file=f"memory/archives/expenses_{date}.json"
        
        if date==current_month:
            continue
        
        if not os.path.exists(os.path.dirname(archive_file)):
            os.makedirs(os.path.dirname(archive_file))
        
        with open(archive_file, "w") as file:
            json.dump(monthly_archives[date], file, indent=4)
            
    for category in expenses:
        current_month_entries=[]
        for entry in expenses[category]:
            entry_date=entry.get("date", "")[:7]
            if entry_date == current_month:
                current_month_entries.append(entry)
        expenses[category]=current_month_entries
                
    with open(expense_file, "w") as file:
        json.dump(expenses, file, indent=4)
        
    print("Sir, all previous months have been archived and current month data retained.")
            
            
        
        
    