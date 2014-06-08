from linked_list import l_list as ll


class EmptyStackError(Exception):
    """The basic format of this is from a stackoverflow thread"""

    def __init__(self, message="The stack is empty."):
        Exception.__init__(self, message)


class Stack(object):
    """  The stack class implements a first in first out data structure, a
    stack.  This implementation uses a linked list.
    """
    def __init__(self):
        """intialize the stack with no contents"""
        self._ll = ll()

    def push(self, item):
        """pushes an item onto the stack"""
        self._ll.insert(item)

    def pop(self):
        """pop an item from the stack and return it"""
        if self._ll.size() < 1:
            raise EmptyStackError()
        else:
            return self._ll.pop()
