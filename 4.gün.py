# num3 = int(input("Please enter an integer between 1 and 10: "))

# while num3 < 1 or num3 > 10:  
#     print("Invalid value!!!!")
#     sayi3 = int(input("Please enter an integer between 1 and 10: "))
# print("Congrats...") 

# t = [1,2,3,4,5,6]
# i = 0
# while (i< len(t)):
#     print(i,"th item", t[i])
#     i += 1
# while True:
#   a = input("Enter a value: ")
#   if a == "Exit":
#     break
# for i in [2,45,57]:
#     print(i)
# for i in range(5):
#     print(i)
# for i in "Python course":
#     print(i)
# for i in "Python course".split():
#     print(i)
# for i in range(10):
#     if i ==5:
#         break
#     print(i)
# for i in range(10):
#     if i == 5:
#         continue
#     print(i)
# nums = list(range(8))
# squares = []
# for i in nums:
#     squares.append(i**2)
# print(squares)
# nums = list(range(8))
# squares = [i**2 for i in nums]
# print(squares)

# nums = list(range(8))

# even_squares = [i**2 for i in nums if i % 2 == 0]

# odd_squares = [i**3 for i in nums if i% 2 == 1]

# print(even_squares)
# print(odd_squares)

# mylist = [3,5,12,7,65,35]

# sum = 0

#   sum = sum + i    #sum += i
#   print(sum)
# print(sum)

# mylist = [3, 5, 12, 7, 65, 35]
# print(mylist[0])
# max1 = mylist[0]
# for i in mylist:
#     max1 = i
#     print("max1: ", max1)
#     print("i", i)
# print(max1)

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# list3 = [a+b for a,b in zip(list1, list2)]
# print(list3)
# import random as rnd

# secret = rnd.randint(1,100)

# check = False

# #guess = int(input("Please enter you guess: "))

# for x in range(5):
#   guess = int(input("Please enter you guess: "))
#   if guess == secret:
#     print("Congrats!!")
#     check = True
#     break
#   elif guess < secret:
#     print("Please enter a greater number!!")
#   else: 
#     print("Please enter a smaller number!!")
    
# if not check:
#   print("Looseer..The number was: ", secret)
d = {}
print(d)
d = {"python":1, "course":2}
print(d)
d2 = {"machine":"learning", "artificial":"intelligence" }
print(d2)
d2["deep"] = "learning"
print(d2)
print(d2.keys)
for v in d.values():
  print(v)
for v in d2.values():
  print(v)
print(d2.values)
for k,v in d2.items():
    print(k,v)
