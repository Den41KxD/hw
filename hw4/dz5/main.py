# file = open("file.txt", "w")
# import random
# def zap(f):
#     x = random.randint(2, 10)
#     y = random.randint(3, 20)
#     z = random.randint(30, 50)
#     file.write(str(x) + " " + str(y) + " " + str(z) + "\n")
# def fizzbuzz(x,y,z,count):
#     if not count % x and not count % y:
#         print("FB")
#         f2.write("FB")
#     elif not count % x:
#         print("F")
#         f2.write("F")
#     elif not count % y:
#         print("B")
#         f2.write("B")
#     else:
#         print(count)
#         f2.write(str(count))
#
# list(map(lambda x: zap(x),range(1,21)))
# file.close()
# f=open("file.txt",'r')
# f2=open("result.txt",'w')
#
# for line in f:
#     k=line.split()
#     x=int(k[0])
#     y=int(k[1])
#     z=int(k[2])
#     count = 1
#     while (count <= z):
#         fizzbuzz(x,y,z,count)
#         count += 1
#     f2.write("\n")
# f.close()
# f2.close()


def my_zip(l,min):
    f=[]
    for i in range(len(l)):
        f.append(list(l[i]))
    new_list=[]
    count = 0

    while count<min:
        c = []
        for i in range(len(l)):
            c.append(f[i][count])
        new_list.append(tuple(c))
        c.clear()
        count+=1

    print(new_list)
s='absfdsf'
t=(1,2,34,5)
f=(4,7,9,43,23)
d= 'sockeosl'
print(list(zip(s,t,f,d)))
l=(s,t,f,d)
min=0
for i in range(len(l)):
    if not i:
        min=len(l[i])
    elif len(l[i])<min:
        min=len(l[i])
print(min)
my_zip(l,min)
