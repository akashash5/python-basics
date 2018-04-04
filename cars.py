class Car:
    def __init__(self, color,price):
        self.color=color
        self.price=price
    
    def display(self):
        print('color: ',self.color, ' price: ', self.price)

c=str(input('Enter color'))
p=str(input('Enter price'))
r=Car(c,p)
r.display() 