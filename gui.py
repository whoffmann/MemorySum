from Tkinter import *
from game import Game
from time import sleep

class GameDisplay(Frame):

    def __init__(self, parent):
        # Create a new game object
        self.game_logic = Game()

        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Memory Sums!")

        self.pack(fill=BOTH, expand=1)
        self.var = IntVar()

        # Create a string variable
        self.eq = StringVar()
        self.user_input = StringVar()

        # Create a input box widget
        self.input_box = Entry(self, textvariable= self.user_input)

        # Create a text box widget
        self.tb = Text(self, width = 40, height = 5)
        
        # Bind a key to the widget
        self.input_box.bind('<Key-Return>', self.onClick)

        self.tb.pack() 
        self.input_box.pack()
    
        # Start by showing equations
        while(not self.game_logic.rb.isFull()):
            self.tb.delete(1.0, 3.0)
            self.tb.insert(1.0, self.game_logic.nextEquation())
            sleep(1)

    def onClick(self, event=None):
        ''' Event that occurs when the answer button is pressed the incoming
        event with either be from a click or the enter button being pressed
        '''
        self.tb.delete(1.0, 3.0)
        # Verify the answer in the text box
        print self.user_input.get()
        if(self.game_logic.validateAnswer(self.user_input.get())):
            self.tb.insert(2.0, 'Correct!')
        self.tb.insert(1.0, self.game_logic.nextEquation())

        # Clear the input box
        self.user_input.set('')
    
def main():
    root = Tk()
    root.geometry("300x150+300+500")
    app = GameDisplay(root)
    root.mainloop()

if __name__ == '__main__':
    main()
