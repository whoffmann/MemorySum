from equation import Equation
from ringbuffer import RingBuffer
from time import sleep

'''
This is a rough draft of the equation memory game

How to play:

First, the player is shown k number of equations, one at a
time, depending on the difficulty level. The player must 
then type in the answer to the oldest equation while still 
remembering the answer to each equation seen.

The goal is to master each level of difficulty

The first level of difficulty is trivial. The answer is
the equation currently seen

The second level of diffiuclty requires one number to be
memorized. After the player memorizes the first answer, 
it becomes hidden and the second equation is shown. After 
typing in the answer for the first equation, the second
equation disappears and the third equation is shown, 
prompting the second question's answer. This continues
for each equation

TODO:
- Improve usuability by adding instructions and more prompts
'''

class Game:
    
    def __init__(self):
        # The number of equations the user is shown at the start
        self.difficulty = 2 

        # The maximum number that can appear in an equation 
        self.max_int = 10

        # Count of correct answers
        self.correct = 0
        
        # Total number of equations completed
        self.total = 0

        # Number of equations for the user to answer
        self.max_equations = 10 

        # Ring buffer of equations
        self.rb = RingBuffer(self.difficulty)
    
    def nextEquation(self):
        ''' Creates the next equation
            
        Returns a string representation of the equation for the user
        to see. The string includes the order number corresponding to
        the equation
        '''
        # Keep track of the number of equations
        self.total += 1
        # Create the equation
        eq = Equation(10) 
        # Add it to the buffer
        self.rb.add(eq)
        # And display it 
        return '#%s) %s' %  (self.total, eq)

    def validateAnswer(self, answer):
        ''' Validates the answer and increments the count of correct answers
        if the answer is correct.
        '''
        if(self.rb.getOldest().validate(answer)):
            self.correct +=1
            return True
        else:
            return False
    
def hideEquation():
    ''' Hides the last equation by printing a bunch of new lines
    '''
    print '\n' * 80 

if __name__ == '__main__':
    g = Game()
    # Show equations until the ring buffer is full
    while(not g.rb.isFull()):
        hideEquation()
        print g.nextEquation() 
        sleep(3)
      
    response = input('Begin! :') 
    while(g.total < g.max_equations):
        hideEquation()
        # Check the answer
        if(g.validateAnswer(response)):
            print("Correct!")

        print g.nextEquation()

        # Get the next answer
        # TODO: validate input
        response = input(':')

    # continue checking the answer for the last few equations
    while(g.total < g.max_equations+g.difficulty-1):
        if(g.validateAnswer(response)):
            print("Correct!")

        # Bump off the previous equation
        g.nextEquation()
        
        response = input(':')
    
    # Validate the last equation answered
    if(g.validateAnswer(response)):
       print("Correct!")

    print 'You got %s out of %s correct!' % (g.correct, g.max_equations)
