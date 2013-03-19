class RingBuffer:
    ''' Ring Buffer data structure

    When inserting after the maximum size is exceeded, the oldest element
    is removed.
    
    This implementation switches states once the buffer reaches max size
    to eliminate max check for every insertion.
    '''
    def __init__(self,size_max):
        '''Initializes the Ring Buffer

        size_max -- maximum size of the Ring Buffer
        '''
        self.size_max = size_max
        self.data = []
    
    def full_add(self, item): 
        '''Adds to the ring buffer when it is full by removing
        the oldest element
        '''
        self.data = self.data[1:self.size_max]
        self.data.append(item)
        
    def add(self, item):
        '''Adds to the ring buffer when it is not full
        '''
        self.data.append(item)

        # Use a new function to add elements if the buffer is full
        if(len(self.data) == self.size_max):
            self.add = self.full_add

    def __str__(self):
        return self.data

    def toList(self):
        return self.data
    
    def isFull(self):
        '''Returns true if the buffer is at max size
        '''
        return len(self.data) == self.size_max

    def getOldest(self):
        return None if len(self.data) is 0 else self.data[0]
