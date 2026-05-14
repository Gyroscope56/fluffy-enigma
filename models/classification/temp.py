
# Put in the desired word length here
desiredLength = 5


with open("new.txt", "w+") as new:
    with open("words.txt", "r+") as file:
        for line in file:
            if (line != "" and len(line) == desiredLength+1 and line.strip().isalpha()):
                new.write(line.strip() + "\n")
    file.close()
new.close()