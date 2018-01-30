
list=[]
for n in range(10):
    list.append(n)
print(list)

name="Hi This is Akash"
for i in name:
    print(i,end=' ')

for n in range(10):
    if n==6:
        break
    print(n,end=',')

for n in range(10):
    if n%2==0:
        continue
    print(n,end=',')
