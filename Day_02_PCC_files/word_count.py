from pathlib import Path

def count_words(path):
    """Count the approx # of words in a file"""
    # TRY/EXCEPT/ELSE pattern:
    # - try: code that might fail (file might not exist)
    # - except: runs ONLY if the specific error occurs
    # - else: runs ONLY if try succeeded (no error)
    try:
        contents = path.read_text(encoding='utf-8')  # encoding='utf-8' handles special characters
    except FileNotFoundError:
        # Catches only this specific error. The program continues running
        # instead of crashing -- 'siddhartha.txt' is missing but that's OK.
        print(f"The file {path} doesn't exist")
    else:
        # split() with no args splits on any whitespace (spaces, tabs, newlines).
        # This gives a rough word count.
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")

# Notice: 'siddhartha.txt' doesn't exist, but the program won't crash.
# The except block handles it, and the loop continues to the next file.
filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']

for file in filenames:
    path = Path(file)
    count_words(path)