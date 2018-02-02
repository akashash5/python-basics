def printlist(list1):
    for i in list1:
        print(i)

def printdict(dict1):
    for i,j in dict1.items():
        print(str(i)+" : "+str(j))

list2=[1,2,3,'Akash']
printlist(list2)

set1={'Akash','Anil','Himanshu','Kenei'}
printlist(set1)

tup=1,2,3,4,5
printlist(tup)

dict1={'Name':'Akash','Age':22}
printdict(dict1)
