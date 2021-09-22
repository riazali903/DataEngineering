import json
import time
from threading import Thread, Lock


class ForgottenMap:

    def __init__(self,name,size):
        self.name = name
        self.size = size
        self.students = []
        self.lock = Lock()

    #@staticmethod
    def read_from_file(self):
        with open('record.json') as f:
            return json.load(f)


    def write_to_file(self):
        # check if this file is engaged ?
        with open('record.json', 'w') as f:
            json.dump(self.students, f, indent=4)

        # else:
        # print('file is engaged...')

    def write(self, input_name, delay_time):
        print(f'Writing {input_name}...')
        if self.lock.locked() is False:
            with self.lock:
                time.sleep(delay_time)
                self.students = self.read_from_file()
                if len(self.students) < self.size:
                    student = {'Name': input_name, 'Searches': int()}
                    self.students.append(student)
                    self.write_to_file()
                else:
                    self.update(input_name)
                print(f'Written {input_name} completed...')
        else:
            print(f'Cannot write {input_name}. lock engaged...')

    def update(self, input_name):
        self.students.sort(key=lambda k: k['Searches'])
        if len(self.students) == 0:
            print('List is empty')
        else:
            for student in self.students:
                if student['Name'] != input_name:
                    self.students.remove(student)
                    add_item = {"Name": input_name, "Searches": 0}
                    self.students.append(add_item)
                    self.write_to_file()
                    print(f'Replaced {student} with {input_name}...')
                    break

    def find(self,search, delay_time):
        print(f'trying to read {search}...')
        if self.lock.locked() is False:
            with self.lock:
                print(f'Reading {search}...')
                time.sleep(delay_time)
                #search = input('find student: ')
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
                    print(f'Name {search} does not exist')
                    self.students.remove(student)
                    add_item = {"Name": search, "Searches": 1}
                    self.students.append(add_item)
                    self.write_to_file()
                    print(f'Replaced {student} with {search}...')

        else:
            print(f'Cannot read {search}. lock engaged...')
            #self.find(search, delay_time)


if __name__ == '__main__':
    size = int(input('what is size?'))
    writer1 = ForgottenMap("instance writer1",size)
    writer1.write()









