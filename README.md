MemorySum
=========

Python memory game


This is currenly a rough draft of the equation memory game

How to play:

First, the player is shown k number of equations, one at a
time, depending on the difficulty level. The player must 
then type in the answer to the oldest equation while still 
remembering the answer to each equation seen.

The goal is to master each level of difficulty.

The first level of difficulty is trivial. The answer is
the equation currently seen.

The second level of difficulty requires one number to be
memorized. After the player memorizes the first answer, 
it becomes hidden and the second equation is shown. After 
typing in the answer for the first equation, the second
equation disappears and the third equation is shown, 
prompting the second question's answer. This continues
for each equation.

HOW TO RUN:
-----------
To play the command line version, run game.py using python:
> python game.py

To run the GUI version, run gui.py:
> python gui.py

If you make changes to ringbuffer.py or equation.py, you can 
run tests by running test.py:
> python test.py

TODO:
-----
- Improve usuability by adding instructions and more prompts
- Handle edge cases for user input
- Allow user to specify difficulty level
- Display user score in GUI
