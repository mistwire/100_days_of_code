#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp



with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt", mode="r") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        new_letter = letter_contents.replace("[name]", name.strip())
        with open(f"./Output/letter for {name}.txt", mode="w") as file:
            file.writelines(new_letter)



#         for i in name:
#             for blank in letter:
#                 if "[name]" in blank:
#                     blank.replace("[name]", i)
#                     print(i)
#             with open(f"./Output/letter for {i}", mode="w") as file:
#                 letter[0] = letter[0].replace("[name]", i.strip())
#                 file.writelines(letter)
    