# Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: This method will help you: https://www.w3schools.com/python/ref_string_strip.asp

text_to_be_replaced = '[name]'

# Create a list of names:
with open('Input/Letters/starting_letter.txt') as letter:
    letter = letter.read()

# Get text string to be manipulated:
with open('Input/Names/invited_names.txt') as names:
    names = names.readlines()

# Loop through names and strip/replace to string & print:
for name in names:
    stripped_name = name.strip()
    new_text = letter.replace(text_to_be_replaced, name)
    with open(f"Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as f:
        f.write(new_text)