import json
from threading import Thread
import time

class Reader:
    def __init__(self):
        self.students = []

    def read_from_file(self):
        with open('record.json') as f:
            record = json.load(f)
            return record

    def write_to_file(self):
        with open('record.json', 'w') as f:
            json.dump(self.students, f, indent=4)

    def find(self):
        while True:
            search = input('find student: ')
            self.students = self.read_from_file()
            for student in self.students:
                if student['Name'] == search:
                    print(f'{search} exists. Total items {len(self.students)}')
                    count = student['Searches']
                    self.students.remove(student)
                    # contain = True
                    update_item = { "Name": search,"Searches": count + 1}
                    self.students.append(update_item)
                    self.write_to_file()
                    break
            else:
                print('Name does not exist')



if __name__ == '__main__':
    stud = Reader()
    stud.find()















