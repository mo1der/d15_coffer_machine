import random
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
#
# shot_names = [person.upper() for person in names if len(person)>5]
# print(shot_names)

students_scores = {name:random.randint(1, 101) for name in names}
print(students_scores)

passed_students = {student:score for (student, score) in students_scores.items() if score > 50}
print(passed_students)