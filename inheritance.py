class Boy:

    def __init__(self, name,surname):
        self.fname = name
        self.lname = surname

    def printName(self):
        return self.fname + " " + self.lname

class Student(Boy):

    def __init__(self, name,surname,regid):
        Boy.__init__(self,name,surname)
        self.regid = regid

    def printStudentDetails(self):
        return self.printName() + ", " +  self.regid

class Participant(Student):

    def __init__(self, name,surname, regid,event):
        Student.__init__(self,name,surname,regid)
        self.event = event

    def printParticipantDetails(self):
        return self.printStudentDetails() + ", " +  self.event


x = Boy("Akash", "C")
y = Student("Anil", "S", "11308589")
z = Participant("Himanshu", "K", "11300555","One India")

print(x.printName())
print(y.printStudentDetails())
print(z.printParticipantDetails())

class Address:

    def __init__(self, city, state):
        self.city = city
        self.state = state

    def Add(self):
        return self.city + " , " + self.state

class LocationDetails(Boy,Address):

    def __init__(self, name,surname,city, state,country):
        Boy.__init__(self,name, surname)
        Address.__init__(self,city,state)
        self.country = country

    def GetDetails(self):
        return self.printName() + " , " + self.Add() + ", " +  self.country

ob = LocationDetails("pratap","thakur","jalandhar","punjab","india")
print(ob.GetDetails())
