from pathlib import Path
import json

numbers = [2, 3, 5, 7, 11, 13]

path = Path('numbers.json')
# json.dumps() converts a Python list to a JSON string: '[2, 3, 5, 7, 11, 13]'
# Then write_text() saves that string to a file.
# This is the WRITE half of the JSON save/load pattern. See number_reader.py for LOAD.
contents = json.dumps(numbers)
path.write_text(contents)
