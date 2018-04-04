class Rectangle:
    def __init__(self, length,breadth):
        self.length=length
        self.breadth=breadth
    def calc(self):
        self.area=self.length*self.breadth
    def display(self):
        print(self.length, ' ', self.breadth,' ', self.area)

r=Rectangle(10,20)
r.calc()
r.display() 