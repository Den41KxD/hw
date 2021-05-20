# dct = {'ivanov':90,'Petrov':70,'sidorov':75,'vasya':90,'kolya':60}
# print(dct)
# min=100
# max=0
# for key, val in dct.items():
#     if val>max:
#         max=val
#     if val<min:
#         min=val
#
# for key, val in dct.items():
#     if val==max:
#         print(key,val)
#     if val==min:
#         print(key,val)

# import copy
# def dva(x):
#     for key in x:
#         count=0
#         for values in x[key]:
#             count+=1
#             if count>1:
#                 count=0
#                 print(key,x[key])
#
# def front(x):
#     for key in x:
#         for values in x[key]:
#             if values =='frontend':
#                 print(key,x[key])
#
# def pyga(x):
#     for key in x:
#         for values in x[key]:
#             if values =='python':
#                 for values in x[key]:
#                     if values == 'java':
#                         print(key,x[key])
#
# import random
# dct = 'ivanov','Petrov','sidorov','vasya','kolya','den'
# group = 'java','python','frontend','fullstack','c++','php'
# dct2={}
# for name in dct:
#     k=0
#     i = random.randint(1,3)
#     t=[]
#     copy1 = list(copy.copy(group))
#     while k<i:
#         t.append(copy1.pop(random.randint(0,random.randint(1,len(copy1)-1))-1))
#         k+=1
#     dct2.update({name:t})
# print(dct2)
# dva(dct2)
# print('\n')
# front(dct2)
# print('\n')
# pyga(dct2)

import sys
def new_size(dct,x):
    z={}
    for key,values in dct.items():
        z.update({key:values+x})
    return z

dct={'Rus':42,'Ger':36,'USA':8,'Fr':38,'Br':24}
razm={
    'xxs':new_size(dct,2),
    'xs':new_size(dct,4),
    's':new_size(dct,6),
    'm':new_size(dct,8),
    'l':new_size(dct,10),
    'xl':new_size(dct,12),
    'xxl':new_size(dct,14),
    'xxxl':new_size(dct,16)
}
print("input size of clothes in international:")
while True:
    string=input(str())
    for key in razm.keys():
        if string=='exit':
            sys.exit()
        if key==string:
            print(razm[string])
    print("input other size of clothes in international:")
    print(' or input\"exit\" for exit')



