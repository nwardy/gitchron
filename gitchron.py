import os
from datetime import datetime
import subprocess

repo_path = "/Users/natewardy/Desktop/gitchron"

os.chdir(repo_path)

log_file = "log.txt"

# Increment the number in the log file
if os.path.exists(log_file):
    with open(log_file, "r") as file:
        lines = file.readlines()
    
    # Extract the last number or default to 0
    last_number = int(lines[-1].strip()) if lines else 0
    new_number = last_number + 1
else:
    new_number = 1  # Start at 1 if the file doesn't exist

# Append the new number to the log file
with open(log_file, "a") as file:
    file.write(f"{new_number}\n")

# Add the file to the Git index
subprocess.run(["git", "add", log_file], check=True)

# Commit the changes
commit_message = f"Update log with number {new_number} on {datetime.now().strftime('%Y-%m-%d')}"
subprocess.run(["git", "commit", "-m", commit_message], check=True)

# Push to the reote repository
subprocess.run(["git", "push"], check=True)

print(f"Log updated with number: {new_number}")
