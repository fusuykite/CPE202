from array_stack import *

# string --> value
# reads an expression in postfix form and returns the answer
def postfix_calc(string):
    stack = empty_stack()
    new = string.split()
    for i in new:
        if i in '+ - * /':
            tup1 = pop(stack)
            x = float(tup1[0])
            tup2 = pop(tup1[1])
            y = float(tup2[0])
            stack = tup2[1]
            if i == '+':
                res = x + y
            elif i == '-':
                res = y - x
            elif i == '*':
                res = x * y
            elif i == '/':
                res = y/x
            stack = push(stack, res)
        else:
            stack = push(stack, i)
    return float(peek(stack))

