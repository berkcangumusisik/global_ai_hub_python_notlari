t , f = True , False
print(t)
print(f)
print(t or f)
print(t and f)
print(not t)
print(t != f)
print(t ==f)
hello = "Hello"
world = "World"
print(hello)
print(len(hello))
print(world+  str(len(world)) + "Hello")
world2 = "%s %d" % (world, len(world))
print(world + str(len(world)))
print(world+ " " + str(len(world)))
print(str("Python"))
print(type(str(5)))
print(type(float(5)))
print(float(5))
print(int(5.5))
hello = "Hello"
print(hello)
print(hello[0])
print(hello[1])
print(hello[2])
print(hello[3])
print(hello[4])
world = "World"
print(world)
print(world[-1])
print(world[-3])
print(world[-5])
# print(world[-7])
hello = "Hello"
print(hello[2:4])
print(hello[:])
print(hello[:4])
print(hello[::-1])
world = "World"
print(world[1:4])
print(world[3:5])
print(world[3:])
print(hello[2:len(world)])
print(world[2:4:1])
city = "istanbul"
print(city[0:6:2])
print("t" in city)
print("y" in city)
print("anb" in city)
print("snl" in city)
n = 10
print(str(n))
s = 13
print(int(s))
# s = "ist"
# print(int(s))
m = 8
print(float(m))
ai = "artifical" + " " + "intellegence"
print(ai)
word = "machine learning"
print(word.capitalize())
print(word.upper())
print(word.replace("machine","artifical"))
word2 = "          artificial general      intelligence"
print(word2.strip())
y = input("Please enter a city name: ")  #input method always takes string type. 
print(y)
x = int(input("Please enter an integer:"))
print(x)
month = 12
day = 365

print('One year is ', month, 'months, and ', day, 'days.', sep =' ')
print('One year is  ', month, ' months, and  ', day, ' days.', sep ='')

print("One year is " + str(month) + " months, and " + str(day) + " days.")
