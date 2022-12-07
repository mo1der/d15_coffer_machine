# import pandas
#
# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     print(key)#Access key and value
#     pass
#
# student_data_frame = pandas.DataFrame(student_dict)
#
# # print(student_data_frame)
#
# for (index, row) in student_data_frame.iterrows():
#     print(row.score)
#
#
# # import pandas
# # student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass
#
# # # Keyword Method with iterrows()

import pandas

# with open("nato_phonetic_alphabet.csv") as file:
#     nato_data = file.read()
#
# nato_data_df = pandas.DataFrame(nato_data)

nato_data = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_dict = {row.letter:row.code for (index, row) in nato_data.iterrows()}

user_word = input("Enter a world").upper()

new_word = [nato_dict[item] for item in user_word]
print(new_word)
#
# #TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
#
# #TODO 2. Create a list of the phonetic code words from a word that the user inputs.
#

