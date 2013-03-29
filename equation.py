from random import randint 

class Equation:
    def __init__(self, max_int, random_func=randint):
        '''Class to represent a randomly generated equation

        max_int -- the maximum random value to use

        random_func(lower, upper) -- function that generates a random number,
        inclusively, between lower and upper. (default random.randint)
        '''
        
        self.random_func = random_func
        # First and second operands 
        self.a = self.random_func(0,max_int)
        self.b = self.random_func(0,max_int)

        # The operator. 0 for addition, 1 for subtraction
        self.operator = self.random_func(0,1)
        # Define the answer
        self.answer = 0
        # Define the string representation of the sign
        self.operator_str = ''
        # Addition
        if(self.operator == 0):
            self.operator_str = '+'
            self.answer = self.a + self.b
        # Subtraction
        elif(self.operator == 1):
            self.operator_str = '-'

            # If the result is negative, swap the operands
            if(self.a < self.b):
                self.a, self.b = self.b, self.a
                
            self.answer = self.a - self.b
    
    def validate(self, response):
        ''' Checks if the user has submitted the right answer for this 
        equation. 
        
        response -- the user's answer to this equation
        '''
        return self.answer == response

    def __str__(self):
        return "%s %s %s = ?" % (self.a, self.operator_str, self.b)

# if __name__ == '__main__':
