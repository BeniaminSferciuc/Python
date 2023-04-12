import matplotlib.pyplot as plt
import numpy as np

# xpoints = np.array([3, 8, 1, 10])
# ypoints = np.random.permutation(np.arange(0, 4))
#
# font1 = {'family':'serif','color':'blue','size':20}
# font2 = {'family':'serif','color':'darkred','size':15}
#
# plt.plot(xpoints, marker='o', ms=20, lw=10, mec='r', mfc='b', linestyle='solid', color='r')
# plt.plot(ypoints)
#
# plt.xlabel("Average Pulse", fontdict=font2)
# plt.ylabel("Calorie Burnage")
# plt.title("Sports Watch Data", fontdict=font1, loc='left')
# plt.grid(axis='both', color='g', ls=':', lw = 1)
# plt.show()
#
#
# #plot 1:
# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])
#
# plt.subplot(1, 2, 1)
# plt.plot(x,y)
# plt.title('Income')
#
# #plot 2:
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])
#
# plt.subplot(1, 2, 2)
# plt.plot(x,y)
# plt.suptitle('My Shop')
# plt.show()
#
# x = np.random.randint(100, size=100)
# y = np.random.randint(100, size=100)
# colors = np.random.randint(100, size=100)
#
# plt.scatter(x, y, c=colors, cmap='OrRd', alpha=0.5)
# plt.colorbar()
# plt.show()
#
# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])
#
# plt.bar(x, y, width=0.5, color='orange')
# plt.show()

y = np.array([25, 10, 15, 50])
name = ['Python', 'HTML', 'CSS', 'JS']
col = ['Green', 'red', 'Blue', 'Orange']
myexplode= [0, 0.2, 0, 0]
plt.pie(y, labels=name, colors=col, shadow=True, startangle=270, explode=myexplode)
plt.legend(title='Learn every day', loc='upper left')
plt.show()
