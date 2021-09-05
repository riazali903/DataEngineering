import json


class Writer:

    def __init__(self,name,size):
        self.name = name
        self.size = size
        self.students = []

    def write_to_file(self,obj):
        with open('record.json', 'w') as f:
            json.dump(obj, f, indent=4)


    def read_from_file(self):
        with open('record.json') as f:
            students = json.load(f)
            return students

    def main(self):
        self.students = self.read_from_file()
        self.students.sort(key=lambda k: k['Searches'], reverse=True)
        student = {}
        while len(self.students) < self.size:
            student = {'Name': input('enter name : '), 'Searches': int()}
            self.students.append(student)
            self.write_to_file(self.students)

        new = input('list full,add new, enter yes or no ?')
        if new == 'yes':
            self.update()

    def update(self):
        students = self.read_from_file()
        students.sort(key=lambda k: k['Searches'])
        print('update this',students)
        if len(students) == 0:
            print('List is empty')
            self.main()
        else:
            add_new = input('please add new')
            for student in students:
                if student['Name'] != add_new:
                    students.remove(student)
                    add_item = {"Name": add_new, "Searches": 0}
                    students.append(add_item)
                    students.sort(key=lambda k: k['Searches'])
                    self.write_to_file(students)
                    break

def call_writer():
    size = int(input('what is size?'))
    writer1 = Writer("instance writer1",size)
    writer1.main()






# with open('students.json') as f:
#     students = json.load(f)
# #students.sort(key=lambda k: k['Searches'])
# print(students)
# search = input('search : ')
# for student in students:
#     if student['Name'] != search:
#         students.remove(student)
#         update_item = {"Name": search, "Searches": 0}
#         students.append(update_item)
#         print(students)
#         with open('students.json', 'w') as f:
#             json.dump(students, f, indent=4)
#         break
#
#
# print('updated one :',students)



