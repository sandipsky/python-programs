class Person(object):
    #constructor
    def __init__(self,name):
        self.name = name

    #To get name
    def getName(self):
        return self.name

    def isEmployee(self):
        return False

class Employee(Person):
    def isEmployee(self):
        return True

#creating objects

emp = Person("Sarup")
print(emp.getName(), emp.isEmployee())
emp1 = Employee("Sandip")
print(emp1.getName(), emp1.isEmployee())
