import json


class writer:

    def __init__(self,name,size):
        self.name = name
        self.size = size
        self.students = []

    def write_to_file(self):
        with open('rooo.json', 'w') as f:
            json.dump(self.students, f, indent=4)

    def main(self):
        student ={}
        while len(self.students) < self.size:
            student = {'Name': input('enter name : '), 'Searches': int()}
            self.students.append(student)

        new =input('list full,add new, enter yes or no ?')
        if new == 'yes':
            student['Name'] = input('enter new name : ')
            self.students.remove(student)
            self.students.append(student)
            print('new appended:',self.students)
        self.write_to_file()

# a = writer()
# a.main()


size = int(input('what is size?'))
writer1 = writer("instance writer1",size)
writer1.main()




