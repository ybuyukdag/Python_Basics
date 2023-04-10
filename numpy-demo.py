import numpy as np

list = [10,15,30,45,60]

n_array = np.array([10,15,30,45,60])

n_array = np.arange(5,15)

n_array = np.arange(50,100,5)

n_array = np.zeros(10)

n_array = np.ones(10)

n_array = np.linspace(0,100,5)

n_array = np.random.randint(10,30,5)

n_array = np.random.rand(10)

mn_array = np.random.randint(-50,50,15).reshape(3,5)

# print(mn_array)
# print(mn_array.sum(axis=1))
# print(mn_array.sum(axis=0))
# print(mn_array.min())
# print(mn_array.max())
# print(mn_array.mean())
#print(mn_array.argmax())
n_array = np.arange(10,20)

#print(n_array[0:3])
#print(n_array[::-1])
#print(n_array)
print(mn_array)
#print(mn_array[0])
#print(mn_array[2,3])
#print(mn_array[:,0])
#print(np.square(mn_array))
print(mn_array % 2 == 0)