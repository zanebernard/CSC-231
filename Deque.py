class Deque:
    
    def __init__(self):
        """Initilizes Deque as a list. Accepts nothing. Returns nothing."""
        self.__deque = []

    def get_front(self):
        """Returns the front of the queue. Accepts nothing."""
        return self.__deque[0]

    def get_rear(self):
        """Returns the rear of the queue. Accepts nothing."""
        return self.__deque[len(self.__deque) - 1]

    def add_front(self, item):
        """Sets an item in the front of the queue. Accepts variable 'item'.
        Returns nothing."""
        if self.is_empty():
            self.__deque.append(item)
        else:
            self.__deque.insert(0, item)
        
    def add_rear(self, item):
        """Sets an item in the rear of the queue. Accepts variable 'item'.
        Returns nothing."""
        self.__deque.append(item)
        
    def remove_front(self):
        """Removes from the front of the queue. Accepts nothing. Returns
        front item."""
        front = self.get_front()
        self.__deque.remove(front)
        return front
        
    def remove_rear(self):
        """Removes from the rear of the queue. Accepts nothing. Returns
        rear item."""
        rear = self.get_rear()
        self.__deque.remove(rear)
        return rear
        
    def is_empty(self):
        """Checks if the deque is empty. Accepts nothing. Returns True if queue
        is empty. Otherwise, returns False."""
        if len(self.__deque) == 0:
            return True
        else:
            return False

    def size(self):
        """Returns the size of the queue. Accepts nothing."""
        return int(len(self.__deque))
