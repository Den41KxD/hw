file = open("file.txt", "w")
import random
count=0
while count<20:
    x = random.randint(2, 10)
    y = random.randint(3, 20)
    z = random.randint(30, 50)
    file.write(str(x) + " " +str(y) + " " + str(z) + "\n")
    count+=1
file.close()
f=open("file.txt",'r')
f2=open("result.txt",'w')

for line in f:
    k=line.split()
    x=int(k[0])
    y=int(k[1])
    z=int(k[2])
    count = 1
    while (count <= z):
        if not count % x and not count % y:
            print("FB")
            f2.write("FB")
        elif not count % x:
            print("F")
            f2.write("F")
        elif not count % y:
            print("B")
            f2.write("B")
        else:
            print(count)
            f2.write(str(count))
        count += 1
    f2.write("\n")
f.close()
f2.close()


