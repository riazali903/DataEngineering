import json
import time

with open('record.json') as f:
    students = json.load(f)

while True:
    contains = False
    search = int(input('enter your search'))
    students.sort(key=lambda k: k['Searches'], reverse=True)


    for student in students:

        if student['ID'] == search:
            student['Searches'] += 1
            contains = True
            with open('record.json', 'w') as f:
                json.dump(students, f, indent=4)

    if contains is False:
        student['ID'] != search
        print('not found, add new')
        del students[-1]
        dict = {}
        dict['ID'] = int(input('enter id : '))
        dict['Name'] = input('enter name : ')
        dict['Searches'] = 0
        students.append(dict)
        with open('record.json', 'w') as f:
            json.dump(students, f, indent=4)





# for a in students:
#     min(a['Searches'])
# def find(id):
#     return user['id']
#
# search= input('enter your search')
#
#
# for student in students:
#     if student['ID']== search:
#         student['Searches'] +=1

    # if search in student:
    #     student["Searches"] += 1
    # else:
    #     print("not found")


# for i in student:
#     if search == i:
#         student["searches"] += 1
#     time.sleep(5)
