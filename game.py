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
- Add a GUI
'''

class Game:
    
    def __init__(self):
        self.difficulty = 2 
        self.max_int = 10
        self.correct = 0
        self.total = 0
        self.max_equations = 10
        self.rb = RingBuffer(self.difficulty)
    
    def nextEquation(self):
        # Keep track of the number of equations
        self.total += 1
        # Create the equation
        eq = Equation(10) 
        # Add it to the buffer
        self.rb.add(eq)
        # And display it 
        return '#%s) %s' %  (self.total, eq)

    def validateAnswer(self, answer):
        if(self.rb.getOldest().validate(answer)):
            self.correct +=1
            return True
        else:
            return False

    
    def gameLoop(self):
        # Show equations until the ring buffer is full
        while(not self.rb.isFull()):
            nextEquation() 
            self.total += 1
            sleep(3)
        
        response = input('Begin! :') 
        while(total < max_equations):
            # Remove the previous equation
            print '\n' * 80
            # Check the answer to the oldest equation 
            if(self.rb.getOldest().validate(response)):
                print("Correct!")
                self.correct +=1
        
            nextEquation()
            self.total += 1
        
            # Get the next answer
            response = input(':')
