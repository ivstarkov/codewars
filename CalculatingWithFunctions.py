#number returns number

def zero(n = ""): 
    if n == "":
        return 0
    elif n[0] == "+":
        return 0 + int(n[1])
    elif n[0] == "-":
        return 0 - int(n[1])
    elif n[0] == "*":
        return 0 * int(n[1])
    elif n[0] == "/":
        return 0 // int(n[1])
    
def one(n = ""):
    if n == "":
        return 1
    elif n[0] == "+":
        return 1 + int(n[1])
    elif n[0] == "-":
        return 1 - int(n[1])
    elif n[0] == "*":
        return 1 * int(n[1])
    elif n[0] == "/":
        return 1 // int(n[1])
    
def two(n = ""):
    if n == "":
        return 2
    elif n[0] == "+":
        return 2 + int(n[1])
    elif n[0] == "-":
        return 2 - int(n[1])
    elif n[0] == "*":
        return 2 * int(n[1])
    elif n[0] == "/":
        return 2 // int(n[1])

def three(n = ""):
    if n == "":
        return 3
    elif n[0] == "+":
        return 3 + int(n[1])
    elif n[0] == "-":
        return 3 - int(n[1])
    elif n[0] == "*":
        return 3 * int(n[1])
    elif n[0] == "/":
        return 3 // int(n[1])
    
def four(n = ""):
    if n == "":
        return 4
    elif n[0] == "+":
        return 4 + int(n[1])
    elif n[0] == "-":
        return 4 - int(n[1])
    elif n[0] == "*":
        return 4 * int(n[1])
    elif n[0] == "/":
        return 4 // int(n[1])
    
def five(n = ""):
    if n == "":
        return 5
    elif n[0] == "+":
        return 5 + int(n[1])
    elif n[0] == "-":
        return 5 - int(n[1])
    elif n[0] == "*":
        return 5 * int(n[1])
    elif n[0] == "/":
        return 5 // int(n[1])
    
def six(n = ""):
    if n == "":
        return 6
    elif n[0] == "+":
        return 6 + int(n[1])
    elif n[0] == "-":
        return 6 - int(n[1])
    elif n[0] == "*":
        return 6 * int(n[1])
    elif n[0] == "/":
        return 6 // int(n[1])
    
def seven(n = ""):
    if n == "":
        return 7
    elif n[0] == "+":
        return 7 + int(n[1])
    elif n[0] == "-":
        return 7 - int(n[1])
    elif n[0] == "*":
        return 7 * int(n[1])
    elif n[0] == "/":
        return 7 // int(n[1])
    
def eight(n = ""):
    if n == "":
        return 8
    elif n[0] == "+":
        return 8 + int(n[1])
    elif n[0] == "-":
        return 8 - int(n[1])
    elif n[0] == "*":
        return 8 * int(n[1])
    elif n[0] == "/":
        return 8 // int(n[1])
    
def nine(n = ""):
    if n == "":
        return 9
    elif n[0] == "+":
        return 9 + int(n[1])
    elif n[0] == "-":
        return 9 - int(n[1])
    elif n[0] == "*":
        return 9 * int(n[1])
    elif n[0] == "/":
        return 9 // int(n[1])
    

def plus(n): 
    txt = "+{}"
    return txt.format(n)
def minus(n):
    txt = "-{}"
    return txt.format(n)
def times(n):
    txt = "*{}"
    return txt.format(n)
def divided_by(n):
    txt = "/{}"
    return txt.format(n)



print(one(divided_by(two())))