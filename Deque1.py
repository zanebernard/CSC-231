class Deque:
    def __init__(self):
        self.__deque = []

    def add_front(self, item):
        if self.is_empty:
            self.__deque.append(item)
            
        self.__deque[0] = item
        
    def add_rear(self):
        self.__deque.append(item)
        
    def remove_front(self):
        del self.__deque
    def remove_rear(self):

    def is_empty(self):
        if len(self.__queue) == 0:
            return True
        else:
            return False

    def size(self):
        return int(len(self.__queue))
