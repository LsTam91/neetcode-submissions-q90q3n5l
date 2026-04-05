class LinkedList:
    
    def __init__(self):
        self.linkedlist = []

    
    def get(self, index: int) -> int:
        if index >= len(self.linkedlist):
            return -1
        else:
            return self.linkedlist[index]

    def insertHead(self, val: int) -> None:
        self.linkedlist = [val] + self.linkedlist

    def insertTail(self, val: int) -> None:
        self.linkedlist.append(val)

    def remove(self, index: int) -> bool:
        if index >= len(self.linkedlist):
            return False
        self.linkedlist = self.linkedlist[:index] + self.linkedlist[index+1:]
        return True

    def getValues(self) -> List[int]:
        return self.linkedlist
        
