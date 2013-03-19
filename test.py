import unittest
from equation import Equation
from ringbuffer import RingBuffer

class EquationTests(unittest.TestCase):

    def fakeRandom(self, lower, upper):
        '''Fake random number generator follows an array to decide
        which numbers to return
        '''
        num = self.fake_numbers[self.fake_iterator]
        self.fake_iterator += 1
        return num 
    
    def setUp(self):    
        self.fake_numbers = [] # list of random numbers to traverse
        self.fake_iterator = 0 # the next index of fake_numbers to return

    def test_addition(self):
        '''An addition operation should be valid

        1 + 2 = 3
        '''
        # a = 1, b = 2, operator = addition
        self.fake_numbers = [1, 2, 0] 

        eq = Equation(10, self.fakeRandom)

        self.assertTrue(eq.a is 1 and  eq.b is 2 and eq.operator is 0)
        self.assertTrue(eq.validate(3)) 

    def test_subtraction1(self):
        '''A subtraction operation should be valid

        2-1 = 1
        '''
        # a = 2, b = 1, operator = subtraction
        self.fake_numbers = [2, 1, 1]

        eq = Equation(10, self.fakeRandom)

        self.assertTrue(eq.a is 2 and  eq.b is 1 and eq.operator is 1)
        self.assertTrue(eq.validate(1)) 

    def test_subtraction2(self):
        '''Subtraction should always be positive

        When the first random number generated is smaller than the second
        during a subtraction, the results should remain positive by swapping
        the two operands.
        ''' 
        # a = 1, b = 2, operator = subtraction
        self.fake_numbers = [2, 1, 1] 

        eq = Equation(10, self.fakeRandom)

        self.assertTrue(eq.a is 2 and  eq.b is 1 and eq.operator is 1)
        self.assertTrue(eq.validate(1)) 

class RingBufferTests(unittest.TestCase):
    def test_add(self):
        '''An non-full ring buffer should contain everything inserted into it
        ''' 
        rb = RingBuffer(3)

        rb.add(1)
        self.assertListEqual(rb.toList(), [1])
        rb.add(2)
        rb.add(3)
        self.assertListEqual(rb.toList(), [1,2,3])
        
    def test_add_full(self):
        '''A full ring buffer should remove the oldest element after a new add
        '''
        rb = RingBuffer(3)

        rb.add(1)
        rb.add(2)
        rb.add(3)
        rb.add(4)
        self.assertListEqual(rb.toList(),[2,3,4])

    def test_getOldest(self):
        '''You can access the oldest element in the ring buffer with getOldest
        When the list is empty, return None
        '''
        rb = RingBuffer(2)
        
        self.assertTrue(rb.getOldest() == None)
        rb.add(1)
        self.assertTrue(rb.getOldest() == 1)
        rb.add(2)
        self.assertTrue(rb.getOldest() == 1)
        rb.add(3)
        self.assertTrue(rb.getOldest() == 2)

    def test_size_one(self):
        '''The ring buffer behaves correctly when the max is 1
        '''
        rb = RingBuffer(1)

        self.assertTrue(rb.getOldest() == None)
        rb.add(1)
        self.assertTrue(rb.getOldest() == 1)
        rb.add(2)
        self.assertTrue(rb.getOldest() == 2)
        rb.add(3)
        self.assertTrue(rb.getOldest() == 3)

if __name__ == '__main__':
    unittest.main()
