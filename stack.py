class Stack:
    def __init__(self):
        self.stack = list()

    def push(self,item):
        """
            Add the item to the stack.
        """
        self.stack.append(item)
        return '{}, has recently been added to the stack.'.format(item)

    def __is_empty(self):
        """
            Check if the stack is emtpy or not.
        """
        if len(self.stack) == 0:
            return True
        else:
            return False


    def pop(self):
        """
            Remove the last item of the stack.
        """
        if self.__is_empty() == True:
            raise RuntimeError("The stack is empty.")
        else:

            val = self.stack.pop()
            return '{}, has recently been remove from the stack'.format(val)

    @property
    def peek(self):
        """
            Get the last item of the stack.
        """
        if self.__is_empty() == True:
            raise RuntimeError("The stack is empty.")
        else:
            val = self.stack[-1]
            return '{}, is the top item in the stack.'.format(val)
        

    @property
    def display(self):
        """
            Get the items of the stack
        """           
        return '{}'.format(self.stack)

st = Stack()
print(st.push(23))
st.push(56)
st.push(56543)
st.push(543)


print(st.display)
print(st.peek)
print(st.display)
print(st.pop())
print(st.display)





