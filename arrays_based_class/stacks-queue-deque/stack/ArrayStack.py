"""
Modify the ArrayStack implementation so that the stack's capacity is limited to maxlen elements, where maxlen
is an optional parameter to the constructor (that defaults to None). If push is called when the stack is at
full capacity, throw a Full exception.
    
"""

class ArrayStack:
    def __init__(self, maxlen=None):

        self._maxlen = maxlen
        self._data = [None] * maxlen if maxlen != None else []
        self._top = -1
        
    def __len__(self):
        return len(self._data)


    def push(self, value):
        if self._maxlen == self._top + 1:
            raise Full("The stack is full.")

        self._top += 1
        if self._maxlen is not None:
            self._data[self._top] = value

        else:
            self._data.append(value)
            

    def pop(self):
        if self.is_empty():
            raise Empty("The stack is empty.")

        item = self._data[self._top]

        if self._maxlen is not None:
            self._data[self._top] = None
        else:
            self._data.pop()
            
        self._top -= 1
        return item


    def top(self):
        if self.is_empty():
            raise Empty("The stack is empty.")
        return self._data[self._top]
    

    def is_empty(self):
        return self._top == -1


    def p(self):
        print(self._data[:self._top + 1])
        

class Empty(Exception):
    """Raise if a container is empty."""

class Full(Exception):
    """Raise if a container is full."""



import unittest

class TestArrayStack(unittest.TestCase):

    def test_push_and_pop(self):
        s = ArrayStack()
        s.push(10)
        s.push(20)
        s.push(30)
        self.assertEqual(s.pop(), 30)
        self.assertEqual(s.pop(), 20)
        self.assertEqual(s.pop(), 10)
        self.assertTrue(s.is_empty())

    def test_top(self):
        s = ArrayStack()
        s.push('a')
        s.push('b')
        self.assertEqual(s.top(), 'b')
        s.pop()
        self.assertEqual(s.top(), 'a')

    def test_empty_stack(self):
        s = ArrayStack()
        with self.assertRaises(Empty):
            s.pop()
        with self.assertRaises(Empty):
            s.top()

    def test_maxlen_limit(self):
        s = ArrayStack(maxlen=2)
        s.push(1)
        s.push(2)
        with self.assertRaises(Full):
            s.push(3)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.pop(), 1)

    def test_len(self):
        s = ArrayStack()
        self.assertEqual(len(s), 0)
        s.push(5)
        self.assertEqual(len(s), 1)
        s.push(10)
        self.assertEqual(len(s), 2)
        s.pop()
        self.assertEqual(len(s), 1)

if __name__ == '__main__':
    unittest.main()
