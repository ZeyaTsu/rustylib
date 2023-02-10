import random

class Sugaku:
    def __init__(self):
        self.debug = False
        self.num = ["1","2","3","4","5","6", "7","8","9"]
        self.operators = ["+","-","/","*"]
        self.finalN = []
        self.finalC = []
        self.length = 1
        self.calength = 2

    def max_digit_length(self, length):
        return length

    def max_cal_length(self, calength):
        return calength    

    def clear(self):
        self.finalN.clear()
        self.finalC.clear()

    def numbers(self): 
        max_len = self.max_digit_length(self.length)
        for i in range(1, max_len+1):
            n = random.choice(self.num)
            self.finalN.append(n)

        if self.debug == True:
            print(self.finalN)

        x = ''.join(self.finalN)
        return x

    def oper(self, mode:str):
        self.numbers()
        max_len = self.max_digit_length(self.length)
        cal_len = self.max_cal_length(self.calength)

        for i in range(1, cal_len): # Loop
            op = random.choice(self.operators)
            self.finalN.append(op) # Adding operators, calling back numbers() to get the next one.
            self.numbers()

        y1 = ''.join(self.finalN) # Final calculation in str
        y = eval(y1) # Resolve
        y = str(y)

        if mode == 'with':
            return (y1,"=",y)
        if mode == 'no-res':
            return y1
        if mode == 'res':
            return y

    def convert(self, word): # Converting oper() to a string without ( , ) ' symbols 
        convert = ''
        for char in word:
            if char not in ('(',')', "'", ','):
                convert += char
        
        wordc = convert
        return wordc
