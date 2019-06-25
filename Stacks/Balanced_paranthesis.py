#take a string and return TRUE if it's parentheses are balanced or FALSE if it is not.


class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size() == 0:
            return None
        return self.items.pop()

def equation_checker(equation):
        """
        Check equation for balanced paranthesis
        """

        #Initiate stack object
        stack = Stack()

        #iterate through equation checking parentheses
        for char in equation:
            if char == "(":
                stack.push(char)
            elif char == ")":
                if stack.pop() == None:
                    return False

        #return true if balanced and false if not
        if stack.size() == 0:
            return True
        return False


print("Pass" if (equation_checker('((3^2 + 8)*(5/2))/(2+6)')) else "Fail")
print("Pass" if not (equation_checker('((3^2 + 8)*(5/2))/(2+6))')) else "Fail")
