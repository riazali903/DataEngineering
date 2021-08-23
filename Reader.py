import json


def from_json():
    with open('record.json') as f:
        return json.load(f)

students = from_json()


def to_json():
    with open('record.json', 'w') as f:
        json.dump(students, f, indent=4)


#students.sort(key= lambda k : k['Searches'])
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

    if contain is False:
        print('not found, add new')
        update_item = {'Name':search,'Searches':0}
        students.append(update_item)
    to_json()






