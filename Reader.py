import json
from threading import Thread
import time

class Reader:
    def __init__(self,search):
        self.search = search
        self.students = []

    def read_from_file(self):
        with open('record.json') as f:
            record = json.load(f)
            return record

    def write_to_file(self):
        with open('record.json', 'w') as f:
            json.dump(self.students, f, indent=4)

    def find(self):
        self.students = self.read_from_file()

        for student in self.students:
            if student['Name'] == self.search:
                count = student['Searches']
                self.students.remove(student)
                # contain = True
                update_item = { "Name": self.search,"Searches": count + 1}
                self.students.append(update_item)
                # print('search update: ',student)
                print('Current size of file: ',len(self.students))
                self.students.sort(key=lambda k: k['Searches'], reverse=True)
                # print('updated list of self.students', self.students)
                break
        else:
            new = input('does not exist, enter yes or no ?')
            # if new == 'yes':
            #     student['Name'] = input('enter new name : ')
            #     student['Searches'] = 0
            #     self.students.remove(student)
            #     self.students.append(student)

        self.write_to_file()

def call_reader():
    search = input('enter your search')
    stud = Reader(search)
    stud.find()















