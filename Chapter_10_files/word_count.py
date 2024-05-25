from pathlib import Path

def count_words(path):
    """Count the approx # of words in a file"""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"The file {path} doesn't exist")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']

for file in filenames:
    path = Path(file)
    count_words(path)