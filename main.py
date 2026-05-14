class Stack:
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

        if not isinstance(new_element, self.dtype):

            raise Exception("[ERROR]: wrong data type!")
        
            """
            print("[ERROR]: Element ")
            print(new_element)
            print("is not of type ")
            print(self.dtype.__name__)
            """ 

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


"""
my_stack = aStack(10)
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

my_stack.pop()

print(my_stack.top())
"""



"""
infix = input("Enter the equation in infix notation: ")
postfix = ""
operatorsStack = Stack(2048)

for c in infix:
    if c == '+' or c == '-' or c == '*' or c == '/':
        pass
    elif c == ' ':
        pass
    else: #c is a num
        postfix = postfix + c + ' '
"""