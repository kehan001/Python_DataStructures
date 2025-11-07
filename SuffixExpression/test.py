
from enum import Enum
from Stack_UseArr.StackClass import Stack


#这个程序只支持单位数的后缀表达式，多位数的等后续吧
class contentType(Enum):
    ADD=0
    SUB=1
    MUL=2
    DIV=3
    MOD=4 # %
    #EOS=5 # \0 C里面字符串的最末尾
    NUM=6

expression = "82/2+56*-"

def getToken(unit):
    match unit:
        case "+":
            return contentType.ADD
        case "-":
            return contentType.SUB
        case "*":
            return contentType.MUL
        case "/":
            return contentType.DIV
        case "%":
            return contentType.MOD
        case _:
            return contentType.NUM


def calculate(op1, op2, symbol):
    match symbol:
        case "+":
            return op1+op2
        case "-":
            return op1-op2
        case "*":
            return op1*op2
        case "/":
            return op1/op2
        case "%":
            return op1%op2

def evaluate(expression):
    #最先出栈的放到op2中，第二个出栈的放到op1
    stack = Stack()
    for i in expression:
        if(getToken(i) == contentType.NUM):
            stack.push(int(i))
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            symbol = i
            stack.push(calculate(op1, op2, symbol))
    return stack.pop()

print(evaluate(expression))