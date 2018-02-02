m=int(input('Enter number 1 '))
n=int(input('Enter number 2 '))
print('Enter 1 for Adding.. ')
print('Enter 2 for Substraction.. ')
print('Enter 3 for Multiplication.. ')
print('Enter 4 for Division.. ')
c=int(input('Enter choice..  '))
if c==1:
    result=m+n
elif c==2:
    result=m-n
elif c==3:
    result=m*n
elif c==4:
    result=m/n
else:
    print('invalid choice')
print('answer: '+str(result))