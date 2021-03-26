import numpy as np 
from matplotlib import pyplot as plt
a = np.array([23,20,22,28,21,25,25,24])

print (a)

print (np.ptp(a))
print (np.percentile(a, 25,))
print (np.percentile(a, 50,))
print (np.percentile(a, 75,))
print (np.percentile(a, 100,))
print (np.median(a))
print (np.mean(a))
print (np.std(a))


x = [20,22,23,28,21,25,24]
y = [1,1,1,1,1,2,1]

plt.bar(x, y, align = 'center')
plt.title("Grafica")
plt.ylabel("Cantidad")
plt.xlabel("Edades")
plt.show()




