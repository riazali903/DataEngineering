import json


def read_from_file():
    with open('record.json') as f:
        return json.load(f)



def write_to_file():
    with open('record.json', 'w') as f:
        json.dump(students, f, indent=4)


students = read_from_file()

print(students)

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
                write_to_file()
                print('search update: ',student)
                print('updated list of students', students)
                break
        else:
            print('search does not exist')
            continue
            #break



find()



        # if contain is False:
        #     print('not found, add new')
        #     update_item = {'Name':search,'Searches':0}
        #     students.append(update_item)
        # write_to_file()







