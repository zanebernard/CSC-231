class Queue:
    
    def __init__(self):
        """Initilizes Queue as a list. Accepts nothing. Returns nothing."""
        self.__queue = []

    def get_front(self):
        """Returns the front of the queue. Accepts nothing."""
        return self.__queue[len(self.__queue) - 1]

    def get_rear(self):
        """Returns the rear of the queue. Accepts nothing."""
        return self.__queue[0]

    def enqueue(self, item):
        """Sets an item in the back of the queue. Accepts variable 'item'.
        Returns nothing."""
        if self.is_empty():
            self.__queue.append(item)
        else:
            self.__queue.insert(0, item)
        
    def dequeue(self):
        """Dequeues from the front of the queue. Accepts nothing. Returns
        front item that was dequeued."""
        front = self.get_front()
        self.__queue.remove(front)
        return front
        
    def is_empty(self):
        """Checks if the queue is empty. Accepts nothing. Returns True if queue
        is empty. Otherwise, returns False."""
        if self.size() == 0:
            return True
        else:
            return False

    def size(self):
        """Returns the size of the queue. Accepts nothing."""
        return int(len(self.__queue))
