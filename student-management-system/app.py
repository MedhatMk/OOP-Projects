#Creat Student class
class Student:
    #init method or constructor
    def __init__(self, name, rollno, branch, year):
        self.name = name
        self.rollno = rollno
        self.branch = branch
        self.year = year
    #Create method
    def create(self):
        #open file in append mode
        with open('student.txt', 'a') as f:
            f.write(self.name + ',' + self.rollno + ',' + self.branch + ',' + self.year )
    #Read method
    def read(self):
        #open file in read mode
        with open('student.txt', 'r') as f:
            for line in f:
                #print all lines in the file
                print(line, end='')
    #Update method
    def update(self, name, rollno):
        #initialize flag as false
        flag = False
        #open file in read mode
        with open('student.txt', 'r') as f:
            #read all lines in the file
            data = f.readlines()
        #open file in write mode
        with open('student.txt', 'w') as f:
            for line in data:
                #split the data
                word = line.split(',')
                #if name and rollno matches
                if word[0] == name and word[1] == rollno:
                    #update the record
                    f.write(self.name + ',' + self.rollno + ',' + self.branch + ',' + self.year )
                    flag = True
                else:
                    #else write the old data
                    f.write(line)
        #if flag is false
        if flag == False:
            print('Record not found')
    #Delete method
    def delete(self, name, rollno):
        #initialize flag as false
        flag = False
        #open file in read mode
        with open('student.txt', 'r') as f:
            #read all lines in the file
            data = f.readlines()
        #open file in write mode
        with open('student.txt', 'w') as f:
            for line in data:
                #split the data
                word = line.split(',')
                #if name and rollno matches
                if word[0] == name and word[1] == rollno:
                    flag = True
                else:
                    #else write the old data
                    f.write(line)
        #if flag is false
        if flag == False:
            print('Record not found')
#main method
def main():
    #infinite loop
    while True:
        #display menu
        print('1. Create Student Record')
        print('2. Read Student Record')
        print('3. Update Student Record')
        print('4. Delete Student Record')
        print('5. Exit')
        #take choice from the user
        choice = input('Enter your choice: ')
        #check choice is one of the five options
        if choice in ('1', '2', '3', '4', '5'):
            #create object of Student class
            student = Student(input('Enter name: '), input('Enter rollno: '), input('Enter branch: '), input('Enter year: '))
            #if choice is one
            if choice == '1':
                #call create method
                student.create()
            #if choice is two
            elif choice == '2':
                #call read method
                student.read()
            #if choice is three
            elif choice == '3':
                #call update method
                student.update(input('Enter name: '), input('Enter rollno: '))
            #if choice is four
            elif choice == '4':
                #call delete method
                student.delete(input('Enter name: '), input('Enter rollno: '))
            #if choice is five
            elif choice == '5':
                #exit from the program
                exit()
        else:
            print('Invalid Input')
#call the main method
if __name__ == '__main__':
    main()
        
    