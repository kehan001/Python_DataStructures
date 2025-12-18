from enum import Enum

from Stack_UseArr.StackClass import Stack


class contentType(Enum):
    LEFT_PARE=0
    RIGHT_PARE=1
    ADD=2
    SUB=3
    MUL=4
    DIV=5
    MOD=6 # %
    EOS=7
    NUM=8

expression = "x/(i-j)*y"

def getToken(unit):
    match unit:
        case "(":
            return contentType.LEFT_PARE
        case ")":
            return contentType.RIGHT_PARE
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

OP_TO_CHAR = {
    contentType.ADD: "+",
    contentType.SUB: "-",
    contentType.MUL: "*",
    contentType.DIV: "/",
    contentType.MOD: "%",
    contentType.LEFT_PARE: "(",
    contentType.RIGHT_PARE: ")"
}

def convert(expression):
    inStack = [0, 20, 12, 12, 13, 13, 13, 0]  #栈内优先级和栈外优先级
    outStack = [20, 20, 12, 12, 13, 13, 13, 0]
    stack = Stack()
    stack.push(contentType.EOS)
    suffix = [] #存放结果
    for i in expression:
        token = getToken(i)
        if token == contentType.NUM:
            suffix.append(i)
            continue
            #如果是右括号，且栈顶元素不是左括号，持续出栈并输出，直到栈顶元素为左括号
        if token == contentType.RIGHT_PARE:
            while ((element := stack.pop()) != contentType.LEFT_PARE):
                suffix.append(OP_TO_CHAR[element])
            continue
            # 不是右括号的情况: 将栈顶元素出栈，重新判断填入新元素
        while inStack[stack.peek().value] >= outStack[token.value]:
            suffix.append(OP_TO_CHAR[stack.pop()])

        stack.push(token)

    #结束for循环，剩余元素全部出栈
    while stack.peek() != contentType.EOS:
        suffix.append(OP_TO_CHAR[stack.pop()])

    return "".join(suffix)


print(convert(expression))
