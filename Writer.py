
import json


students = []
students.sort(key= lambda k : k['Searches'])

size = int(input("plese enter dict size : "))
if size <= 10:
    for i in range(size):
        dict = {}
        dict['ID'] = int(input('enter id : '))
        dict['Name'] = input('enter name : ')
        dict['Searches'] = int()
        students.append(dict)
        with open('record.json', 'w') as f:
            json.dump(students, f,indent=4)
# else:
#     for student in students:
#         print(min(student['Searches']))




#search= int(input('enter your search'))




















