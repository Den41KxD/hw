
import unittest
import HWList
class payments(unittest.TestCase):
    def setUp(self) -> None:
        self.ff = HWList.LinkedList()
        self.ff.append(1)
        self.ff.append(2)
        self.ff.append(3)
        return super().setUp()

    def test_empty(self):
        self.d=HWList.LinkedList()
        self.assertEqual(str(self.d), '||')

    def test_str(self):
        self.assertEqual(str(self.ff), '|1 -> 2 -> 3|')

    def test_append(self):
        self.ff.append('new')
        self.assertEqual(str(self.ff), '|1 -> 2 -> 3 -> new|')

    def test_len(self):
        self.assertEqual(len(self.ff), 3)

    def test_index(self):
        self.assertEqual(self.ff[2], 3)

    def test_change(self):
        self.ff.append('new')
        self.ff[2]= 'changed'
        self.assertEqual(str(self.ff), '|1 -> 2 -> changed -> new|')

    def test_del(self):
        self.ff.append('new')
        self.ff[2] = 'changed'
        del self.ff[1]
        self.assertEqual(str(self.ff), '|1 -> changed -> new|')

    def test_cont(self):
        self.ff.append('new')
        self.ff[2] = 'changed'
        del self.ff[1]
        self.ff3=HWList.LinkedList()
        self.ff3.append([5,6,])
        self.assertEqual(str(self.ff + self.ff3), '|1 -> changed -> new -> 5 -> 6|')

    def test_eq(self):
        self.ff4=HWList.LinkedList()
        self.ff4.append([1, 'changed', 'new'])
        self.ff5 = HWList.LinkedList()
        self.ff5.append([1, 'changed', 'ne'])
        try:
            self.assertEqual(str(self.ff4), str(self.ff5))
            print('equal')
        except:
            print('Not equal')

    def tearDown(self) -> None:
        return super().tearDown()

