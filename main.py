class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def show(self):
        print("Name is ", self.name, "and salary is", self.__salary)

#outside class
E = Employee("Bella", 6000)
E.show()
#print(E.PrintName())


#AttributeError: 'Employee' object has no attribute