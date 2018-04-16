F1=open("gittext.txt","w")
import json
x=[1,2,3,4]
print(json.dumps(x))
json.dump(x,F1)
F1.close()
F1=open("gittext.txt","r")
y=json.load(F1)
print(y)

