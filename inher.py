class Person:

    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def Name(self):
        return self.firstname + " " + self.lastname

class Employee(Person):

    def __init__(self, first, last, staffnum):
        Person.__init__(self,first, last)
        self.staffnumber = staffnum

    def GetEmployee(self):
        return self.Name() + ", " +  self.staffnumber

class Manager(Employee):

    def __init__(self, first, last, staffnum,dept):
        Employee.__init__(self,first, last,staffnum)
        self.dept = dept

    def GetManager(self):
        return self.GetEmployee() + ", " +  self.dept


x = Person("Akash", "C")
y = Employee("Anil", "S", "2018")
z = Manager("Himanshu", "K", "1131","SCA")

print(x.Name())
print(y.GetEmployee())
print(z.GetManager())

class Address:

    def __init__(self, city, state):
        self.city = city
        self.state = state

    def Add(self):
        return self.city + " , " + self.state

class PersonDetails(Person,Address):

    def __init__(self, first, last,city, state,country):
        Person.__init__(self,first, last)
        Address.__init__(self,city,state)
        self.country = country
    # def Add(self):
    #     return 'overriding function'

    def GetDetails(self):
        return self.Name() + " , " + self.Add() + ", " +  self.country

ob = PersonDetails("pratap","thakur","jalandhar","punjab","india")
print(ob.GetDetails())
