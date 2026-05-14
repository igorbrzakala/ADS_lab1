import string

# works without brackets [v1]
"""
class aStack:
    max_size = 0
    current_size = 0
    data = []

    def __init__(self, dtype, init_max_size):
        self.dtype = dtype
        self.max_size = init_max_size
        self.data = [None] * init_max_size

    def push(self, new_element):
        if self.current_size >= self.max_size:
            raise Exception("[ERROR]: Stack overflow!")

        if type(new_element) != self.dtype:
            print(self.dtype)
            print("\n")
            print(type(new_element))

            raise Exception("[ERROR]: wrong data type!")

        self.data[self.current_size] = new_element
        self.current_size += 1

    def pop(self):
        if self.current_size > 0:
            last_element = self.data[self.current_size - 1]
            self.current_size -= 1
            self.data[self.current_size] = None
            return last_element
        else:
            raise Exception("[ERROR]: poping from a stack with size already 0")

    def is_empty(self):
        if self.current_size > 0:
            return False
        else:
            return True

    def top(self):
        if self.current_size > 0:
            return self.data[self.current_size - 1]
        else:
            raise Exception("[ERROR]: stack is empty")

def precedence(operator):
    if operator == '+' or operator == '-':
        return 1
    elif operator == '*' or operator == '/':
        return 2

def to_postfix(infix):
    postfix = ""
    operatorsStack = aStack(str, 2048)

    for c in infix:
        if c == '+' or c == '-' or c == '*' or c == '/':
            if operatorsStack.is_empty():
                operatorsStack.push(c)
            else:
                if precedence(c) > precedence(operatorsStack.top()):
                    operatorsStack.push(c)
                else:
                    while operatorsStack.is_empty() == False and precedence(c) <= precedence(operatorsStack.top()):
                        postfix += operatorsStack.pop()
                        postfix += ' '

                    operatorsStack.push(c)
        elif c == ' ':
            pass
        else: #c is a num
            postfix = postfix + c + ' '

    while not operatorsStack.is_empty():
        postfix += operatorsStack.pop()
        postfix += ' '

    return postfix
"""
# ---

"""
notes: iterate through tokens using split().

- push ( onto the stack
- when ) is found, pop operators until ( is reached
"""

# works without brackets [v1]
class aStack:
    max_size = 0
    current_size = 0
    data = []

    def __init__(self, dtype, init_max_size):
        self.dtype = dtype
        self.max_size = init_max_size
        self.data = [None] * init_max_size

    def push(self, new_element):
        if self.current_size >= self.max_size:
            raise Exception("[ERROR]: Stack overflow!")

        if type(new_element) != self.dtype:
            print(self.dtype)
            print("\n")
            print(type(new_element))

            raise Exception("[ERROR]: wrong data type!")

        self.data[self.current_size] = new_element
        self.current_size += 1

    def pop(self):
        if self.current_size > 0:
            last_element = self.data[self.current_size - 1]
            self.current_size -= 1
            self.data[self.current_size] = None
            return last_element
        else:
            raise Exception("[ERROR]: poping from a stack with size already 0")

    def is_empty(self):
        if self.current_size > 0:
            return False
        else:
            return True

    def top(self):
        if self.current_size > 0:
            return self.data[self.current_size - 1]
        else:
            raise Exception("[ERROR]: stack is empty")

def precedence(operator):
    if operator == '+' or operator == '-':
        return 1
    elif operator == '*' or operator == '/':
        return 2

def to_postfix(infix):
    postfix = ""
    operatorsStack = aStack(str, 2048)

    for c in infix:
        if c == '+' or c == '-' or c == '*' or c == '/':
            if operatorsStack.is_empty():
                operatorsStack.push(c)
            else:
                if precedence(c) > precedence(operatorsStack.top()):
                    operatorsStack.push(c)
                else:
                    while operatorsStack.is_empty() == False and precedence(c) <= precedence(operatorsStack.top()):
                        postfix += operatorsStack.pop()
                        postfix += ' '

                    operatorsStack.push(c)
        elif c == ' ':
            pass
        else: #c is a num
            postfix = postfix + c + ' '

    while not operatorsStack.is_empty():
        postfix += operatorsStack.pop()
        postfix += ' '

    return postfix
# ---

infix = input("Enter the equation in infix notation: ")
print(to_postfix(infix))

# 3 + 6 * 2 - 5
