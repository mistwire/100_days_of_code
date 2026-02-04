from pathlib import Path
import json

# FUNCTION DECOMPOSITION: This program is split into 3 focused functions.
# Each one does ONE thing. This makes the code easier to read, test, and debug.

def get_stored_username(path):
    """Get stored username if available"""
    if path.exists():
            contents = path.read_text()
            username = json.loads(contents)  # JSON string -> Python object
            return username
    else:
         return None  # Explicit return of None signals "no data found"

def get_new_username(path):
    """Prompt for new username"""
    username = input("What is your name? ")
    contents = json.dumps(username)  # Python object -> JSON string
    path.write_text(contents)        # Persist to disk so it survives between runs
    return username

def greet_user():
    """Greet user by name"""
    # ORCHESTRATOR function: coordinates the other two functions.
    # It doesn't do file I/O itself -- it delegates to specialized functions.
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        print(f"Welcome back {username}!")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")

greet_user()