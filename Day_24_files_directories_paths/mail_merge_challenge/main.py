#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp



# PATTERN: Mail merge - template-based document generation
# Separates data (names) from format (letter template) for reusable automation

# Step 1: Read all names to process
# KEY CONCEPT: readlines() returns list with newlines: ["Alice\n", "Bob\n"]
# This is different from read() which returns one string
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

# Step 2: Read template letter (once, outside loop - efficient pattern)
# PATTERN: Read template once, then loop through data using it repeatedly
# This is faster and clearer than reading the template inside the loop
with open("./Input/Letters/starting_letter.txt", mode="r") as letter_file:
    letter_contents = letter_file.read()  # Entire letter as one string

    # Step 3: For each name, create personalized letter
    for name in names:
        # KEY CONCEPT: string.replace(old, new) returns new string with substitutions
        # This requires stripping newlines from readlines() output
        new_letter = letter_contents.replace("[name]", name.strip())

        # Step 4: Write personalized letter to output file
        # PATTERN: Use f-string for dynamic filename based on data
        # mode="w" creates new file each time (or overwrites if exists)
        with open(f"./Output/letter for {name.strip()}.txt", mode="w") as file:
            # NOTE: writelines() doesn't add newlines; it writes exactly what you give it
            # new_letter already contains all formatting from template
            file.writelines(new_letter)



#         for i in name:
#             for blank in letter:
#                 if "[name]" in blank:
#                     blank.replace("[name]", i)
#                     print(i)
#             with open(f"./Output/letter for {i}", mode="w") as file:
#                 letter[0] = letter[0].replace("[name]", i.strip())
#                 file.writelines(letter)
    