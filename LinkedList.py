class Node:

    def __init__(self, data):
        """Initializes 2 variables: 'data' and 'next'. 'next' points to
        the next element in the list, otherwise it has a value of None."""
        self.data = data
        self.next = None    #points to the next element in the list

    def getData(self):
        """Returns the information in the 'data' variable."""
        return self.data

    def getNext(self):
        """Returns the information in the 'next' variable."""
        return self.next

    def setData(self, newdata):
        """Takes one positional argument as new data. Sets the new data
        for variable 'data'."""
        self.data = newdata

    def setNext(self, newnext):
        """Takes one positional argument as new next. Sets the new next
        value for variable 'next'."""
        self.next = newnext
        
    def __str__(self):
        """Returns variable 'data' as a string."""
        return str(self.data)

class LinkedList:

    def __init__(self):
        """Initializes one variable 'head'. Head represents the head element
        in the linked list from which the rest of the elements stem from."""
        self.head = None

    def __iter__(self):
        """Allows the list to be iterated through. Returns nothing."""
        current = self.head     #starts from the top
        
        while current is not None:
            yield current
            current = current.next  #increments through
            
    def is_empty(self):
        """Returns T/F value of this predicate: self.head = None."""
        return self.head == None

    def add(self, item):
        """Takes one positional argument as a new item. Creates a node from
        that item and links our previous 'head' as the next element."""
        new = Node(item)        #creates the new node
        new.setNext(self.head)  #moves the head as the next element
        self.head = new         #new element is new head

    def size(self):
        """Iterates through the list and increments its size. Returns the size.
        """
        size = 0
        for i in self:          #iterates through list
            size += 1           #increments the size
        return size

    def append(self, item):
        """Takes one positional argument as a new item. Creates as a new node
        and links it to the end of the linked list. Returns nothing."""
        if self.is_empty():    #if the list is empty
            self.add(item)      #we simply just add the item
        else:
            current = self.head #intializes the first element
            
            while current.next is not None: #stops the iteration once there is no next element
                current = current.next
            new = Node(item)
            current.setNext(new)        #links the item to the last element
            
    def pop(self, pos=None):
        """Takes a default argument as the pos. User can enter a desired index
        for popping. Otherwise, it pops the last element. Returns the popped
        element."""
        
        #init
        current = self.head     #init first element (estabilsh first element of list)
        pos_not_reached = True  #init flag (for exiting while)
        counter = 0             #init counter (for reaching position values)

        #3 possible scenarios for popping
        if pos is None and current.next != None:    #1: user does not enter a position and there is more than one element
            for current in self:
                if current.next.next == None:   #interupts for loop, when a is current: 'a'->'b'->None
                    popped_item = current.next  #popped is 'b'
                    current.setNext(None)                                              #'a'->None
                    return popped_item          #return 'b'
                
        elif (pos is not None and pos != 0) and current.next != None:   #2: user enters a pos, and it is not the first element
            while pos_not_reached:
                if counter == (pos - 1):    #interupts while loop before the desired (for b entered: ['a']->'b')
                    popped_item = current.next      #popped is 'b'
                    if current.next.next == None:   #checks for: ['a'->'b'->None], i.e. if 'b' is the end of the list
                        current.setNext(None)       #['a'->None] cuts list
                    else:
                        current.setNext(current.next.next)  #['a'->'b'->'c']=>['a'->'c']
                    pos_not_reached = False         #flip flag
                    return popped_item              #return 'b'
                current = current.next      #iterate list
                counter += 1                #increment counter
        else:                           #3: the desired element is the first element
            popped_item = self.head
            self.head = current.next    #sets the new first element as the next element
            return popped_item          #['a'->'b']->['b'] or ['a'->None]->[None]

    def search(self, item):
        """Takes one positional argument as a new item. Iterates through the
        list until it finds the item. If the item is found, returns True.
        Else, returns False."""
        for current in self:        #iterates list
            if str(current) == str(item):   #interupts for loop when the item matches
                return True
            current = current.next
            
    def remove(self, item):
        """Takes one positional argument as a new item. Iterates through the
        list until it finds the item. If the item is found, it removes the item.
        Else, it removes nothing. Nothing is returned."""
        counter = 0
        
        for current in self:        #iterates list
            if str(current.next) == str(item):  #interupts for loop when: b = item, for ['a'->'b']
                if current.next.next == None:   #checks for: ['a'->'b'->None]
                    current.setNext(None)       #['a'->None]
                else:
                    current.setNext(current.next.next) #else: ['a'->'b'->'c']=>['a'->'c']
            elif str(current) == str(item):     #interupts for loop when: a = item
                self.head = current.next        #['a'->'b']->['b'] or ['a'->None]->[None] 
            counter += 1
