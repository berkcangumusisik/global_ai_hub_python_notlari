d = {'python': 1, 'course': 2}
d["a"] = [3,4,5]
print(d)
print(d.pop("python"))
print(len(d))
print("a" in d)
print("aa" in d)
d2= {'machine': 'learning',
 'artificial': 'intelligence',
 'java': 'programming',
 'ruby': 'language',
 'deep': 'learning'}
print(d2.get("artificial"))
d4 = {"human":2,
      "cat":4,
      "spider":8
     }

for i in d4:
  leg = d4[i]
  print("%s has %d legs " % (i,leg))
  print(str(i) + " has " + str(leg) +" legs.")
for i,leg in d4.items():
  print(str(i) + " has " + str(leg) +" legs.")
districts = {"İstanbul":["Bostancı", "Beşiktaş", "Kadıköy"], 
           "Ankara":["Çankaya", "Gölbaşı", "Kızılcahamam"],
           "İzmir":["Çeşme","Bornova","Foça"]}
print(districts["İstanbul"])
print(type(districts))
print(type(districts["Ankara"]))
print(districts["İzmir"][0])
print(districts["İzmir"][2])
nums = list(range(9))

even_sqr = {x: x**2 for x in nums if x % 2 == 0}
print(even_sqr)

s = {"python", 5,6,8,5,6,"abc", "python","python","python","python","python","python","python","python","python"}
print(s)
empty = set()
print(type(empty))
empty = { }
print(type(empty))
s2 = set(["python", 5,6,8,5,6,"abc", "python"])
print(s2)
ne = set("pineapple")
print(ne)
print(6 in s2)
print(9 in s2)
print(len(s2))
s2.add("ai")
print(s2)
from math import sqrt
print({x for x in list(range(10))})
print({sqrt(x) for x in list(range(10))})
tupl = (1,2,3,4,5)
print(tupl)
print(type(tupl))
print(tupl[3])
print(tupl[-2])
print([tupl[:4]])
dm3 = ("asli", 5, 8, "september")
print(dm3.index("september"))
print(dm3.count(5))
# dm4 = ("apple","pear","strawberry")

# dm4[0] = "cherry"

# print(dm4)
a = {(x, x+1): x for x in range(10)}
print(a)
s5 = (5,6)
print(a[s5])
print(a[(3,4)])
# def hello():
#   print("Hello Everyone!!")
# hello()

def hello(name):
    print("Hello" + name)
hello(" Berkcan") 

def func_in_func(name1):
    return hello(name1)
func_in_func("  Ugurcan")

def func1():
  print("Hello World!!")


func1()
print("Google")
func1()
func1()
func1()
func1()

def summ(a,b):
    summ = a+b
    print(summ)
summ(6.0,7.5)
t = summ(8,9)
t

def func(x,y):
  summ = x + y
  multip = x * y
  return (summ,multip)
t,c = func(23,45)
print(t,c)
func(23,45)
print("Sum of the values: " + str(t) + ", Multiplying of the values: " + str(c))
def sqr(x):
  if x == 5:
    return ("Terminated because you entered 5")

  result = x **2
  return (result)
print(sqr(10))
print(sqr(5))
d = sqr(5)
print(d)
def func(x):
  if x > 0:
    return ("Positive")
  elif x < 0:
    return ("Negative")
  else:
    return ("Zero")
for i in [-2,5,6,0,-4,-7]:
  print(func(i))
def factorial(num):
  factorial = 1
  if (num == 0 or num == 1):
    print("Factorial: ", factorial)
  else:
    while (num >= 1):
      factorial = factorial * num
      num -= 1
    print("Factorial: ", factorial)
factorial(5)

def faktoriyel(sayi):
  faktoriyel = 1
  for i in range(1,sayi+1):
    faktoriyel *= i
  return faktoriyel
faktoriyel(5)

def factorial2(num2):
  factorial2 = 1
  if (num2 == 0 or num2 == 1):
    print("Factorial: ", factorial2)
  else:
    for i in range(factorial2, num2+1):    
       factorial2 *= i      
    print("Factorial: ", factorial2)
factorial2(6)
x = factorial2(6)
print(x)
def factorial3(nums):
  factorial3 = 1
  if (nums == 0 or nums == 1):
    return ("Factorial: ", factorial3)
  else:
    for i in range(factorial3, nums+1):
       factorial3 *= i      
    return ("Factorial: ", factorial3)
x = factorial2(3)
print(x)
def hello2(name, capLetter= False ):
    if capLetter:
        print("Hello" + name.upper())
    else:
        print("Hello " + name)
hello2("Asli")
hello2(" Asli", capLetter=True)
def multp(*args):
  result = 1
  for i in args:
    result *= i
  print(result) 
multp(4,5,6,7,8)
multp(2,3,4,5)
