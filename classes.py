class Rectangle:
    def __init__(self, length,breadth):
        self.length=length
        self.breadth=breadth
    def calc(self):
        self.area=self.length*self.breadth
    def display(self):
        print('length: ',self.length, ' breadth: ', self.breadth,' area: ', self.area)

l=int(input('Enter length'))
b=int(input('Enter breadth'))
r=Rectangle(l,b)
r.calc()
r.display() 