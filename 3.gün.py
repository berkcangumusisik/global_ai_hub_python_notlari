myList = [3,5,6,7]
print(myList)
print(type(myList))
print(myList[0])
print(myList[2])
print(myList[-1])
print(myList[-3])

a = 5
print(a)
a = 3
print(a)
myList[2] = "Python"
print(myList)
myList.append("course")
print(myList)
myList = [3,4,5,6,7]
myList.append("course")
myList.append("course")
thelast = myList.pop()
print(thelast)
print(myList)
print(myList.index("course"))
print(myList.index(4))
print(myList.count("course"))
list2 = ["Python","Java","R","JavaScript","Ruby","Python","Python"]
print(list2.count("Python"))

print(myList)
myList.remove("course")
mylist2 = ["python", "course", "hello"]
mylist2.sort()
print(mylist2)
mylist = [2, 3, 4, 5, 6, 'python', 'flutter', 'Android', 'JavaScript', 'dart', 3.2, 5.0]
print(mylist)
mylist.insert(5,55)   # insert(x,y) --> adding x th index the y value but don't change the x th value, it remains the same.
print(mylist)
a = list([1,2,3,4,5,6])
liste1 = list()
numbers = list(range(8))

print(numbers)
print(liste1)
numbers2 = list(range(2,15,3)) #range(start, stop, step)
print(numbers2)
numbers2.reverse()
print(numbers2)
numbers = [0,1,2,3,4,5,6,7,8]
print((numbers[2:5]))
print((numbers[5:8]))
numbers[5:8] = [10,11,12]
print(numbers)
print(12 in numbers)
print(15 in numbers)
x = [1,2,3] + [ 4,5]
print(x)
x = [1,2,3]*3
print(x)
course = "python"

# s = input("Please enter a character: ")

# if s in course:
#     print("Exist!")
# else:
#   print("Don't exist...")

# num = int(input("Please enter a number:"))
# if num<0:
#     num *= -1
# print("Result:",num) 

# score = int(input("Please enter your score: "))

# if score <= 40:
#   print("Very bad, you should work hard..")
# elif score <= 60:
#   print("Nice but you should work more..")
# elif score <= 100:
#   print("Congratulation!")
# else:
#   print("Invalid score!!!")

# x =8
# if x>4:
#     x = x+1
# elif x>5:
#     x = x+2
# elif x>7:
#     x = x+3
# print("x, ",x)
# print("**************ATM Giriş Paneli**************")

# kullanici_adi = "Omer"
# parola ="hello"

# kullanici_adi1 =input("Lütfen kullanıcı adınızı giriniz")

# parola1= input("Lütfen Parolanızı giriniz.")

# if (kullanici_adi != kullanici_adi1 and parola == parola1):
#     print("Kullanıcı adınız hatalı")
# elif (kullanici_adi==kullanici_adi1 and parola!= parola1):
#     print("Parolanız hatalı")
# elif (kullanici_adi != kullanici_adi1 and parola!= parola1):
#     print("Kullanıcı adınız ve parolanız hatalıdır.")
# else:
#     print("Tebrikler, Başarıyla giriş yaptınız")

# x = 5

# if x > 4:
#   x = x+1

# if x > 5:
#   x = x+2

# if x > 7:
#   x = x+3

# print ("x, ", x)
# x = 10
#  if x>5:
#      if x>7:
#          print("İlker and Eylül")
num = 0
while num<9:
    print("Value:{}".format(num))
    num = num+1

# num2 = 0

# while num2 != 9:
#   print("Value:", num2)
#   num2 +=2
