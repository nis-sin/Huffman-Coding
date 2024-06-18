class Node:
    def __init__(self, value: int, priority: int, isInternal: bool = False):
        self.__value: int = value
        self.__priority: int = priority     # Priority == frequency of the character
        self.__left: Node = None
        self.__right: Node = None
        self.__isInternal: bool = isInternal # True if the node is an internal node, False otherwise
    
    def getValue(self) -> int:
        return self.__value
    
    def getPriority(self) -> int:
        return self.__priority

    def setLeft(self, left) -> None:
        self.__left = left
    
    def setRight(self, right) -> None:
        self.__right = right
    
    def getLeft(self):
        return self.__left
    
    def getRight(self):
        return self.__right
    
    def isInternal(self) -> bool:
        return self.__isInternal


class Queue:
    def __init__(self):
        self.__queue: list[Node] = []
        self.__length: int = 0
    
    def enqueue(self, node: Node) -> None:
        self.__queue.append(node)
        self.incrementLength()

    def dequeue(self) -> Node:
        if self.getLength() == 0:
            print("Queue is empty")
            return None
        self.decrementLength()
        return self.__queue.pop(0)
    
    def getLength(self) -> int:
        return self.__length

    def getQueue(self) -> list[Node]:
        return self.__queue

    def incrementLength(self):
        self.__length+=1

    def decrementLength(self):
        self.__length-=1


class PriorityQueue(Queue):
    def __init__(self):
        super().__init__()

    def enqueue(self, node: Node) -> None:
        self.incrementLength()
        for i, n in enumerate(self.getQueue()):
            if n.getPriority() > node.getPriority():
                self.getQueue().insert(i, node)
                return
        self.getQueue().append(node)