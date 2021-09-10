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
        while True:
            input_name = input('enter name: ')
            self.students = self.read_from_file()
            if len(self.students) <= self.size:
                student = {'Name': input_name, 'Searches': int()}
                self.students.append(student)
                self.write_to_file(self.students)
            else:
                self.update(input_name)

    def update(self, input_name):
        self.students.sort(key=lambda k: k['Searches'])
        print('update this', self.students)
        if len(self.students) == 0:
            print('List is empty')
        else:
            #add_new = input('please add new')
            for student in self.students:
                if student['Name'] != input_name:
                    self.students.remove(student)
                    add_item = {"Name": input_name, "Searches": 0}
                    self.students.append(add_item)
                    self.write_to_file(self.students)
                    break



if __name__ == '__main__':
    while True:
        size = int(input('what is size?'))
        writer1 = Writer("instance writer1",size)
        writer1.main()










