
import numpy as np
a = np.array([1, 2, 3, 4, 5 ])
print(type(a))
print(a.ndim)
print(a[0])
print(a[3])
print(a[2])
a[2] = 8
print(a)
b = np.array([[1,2,3,4],[5,6,7,8]])   
print(b.ndim)
print(b.shape)
print(b[0,0])
print(b[1,0])
print(b[1,1])
print(b[0,0],b[1,0], b[1,1])
c = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(c.ndim)          
print(c.shape)
d = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(d.ndim)          
print(d.shape)
s = np.zeros((2,2))
print(s)
s2 = np.ones((2,3)).astype("int64").dtype

print(s2)
s3 = np.full((3,3),8)

print(s3)
s4 = np.empty((4,5))

print(s4)
s5 = np.eye(4)

print(s5)
s6 = np.random.random((5,5))      

print(s6)

s7 = np.arange(0,10,1)
print(s7)
s8 = np.linspace(2,3,5)
print(s8)
array_random = np.random.randint(5,10, size = 10)
array_random.shape 
d2 = np.random.randint(5,10, size = (5,3))

print(d2)

print(d2.shape)
print(d2.reshape(3,5))
print(d2.reshape(15,1))
d3 =  np.random.randint(5,10, size = (5,3))

print(d3)
d3 = d3.ravel()

print(d3)
print(d3.shape)
print(d3.astype("int64").dtype)
d3 = d3.reshape(3,5)
print(d3)
d3.max
d3.min
print(d3[::-1])
news = np.random.randint(1,100,10)

print(news)
print(type(news))
print(news.ndim)
print(news.shape)
print(news.argmax())
print(news.argmin())
print(news.mean())
a = np.array([[1,2,3],[4,5,6]])

b = np.array([[6,5,4], [3,2,1]])
print(np.vstack((a,b)))
print(np.hstack((a,b)))
myArray = np.array([0,1,2,3,4,5,6,7,8,9]).reshape(5,2)

print(myArray)
print(np.concatenate([myArray,myArray], axis = 0))  #vertical 
print(np.concatenate([myArray,myArray], axis = 1)) #horizontal
a = np.array([[1,2,3,4],
              [5,6,7,8],
              [9,10,11,12]])

b = a[:2, 1:3]    

print(b)
print(a[0,1])
b[0,0] = 77    

print(a[0,1])
line1 = a[1,:]    
line2 = a[1:2, :]  
line3 = a[[1],:]    
print(line1, line1.shape)
print(line2, line2.shape)
print(line3, line3.shape)
col1 = a[:,1]
col2 = a[:, 1:2]

print(col1, col1.shape)
print(col2, col2.shape)
t = np.array([[1,2],
              [3,4],
              [5,6]])

print(t[[0,1,2],[0,1,0]]) 
print(np.array([t[0,0], t[1,1], t[2,0]]))
s = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])

print(s)
print(s[np.arange(4), indis]) #([0,1,2,3],[0,2,0,1]) 
x = np.array([[1,2],[3,4]], dtype= np.float64)
y = np.array([[5,6],[7,8]], dtype= np.float64)


print(x+y)

print(np.add(x,y))
print(x-y)

print(np.subtract(x,y))
print(x*y)

print(np.subtract(x,y))
print(np.dot(x,y))
print(x/y)

print(np.divide(x,y))
s = np.array([[4,9],[16,81]], dtype = np.float64)

print(np.square(s))
s = np.array([[4,9],[16,81]], dtype = np.float64)

print(np.exp(s))
v = np.array([10,100,1000,10000,100000,1000000])

print(np.log(v))
x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])

a = np.array([9,10])
b = np.array([11,12])


print(a.dot(b))

print(np.dot(a,b))
print(x.dot(a))

print(np.dot(a,x))
print(y.dot(b))

print(np.dot(y,b))
x = np.array([[1,2],[3,4]])

print(np.sum(x))

print(np.sum(x, axis = 0))

print(np.sum(x, axis = 1))