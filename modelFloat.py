x = 0
y = 0
op = ""

def init (a, c, b):
    global x
    global y
    global op
    x = a
    y = b
    op = c

def sum():
    return x + y

def sub():
    return x - y

def mul():
    return x * y

def dev():
    return x / y

def chooseOp():
    if op == "+":
        return sum()
    elif op == "-":
        return sub()
    elif op == "*":
        return mul()
    elif op == "/":
        return dev()
    else: return "Некорректный выбор операции"