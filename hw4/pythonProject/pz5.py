s="wedfweHSDYDncdfSHYD"
s2="UIHDFnvdHJDFfdjk"
def niz(str):
    return str.lower()
def verh(str):
    str.upper()
    return str.upper()


print(verh(s))
print(niz(s))

def kvad(num):
    return num ** 2

numbers = [i for i in range(1,10)]
numbers2= list(map(kvad,numbers))
print(numbers)
print(numbers2)

f=open('file.txt','w')
f.write("The first national preserves were Big Thicket National Preserve in Texas and Big Cypress National Preserve in Florida, both established in 1974. The Big Cypress Swamp, adjacent to Everglades National Park and originally intended to be included in it, was at risk of destruction by a proposed airport. Opposition by conservationists and studies showing its role in water protection led to its cancellation after one runway was built, and President Richard Nixon proposed the area's preservation as Big Cypress National Fresh Water Reserve to protect the local water supply. Congressional deliberation resulted in a new designation of a national preserve that bought out private landowners to conserve  The Big Thicket, a large area of swamps and forests, was originally proposed to be preserved as a state park or national park, but these were opposed by timber firms who wanted to retain their logging lands. A 1967 survey by the National Park Service proposed establishing nine units representative of the variety of plant life in the region, but because the thicket was already fragmented by roads and logging, it would not qualify as a national park. National monument was also deemed a suboptimal designation, and compromise on the boundary and management provisions eventually led to its establishment as a national preserve. The bills creating both preserves were signed on the same day by President Gerald Ford and contained similar wording limiting construction, agriculture, and mineral extraction to that still assuring the area's natural and ecological integrity in perpetuity,while permitting hunting.")

f.close()
f2=open('file.txt','r')


def func (word):
    if word in clov:
        clov[word]+=1
    else:
        clov[word]=1
clov=dict()
for line in f2:
    k=line.split()
# k = list(map(lambda x: x.split(),f2))
list(map(func,k))
print(clov)


