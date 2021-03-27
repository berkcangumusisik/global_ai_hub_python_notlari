def salaryCalc(salary):

  if salary < 0:
    print("Invalid value")
  else:

    if 0 < salary <= 1000:
      salary = salary + salary * 0.15
    elif salary <= 2000:
      salary = salary + salary * 0.1
    elif salary <= 3000:
      salary = salary + salary * 0.05
    else:
      salary = salary + salary * 0.025

    print("New salary: ", salary)

salaryCalc(-5)
salaryCalc(800)

# def salaryCalc2():

#   print = float(input("Please enter your current salary: "))

#   if salary < 0:
#     print("Invalid value")
#   else:
#     if 0 < salary <= 1000:
#       salary = salary + salary * 0.15
#     elif salary <= 2000:
#       salary = salary + salary * 0.1
#     elif salary <= 3000:
#       salary = salary + salary * 0.05
#     else:
#       salary = salary + salary * 0.025

#     print ("New salary: ", salary)
 
# new_salary = salaryCalc2()
# print(new_salary)
# rnd = ["artificial","intelligence","machine","learning","python","programming"]
# import random as rnd
# def randomWord(words):
#   index = rnd.randint(0, len(words)-1)
#   return words[index]
# word = randomWord(words)
# print(word)
# 
# def display():
#   x = 4
#   return(x)
# display
# 
# 
# 
# s = input("Please enter a name: ")

# upper = s.capitalize()

# print(upper)
myList = [45,7,23,6,12,78]

maxElement = max(myList)

maxIndex = myList.index(maxElement)

print(maxIndex)

# print "Hello World"
# num1 = input("1.sayı: ")
# num2 = input("2.sayı: ")
# print(num1 ,"+", num2, "=", num1 + num2)

# num3 = int(input("First integer: "))
# num4 = int(input("Second integer: "))

# print(num3, "/",num4, "=", num3/num4)
num3 = input("First integer: ")
num4 = input("Second integer: ")

try:
  num3_int = int(num3)
  num4_int = int(num4)

  print(num3_int, "/",num4_int, "=", num3_int/num4_int)

except (ValueError, ZeroDivisionError):
  print("Error!!!")
num3 = input("First integer: ")
num4 = input("Second integer: ")

try:
  num3_int = int(num3)
  num4_int = int(num4)

  print(num3_int, "/",num4_int, "=", num3_int/num4_int)

except ValueError:
  print("Please enter an integer value!!!")
except ZeroDivisionError:
  print("Please enter the second input different than 0 value!!!")
except:
  print("Unknown error...")
  while True:
    num1 = input("First number: (Press q for quit the program): ")

    if num1 == "q":
        break

    num2 = input("Second number: ")

    try:
        num1_int = int(num1)
        num2_int = int(num2)
        print(num1_int, "/", num2_int, "=", num1_int / num2_int)
    except (ValueError, ZeroDivisionError):
        print("Error!")
        print("Please try again!")

class car():
    colour = "yellow"
    brand = "xyz"
    door = 4
    model = 1987
print(car.model)
print(car.brand)
print(car.door)
print(car.colour)
car2 = car()
print(car2.colour)
print(car.brand)
print(dir(car))
class Car3():

  def __init__(self, colour, brand, door):
    self.colour = colour
    self.brand = brand
    self.door = door


red_car = Car3("red", "abc",2)

yellow_car = Car3("yellow", "xyz", 4)

print(red_car.colour)
print(yellow_car.brand)
blue_car = Car3("blue","bnm",10)

print(blue_car.brand)
print(blue_car.colour)
print(blue_car.door)
class Person():
  name = ""
  age = 0

  def __init__(self, personName, personAge):
    self.name = personName
    self.age = personAge


  def welcomePerson(self):
    print("Hello " + self.name)

  
  def showAge(self):
    print(self.age)
person1 = Person ("Asli", 28)

person1.welcomePerson()
person1.showAge()