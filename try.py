#import json

# students = []
# students.sort(key= lambda k : k['Searches'])
#
# size = int(input("plese enter dict size : "))
# if size <= 10:
#     for i in range(size):
#         dict = {}
#         dict['ID'] = int(input('enter id : '))
#         dict['Name'] = input('enter name : ')
#         dict['Searches'] = int()
#         students.append(dict)
#         with open('rooo.json', 'w') as f:
#             json.dump(students, f,indent=4)



# students = {}
# n = 3
# for i in range(n):
#     ID =input('enter id : ')
#     Name = input('enter name : ')
#     students[ID] = Name
#     j = json.dumps(students, indent=4)
#     with open('record.json', 'w') as f:
#         f.write(j)
#
# with open('record.json','r') as jfile:
#     jstd = json.load(jfile)
#
# searches =[]
# search = input('enter search')
# searches.append(search)
# searches = list(zip(ID,search))
# print('THis is json : ',jstd)
# print(searches)

# students = []
# n = 3
# for i in range(n):
#     dict ={}
#     dict['ID'] = int(input('enter id : '))
#     dict['Name'] = input('enter name : ')
#     dict['Searches'] = int()
#     students.append(dict)
#     j2 = json.dumps(students, indent=4)
#     with open('record.json', 'w') as f:
#         f.write(j2)
#



# with open('record.json') as f:
#     students = json.load(f)
# #
# # sresults = []
# # search= [int(input('enter your search'))]
# # sresults.append(search)
# #
# # for student in students:
# #     if student['ID'] == search:
# #         student['Searches'] += 1
# #         print(student)
#
# for student in students:
#     print(student['Searches'])
















import json
import time

with open('rooo.json') as f:
    students = json.load(f)
#students.sort(key= lambda k : k['Searches'])
while True:
    contain = False
    search = input('enter your search')
    students.sort(key=lambda k: k['Searches'], reverse=True)

    for student in students:
        if student['Name'] == search:
            sCount = student['Searches']
            students.remove(student)
            #student['Searches'] += 1
            contain = True
            update_item = {"Searches": sCount + 1, "Name": search}
            students.append(update_item)
            with open('rooo.json', 'w') as f:
                json.dump(students, f, indent=4)

    if contain is False:
        print('not found, add new')
        update_item = {'Searches':0,'Name':search}
        # dict['ID'] = int(input('enter id : '))
        # dict['Name'] = input('enter name : ')
        # dict['Searches'] = 0
        # dict['Name'] = search
        students.append(update_item)
        with open('rooo.json', 'w') as f:
            json.dump(students, f, indent=4)




