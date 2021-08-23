
import json
from threading import Thread
import time


students = []
#students.sort(key=lambda k: k['Searches'])
size = (len(students))
size= int(input("plese enter dict size : "))



for student in range(size):
    if len(students) <= size:
        student = {}
        #student['ID'] = int(input('enter id : '))
        student['Name'] = input('enter name : ')
        student['Searches'] = int()
        students.append(student)
        size +=1
        with open('rooo.json', 'w') as f:
            json.dump(students, f,indent=4)

# else:
#     while True:
#         contain = False
#         search = input('enter your search')
#         students.sort(key=lambda k: k['Searches'], reverse=True)
#
#         for student in students:
#             if student['Name'] == search:
#                 sCount = student['Searches']
#                 students.remove(student)
#                 contain = True
#                 update_item = {"Name": search, "Searches": sCount + 1}
#                 students.append(update_item)
#
#         if contain is False:
#             print('not found, add new')
#             update_item = {'Name': search, 'Searches': 0}
#             students.append(update_item)
#         with open('rooo.json', 'w') as f:
#             json.dump(students, f, indent=4)
#


#search= int(input('enter your search'))




















