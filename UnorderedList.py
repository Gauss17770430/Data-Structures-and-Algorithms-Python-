class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next
    
    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class UnorderedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        temp = Node(item)
        temp.next = self.head
        self.head = temp

    def size(self):
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.next
        return count

    def search(self, item):
        found = False
        current = self.head
        while current != None and not found:
            if current.data == item:
                found = True
            else:
                current = current.next
        return found

    def remove(self, item):
        previous = None
        current = self.head
        found = False
        while current != None and not found:
            if current.data == item:
                found = True
            else:
                previous = current
                current = current.next
        
        if found:
            if previous == None:
                self.head = None
            else:
                previous.next = current.next

if __name__ == '__main__':
    temp = Node(93)
    print(temp.getData())

    mylist = UnorderedList()
    print(mylist.head)