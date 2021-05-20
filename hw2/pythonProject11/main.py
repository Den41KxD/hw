# -*- coding: utf-8 -*-
# initializing empty envelops
# i = int(input())
# if (not i and i%2):
#     print("true")
#
# else:
#     print("false")
# i = int(input())
# if(i%2 and not i%3 and not i%5 and i%10):
#     print("da")
# else:
#     print ("no")
# i = int(input())
# t=1
#
# while(t<i/2):
#     if not i%t:
#          print(t)
#     t+=1
#
i=int(input())
t=1
count =0
while((t<i)):
    t *= 10
    if t==10:
        print(i%t)
    else:
        print((i % t)//(t/10))
    count+=1
print ("разрядов: " + str(int(count)))
k=2
l=0
m=0
while(i>1):

    if(i%k==0):
        l=i/k
        m += 1
        print("множитль" + str(int(m)) + " = " + str(int(k)))
        k=2
        i = l
    else: k+=1
    if(i==1):print("множитль" + str(int(m+1)) + " = " + str(int(1)))