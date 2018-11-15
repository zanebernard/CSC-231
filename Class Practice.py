class XYcoord(object):
    
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __repr__(self):
        return '(' + str(self.__x) + ',' \
               + str(self.__y) + ')'
