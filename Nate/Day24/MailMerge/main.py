name_list = []
replaced_string = "[name]"

with open('./input/Names/invited_names.txt', mode='r') as f:
    for name in f.readlines():
        name_list.append(name.strip('\n'))

with open('./input/Letters/starting_letter.txt', mode='r') as j:
    letter = j.read()
    for name in name_list:
        with open(f'./Output/ReadyToSend/{name}.txt', mode='w') as f:
            f.write(letter.replace(replaced_string, name))
