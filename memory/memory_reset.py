import os
from datetime import datetime
from memory.memory import reset_monthly_expense

def check_and_reset_monthly_expense():
    """Checks if a new month has started and resets the monthly expense if necessary."""
    reset_file= "memory/last_reset.txt"
    current_month= datetime.now().strftime("%Y-%m")
    if not os.path.exists(reset_file):
        with open(reset_file, "w") as file:
            file.write(current_month)
        print("Initializing monthly tracking, sir. Resetting archive for the first time.")
        reset_monthly_expense()
        
    with open(reset_file, "r") as file:
        last_reset_month = file.read().strip()
            
    if last_reset_month != current_month:
        print("New month detected, sir. Executing monthly archive protocol...")
        reset_monthly_expense()
        with open(reset_file, "w") as file:
            file.write(f"{current_month}")

    
        