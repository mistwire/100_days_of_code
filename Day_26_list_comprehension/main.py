# Read in both files as a list
with open("file1.txt") as f1:
    file1 = f1.readlines()
    # file1_clean = [int(x.strip()) for x in file1]

with open("file2.txt") as f2:
    file2 = f2.readlines()
    # file2_clean = [int(x.strip()) for x in file2]

result = [int(i) for i in file1 if i in file2]

# Write your code above 👆

print(result)


