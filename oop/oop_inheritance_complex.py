class Calculation1:
    def summation(self,a,b):
        return a+b

class Calculation2:
    def multiplication(self,a,b):
        return a*b

class Derived(Calculation1, Calculation2):
    def division(self,a,b):
        return a/b

d = Derived()
print(d.summation(10,20))
print(d.multiplication(10,20))
print(d.division(10,20))



if isinstance(d,Derived):
    print("d is instance of Derived")
elif isinstance(d,Calculation2):
    print("d is instance of Calculation2")
elif isinstance(d, Calculation1):
    print("d is instance of Calculation1")
else:
    print("d is not a instance")