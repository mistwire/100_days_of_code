from pathlib import Path
import json

path = Path('numbers.json')
contents = path.read_text()        # Read the JSON file as a plain string
# json.loads() converts the JSON string back into a Python list.
# This is the READ half of the JSON save/load pattern. See number_writer.py for WRITE.
numbers = json.loads(contents)

print(numbers)  # This is a real Python list again, not just a string

