
import json
from threading import Thread
import time
#import Reader

students = []

def write_to_file():
    with open('record.json', 'w') as f:
        json.dump(students, f, indent=4)


#students.sort(key=lambda k: k['Searches'])
#size = (len(students))

size= int(input("plese enter dict size : "))


while True:
    if len(students) < size:
        student = {}
        #student['ID'] = int(input('enter id : '))
        student['Name'] = input('enter name : ')
        student['Searches'] = int()
        students.append(student)
        print(students)

    else:
        new =input('list full,add new ?')
        if new == 'yes':
            student['Name'] = input('enter new name : ')
            students.remove(student)
            students.append(student)
            print('new appneded:',students)

        # break
        else:
            break
    write_to_file()



# with open('record.json', 'w') as f:
#     json.dump(students, f, indent=4)


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




















