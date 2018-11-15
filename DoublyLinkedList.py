class Node:

    def __init__(self, data):
        """Initializes 3 variables: 'data', 'previous', and 'next'."""
        self.data = data
        self.next = None
        self.previous = None

    def setData(self, newdata):
        """Takes one positional argument as new data. Sets the new data
        for variable 'data'."""
        self.data = newdata

    def setNext(self, newnext):
        """Takes one positional argument as new next. Sets the new next
        value for variable 'next'."""
        self.next = newnext

    def setPrevious(self, newprevious):
        """Takes one positional argument as new next. Sets the new next
        value for variable 'next'."""
        
    def __str__(self):
        """Returns variable 'data' as a string."""
        return str(self.data)

class DoublyLinkedList:

    def __init__(self):
        
        self.head = None
        self.tail = None

    def __iter__(self):
        """Allows the list to be iterated through. Returns nothing."""
        current = self.head     #starts from the top
        
        while current is not None:
            yield current
            current = current.next  #increments through

    def is_empty(self):
        """Returns T/F value of this predicate: self.head = None."""
        return self.head == None

    def size(self):
        """Iterates through the list and increments its size. Returns the size.
        """
        size = 0
        for i in self:          #iterates through list
            size += 1           #increments the size
        return size
    def add(self, item):
        """Takes one positional argument as a new item. Creates a node from
        that item and links our previous 'head' as the next element."""
        new = Node(item)        #creates the new node
        new.setNext(self.head)  #moves the head as the next element
        self.head = new         #new element is new head
