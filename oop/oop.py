#single level inheritance

class Animal():
    def eat(self):
        print("All Animals eat food ")

    def sleep(self):
        print("All Animals need sleep")

class Mammal(Animal):

    def run(self):
        print("All mammals can run")


a = Animal()
a.eat()

m = Mammal()
m.sleep()
m.run()


#multi level inheritance

class Grandfather:
    def fair(self):
        print("I am fair")

    def active(self):
        print("I am lazy")

    def social(self):
        print("I am social")

class Father(Grandfather):
    def tall(self):
        print("I am tall")

    def educated(self):
        print("I am educated")

class Me(Father):
    def slim():
        print("I am slim")

me = Me()
me.fair()

#multiple inheritance

class Father:
    def slim(self):
        print("I am slim")

class Mother:
    def active(self):
        print("I am active")

class Child(Father, Mother):
    def educated(self):
        print("I am educated")

ch = Child()
ch.slim()
ch.active()