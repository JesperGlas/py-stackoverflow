from __future__ import annotations  # for type hints on self-defined classes
from typing import TypeVar          # for generic data type in list


T = TypeVar('T', int, str)

class LinkedItem:
    
    def __init__(self, data: T):
        self._previous: LinkedItem = None
        self._next: LinkedItem = None
        self._data: T = data

    def __str__(self) -> str:
        return str( self._data )

class LinkedList:

    def __init__(self):
        self._head: LinkedItem = None
        self._tail: LinkedItem = None
        self._length: int = 0
        
    def __len__(self) -> int:
        return self._length
    
    def __str__(self) -> str:
        res: str = "["
        if len(self) > 0:
            current: LinkedItem = self._head
            res += f"{current}"
            while (current := current._next) != None:
                res += f", {current}"
        res += "]"
        return res
        
    def append(self, data: T) -> None:
        if len(self) == 0:
            self._head = self._tail = LinkedItem(data)
        else:
            new_item = LinkedItem(data)     # create new item
            self._tail._next = new_item     # add after last item (tail)
            new_item._previous = self._tail # set tail as new items previos
            self._tail = new_item           # set tail as new item
        self._length += 1                   # increment list length

    def push(self, data: T) -> None:
        if len(self) == 0:
            self.append(data)
        else:
            new_item = LinkedItem(data)     # create new item
            self._head._previous = new_item # add before first item (head)
            new_item._next = self._head     # set head as new items next
            self._head = new_item           # set head as new item
        self._length += 1                   # increment list length

    def pop(self) -> T:
        res: T = None
        if len(self) > 0:
            if len(self)  == 1:
                res = self._head._data
                self._head = self._tail = None
            elif len(self) > 1:
                res = self._head._data
                self._head = self._head._next
            self._length -= 1 # decrement list length
        return res
    
if __name__ == '__main__':
    link = LinkedList()
    link.append("Hello")
    link.append("World")
    link.append(5)
    
    print(link.pop())
    
    link.push("Hello")
    
    print(link)