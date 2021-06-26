"""
Реализуйте необходимые методы для того, чтобы следующий код выполнился

Должна быть возможность инициализировать LinkedList с помощью списка, или пустым.
"""

import copy


class Element:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if type(value) == list:
            for i in value:
                self.new = Element(i)
                if self.head is None:
                    self.head = self.new
                else:
                    last = self.head
                    while last.next:
                        last = last.next
                    last.next = self.new
        else:
            self.new = Element(value)
            if self.head is None:
                self.head = self.new
                return
            last = self.head
            while last.next:
                last = last.next
            last.next = self.new

    def __str__(self):
        if self.head is None:
            return '||'
        else:
            s = '|'
            printval = self.head
            while printval is not None:
                s += str(printval.value) + ' -> '
                printval = printval.next

            return s[:-4] + '|'

    def __len__(self):
        lenn = self.head
        count = 0
        while lenn is not None:
            lenn = lenn.next
            count += 1
        return count

    def __getitem__(self, pos):
        elem = self.head
        count = 0
        while count != pos:
            elem = elem.next
            count += 1
        return elem.value

    def __setitem__(self, pos, value):
        elem = self.head
        count = 0
        while elem.next is not None:
            elem = elem.next
            count += 1
            if count == pos:
                elem.value = value
        return

    def __delitem__(self, pos):
        elem = self.head
        count = 1
        if pos == 0:
            self.head = elem.next
        while elem.next is not None:
            if count == pos:
                prev = elem
                elem = elem.next
                prev.next = elem.next
            elem = elem.next
            count += 1

    def __add__(self, other):
        elem = self.head
        flag = True
        while elem.next is not None and flag:
            elem = elem.next
            if elem.next:
                for Any in other:
                   self.append(Any)
                flag = False
        return self

    def __eq__(self, other):
        if len(self) != len(other):
            return False
        elem = self.head
        elem2=other.head
        if elem.value == elem2.value:
            while elem.next is not None:
                    elem=elem.next
                    elem2=elem2.next
                    if elem.value == elem2.value:
                        pass
                    else: return False
        return True
    def __bool__(self):
        if self.head is None: return True
        else: return False

    def __iter__(self):
        elem=self.head
        if elem==self.head:return LinkedListIterator(elem)
        while elem.next is not None:
            elem=elem.next
            return LinkedListIterator(elem)
class LinkedListIterator:

    def __init__(self, head):
        self.current = head

    def __next__(self):
        if self.current == None:
            raise StopIteration
        else:
            item = self.current.value
            self.current = self.current.next
            return item

if __name__=='__main__':
    ll = LinkedList()
    print(ll)
    ll.append(132)
    ll.append(256)
    ll.append('lol')
    ll.append(372)
    ll.append(421)
    print(ll)
    print('\ncopy and add\n')
    ll2=copy.deepcopy(ll)
    ll2.append('new')
    print(ll2)


    print(f"\nlen = {len(ll)} \n")

    print(f"element 2 = {ll[2]}\n")

    print(f"ll after change:\n")
    ll[1]='changed'
    print(ll)

    print("\nRemuve in ll2:")
    print('\n')
    del ll2[2]
    print(ll2)

    print('\nll3')
    ll3=LinkedList()
    ll3.append([5,6])
    print(ll3)
    print('ll3 add ll2')
    print(ll2+ll3)
    print('\n eq:')

    ll4=LinkedList()
    ll5=LinkedList()
    ll4.append([3,4,5])
    ll5.append([3,4,6])
    if ll4==ll5:print('True')
    else: print('False')
    if ll:pass

    print('\niter')
    print(ll)
    for i in ll:
        print(i)



# print(ll)
# # empty list should be represented as two pipes (vertical lines)
# # ||
# ok

# print(ll2)
# # |1 -> 2 -> 3|
#ok

# ll2.append('new')
# print(ll2)
# # |1 -> 2 -> 3 -> 'new'|
#ok
#

# print(len(ll2))
# # 4
#ok

# print(ll2[2])
# # 3
#ok

# ll2[2] = 'changed'
# print(ll2)
# # |1 -> 2 -> 'changed' -> 'new'|
#ok

# del ll2[1]
# print(ll2)
# # |1 -> 'changed' -> 'new'|
#ok

# print('truthy' if ll else 'falsy')
# # falsy
#ok

# print('truthy' if ll2 else 'falsy')
# # truthy
# ok

# ll3 = LinkedList([5, 6])
# print(ll2 + ll3)
# # |1 -> 'changed' -> 'new' -> 5 -> 6|
#ok

# ll4 = LinkedList([1, 'changed', 'new'])
# print('equal' if ll2 == ll4 else 'not equal')
# # equal
# ok

# print('not equal' if ll2 != ll3 else 'equal')
# # not equal
# ok

# Если предыдущего покажется маловато, то вот со звездочкой на десерт:
# for i in ll2:
#     print(i)