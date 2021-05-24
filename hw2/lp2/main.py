#первое задание
# print("Hello")
# # i=int(input())
# i=45
# if i>=100:
#     print("меньше или равно 100")
# elif((i>10) and (i<100)):
#     print("между 10 и 100")
# else:
#     print("мало")
# if(i>1000):
#     print("много")
#
#
# x=5
# z=15
# result = (x<i) and (i<=z)
# if result:
#     print("true")
# else :
#     print("false")
#
# l1 = [1, 2, 3]
# l2 = [1, 2, 3]
#
# if l1==l2:
#     print("true")
# else:
#     print("False")
#
#
# if l1 is l2:
#     print("true")
# else:
#     print("False")
#
# if 3 in l1:
#     print("true")
# else:
#     print("False")
#
# if 5 not in l1:
#     print("true")
# else:
#     print("False")
#
# test = False
# print ('ttt' if test else 'fff')

#Буль

# print(" fizz= ")
# x=int(input())
# print(" buzz= ")
# y=int(input())
# print(" z= ")
# z=int(input())
#
#
# count=1
# while(count<=z):
#
#     if not count%x and not count%y:
#         print("FB")
#     elif not count%x:
#         print("F")
#     elif not count%y:
#         print("B")
#     else:
#         print(count)
#     count+=1

#задание 2


print("угадай число")
import random
x = random.randint(1,100)
print("x=",x)
k=0
count=0
while(k!=x):
    print("введи число которое загадано:")
    k=int(input())
    i=x-k
    if k==x:
        print("угадал ")
        print("попыток:" + str(int(count)))
    elif i>=20 or i<=-20:
        print("очень далеко")
    elif 20>=i>=10 or -20 <= i <= -10:
        print("близко,попробуй ещё")
    elif 10>=i >=1:
        print("очень рядом,попробуй больше")
    elif -10 <= i <= -1:
        print("очень рядом, попробуй меньше")
    count+=1
