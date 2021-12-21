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

class OrderList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def size(self):
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.next
        return count

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

    def search(self, item):
        found = False
        stop = False
        current = self.head
        while current != None and not found and not stop:
            if item == current.data:
                found = True
            else:
                if item < current.data:
                    stop = True
                else:
                    current = current.next
        return found

    def add(self, item):
        stop = False
        previous = None
        current = self.head
        while current != None and not stop:
            if item < current.data:
                previous = current
                current = current.next
            else:
                stop = True

        temp = Node(item)
        if previous == None:
            self.head = temp
            temp.next = None
        else:
            temp.next = current
            previous.next = temp