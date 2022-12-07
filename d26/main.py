# list = [1, 2, 3, 4]
# new_list = [el + 10 for el in list]
# print (new_list)
#
# name = "Piotr"
# new_name = [n.upper() for n in name]
# print(new_name)
#
# new_range = [n*2 for n in range(1, 5)]
# print(new_range)

import random
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
#
# shot_names = [person.upper() for person in names if len(person)>5]
# print(shot_names)

students_scores = {name:random.randint(1, 101) for name in names}
print(students_scores)