f=open("gittext.txt","r")
x=f.readlines()
f2=open("gittext2.txt","w+")
f2.writelines(x)
f2.seek(0,0)
print(f2.readlines())