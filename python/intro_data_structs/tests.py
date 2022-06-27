import unittest
from enqueue import ListIndexUpdate as LIU

class TestListQueue(unittest.TestCase):
    def testinit(self):
        q = LIU()

    def testaddandremoveoneitem(self):
        q = LIU()
        q.enqueue(3)
        self.assertEqual(q.dequeue(),3)

    def testalternatingaddremove(self):
        q = LIU()
        for i in range(1000):
            q.enqueue(i)
            self.assertEqual(q.dequeue(), i)

    def testmanyoperations(self):
        q = LIU()
        for i in range(1000):
            q.enqueue(2 * i + 3)
        for i in range(1000):
            self.assertEqual(q.dequeue(), 2 * i + 3)

    def testlength(self):
        q = LIU()
        self.assertEqual(len(q), 0)
        for i in range(10):
            q.enqueue(i)
        self.assertEqual(len(q), 10)
        for i in range(10):
            q.enqueue(i)
        self.assertEqual(len(q), 20)
        for i in range(15):
            q.dequeue()
        self.assertEqual(len(q), 5)

if __name__ == '__main__':
    unittest.main()
