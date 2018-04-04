class Car:
    def __init__(self, color,price):
        self.color=color
        self.price=price
    
    def display(self):
        print('color: ',self.color, ' price: ', self.price)

l=str(input('Enter color'))
b=str(input('Enter price'))
r=Car(l,b)
r.display() 