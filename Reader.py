
import json
from threading import Thread
import time
from Writer import write_to_file

# def read_from_file():
#     with open('record.json') as f:
#         return json.load(f)

def read_from_file():
    with open('record.json') as f:
        students =json.load(f)
        return students



students = read_from_file()


#students.sort(key= lambda k : k['Searches'])
def find():

    while True:
        contain = False
        search = input('enter your search')
        students.sort(key=lambda k: k['Searches'], reverse=True)

        for student in students:
            if student['Name'] == search:
                sCount = student['Searches']
                students.remove(student)
                contain = True
                update_item = { "Name": search,"Searches": sCount + 1}
                students.append(update_item)
                print('search update: ',student)
                print('Current size of file: ',len(students))
                print('updated list of students', students)
                break
                print('after break',students)
        else:
            #print('search does not exist')
            new = input('does not exist, enter yes or no ?')
            if new == 'yes':
                student['Name'] = input('enter new name : ')
                students.remove(student)
                students.append(student)
                print('new appended:', students)
            else:
                break
        with open('record.json', 'w') as f:
            json.dump(students, f, indent=4)

find()

