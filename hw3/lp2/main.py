# pz1

# l = [1,2,3,4,5,6,7,8,9,10]
# sum=0
# for i in l:
#     sum +=i
# print(sum)
# sum=0
# leng=len(l)
# count=0
# while count < leng:
#     sum+=l[count]
#     count+=1
# print(sum)

# pz2+3

# import sys
# filename=sys.argv[0]
# f=open(filename,'r')
# for line in f:
#     print(line)
# f.close()
#
# f=open(filename).readlines()
# for line in reversed(f):
#     print(line)

# pz4
# import sys
# bank = [10,20,50,100,200,500,1000]
# l=int(input())
# if l%10:
#     print("Error!! enter another amount")
#     sys.exit()
# x=len(bank)
# count=0
# while l>0:
#     if l-bank[x-1]<0:
#         print(str(count) + " kypyr po " + str(bank[x-1]))
#         x-=1
#         count=0
#     else:
#         l-=bank[x-1]
#         count+=1
#         if l==0:
#             print(str(count) + " kypyr po " + str(bank[x - 1]))
#

# pz5

bank = [10, 20, 50, 100, 200, 500, 1000]
kolvo = []
max = 0

for c in bank:
    max += c * 10
l = max+1
print("enter amount")
while l>max or l%10:
    l = int(input())
    if l>max or l%10 :
        print("Error!! enter another amount")
count = i = 0
while l > 0:
    l -= bank[i]
    count += 1
    print(l)
    if l - bank[i] < 0 and l:
        l += bank[i] + bank[i - 1]
        count -= 1
        kolvo[i - 1] -= 1
    if count > 9 and l:
        kolvo.insert(i, count)
        i += 1
        count = 0
    if not l:
        kolvo.insert(i, count)
        print("end")
i = 0
f=len(kolvo)
while i<f:
    print(str(kolvo[i]) + " kypyr po " + str(bank[i]))
    i += 1
