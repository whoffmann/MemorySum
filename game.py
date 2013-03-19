from equation import Equation
from ringbuffer import RingBuffer

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
- Make the previous answers hidden (the game is pointless
 if there is nothing to memorize)
- Improve usuability by adding instructions and more prompts
- Add a GUI
'''

difficulty = 2 # How many equations back the player has to remember
max_int = 10

correct = 0
total = 0
max_equations = 10

rb = RingBuffer(difficulty)

def nextEquation():
    # Create the equation
    eq = Equation(10) 
    # Add it to the buffer
    rb.add(eq)
    # And display it 
    print '#%s) %s' %  (total, eq)

# Show equations until the ring buffer is full
while(not rb.isFull()):
    nextEquation() 
    total += 1

response = input('Begin! :') 
while(total < max_equations):
     
    # Check the answer to the oldest equation 
    if(rb.getOldest().validate(response)):
        print("Correct!")
        correct +=1
    

    nextEquation()
    total += 1

    # Get the next answer
    response = input(':')
