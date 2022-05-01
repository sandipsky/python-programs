
class Person(object):
    #constructor
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def display(self):
        print(self.name)
        print(self.id)

class Employee(Person):
    def __init__(self,name,id,salary,post):
        self.salary = salary
        self.post = post

    #invoking the __init__of parent class
        Person.__init__(self,name,id)

    def display(self):
        Person.display(self)
        print(self.salary)
        print(self.post)

#creation of object
a = Employee('Sandip', 1, 20000, "Intern")

a.display()