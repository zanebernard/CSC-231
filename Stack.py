class Stack:

    def __init__(self):
        """Initilizes the stack as a list. Accepts nothing. Returns nothing."""
        self.__stack = []

    def push(self, item):
        """Pushes item on top of the stack as the end of the list. Accepts
        variable 'item'. Returns nothing."""
        self.__stack.append(item)

    def pop(self):
        """Pops item from the top. Accepts nothing. Returns the item that was
        popped."""
        self.__stack.remove(self.__stack[len(self.__stack) - 1])
        return self.peek()

    def peek(self):
        """Peeks the item on top of the stack. Accepts nothing. Returns nothing.
        """
        if len(self.__stack) > 0:
            return self.__stack[len(self.__stack) - 1]
        else:
            return "Nothing on top."

    def is_empty(self):
        """Checks if the stack is empty. Accepts nothing. Returns True if the
        stack is empty. Otherwise, it returns false."""
        if len(self.__stack) == 0:
            return True
        else:
            return False

    def size(self):
        """Returns the size of the stack. Accepts nothing."""
        return int(len(self.__stack))
