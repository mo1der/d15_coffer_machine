# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# with open(r'.\Input\Names\invited_names.txt') as file_with_names:
    # names = file_with_names.read()

file_with_names = open(r'.\Input\Names\invited_names.txt', "r")
names = file_with_names.readlines()
file_with_names.close()

print(names)
names2 = []
for a in names:
    w = a.replace("\n", "")
    names2.append(w)
print(names2)

print(names2[0])
with open(r'.\Input\Letters\starting_letter.txt') as file_starting_letter:
    starting_letter = file_starting_letter.read()

print(starting_letter)

for person in range(len(names2)):
    letter = starting_letter.replace("[name]", f"{names[person]}")
    final_letter = letter.replace("\n", "", 1)
    file_name = "letter_to_" + names[person]
    file_name = file_name.replace("\n", "", 1)
    file = open(f'.\Output\ReadyToSend\{file_name}.txt', mode="w")
    file.write(final_letter)

file_starting_letter.close()

# print(letter1.replace("\n", "", 1))

# with open(r'.\Output\ReadyToSend\person.txt', mode="w") as letter_to_lerson:
#     zawartosc = letter_to_lerson.read()