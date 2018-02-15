import numpy as np
import matplotlib.pyplot as plt
n=10000
x= np.random.uniform(low=50.0, high=100.0, size=(n,))
y= np.random.uniform(low=50.0, high=100.0, size=(n,))
fig, ax = plt.subplots()
diff=x-y
dmed=np.median(diff)
dmax=max(diff)
dmin=min(diff)
dsplit=(abs(dmax)-abs(dmin))%11
colorbar=[]
colorbar.append([1.0,0.0,0.0,0.9])
colorbar.append([1.0,0.2,0.0,0.8])
colorbar.append([1.0,0.4,0.0,0.7])
colorbar.append([1.0,0.5,0.0,0.6])
colorbar.append([1.0,0.7,0.0,0.5])
colorbar.append([1.0,1.0,0.0,0.4])
colorbar.append([0.7,1.0,0.0,0.5])
colorbar.append([0.5,1.0,0.0,0.6])
colorbar.append([0.4,1.0,0.0,0.7])
colorbar.append([0.2,1.0,0.0,0.8])
colorbar.append([0.0,1.0,0.0,0.9])

colors = []
for i in diff:
    if i<=dmin+dsplit:
        colors.append(colorbar[0])
    elif i<=dmin+dsplit*2:
        colors.append(colorbar[1])
    elif i<=dmin+dsplit*3:
        colors.append(colorbar[2])
    elif i<=dmin+dsplit*4:
        colors.append(colorbar[3])
    elif i<=dmin+dsplit*5:
        colors.append(colorbar[4])
    elif i<=dmin+dsplit*6:
        colors.append(colorbar[5])
    elif i<=dmin+dsplit*7:
        colors.append(colorbar[6])
    elif i<=dmin+dsplit*8:
        colors.append(colorbar[7])
    elif i<=dmin+dsplit*9:
        colors.append(colorbar[8])
    elif i<=dmin+dsplit*10:
        colors.append(colorbar[9])
    elif i<=dmin+dsplit*11:
        colors.append(colorbar[10])


#print(colors)
ax.scatter(x,y, c=colors, s=abs(diff)**2)

ax.set_ylabel('Qualifying percent', fontsize=15)
ax.set_xlabel('Present percentage', fontsize=15)
ax.set_title('%P versus %Q')

ax.grid(True)
fig.tight_layout()

plt.show()
