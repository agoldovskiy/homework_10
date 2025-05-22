class Node:
    def __init__(self, value, next, previous) -> None:
        """
        value: the value of a Node \n
        next: the next Node \n
        previous: the previous Node \n
        """
        self.value = value
        self.next = next
        self.previous = previous

class DoubleLinkedList:
    def __init__(self) -> None:
        """
        head: the first Node \n 
        tail: the last Node \n 
        length: the length of the DoubleLinkedList (whever if it is cycled or not) \n 
        cycle: False by default, if True - tail.next = head, head.previous = tail \n 
        """
        self.head = None
        self.tail = None
        self.length = 0
        self.cycle = False

    def printlist(self):
        current = self.head
        for i in range(self.length):
            if current.next != None:
                print (current.value, end=' <-> ')
            else:
                print (current.value)
            current = current.next

    def setCycle (self):
        self.cycle = True
        self.head.previous = self.tail
        self.tail.next = self.head

    def addfirst(self, value):
        if self.length == 0:
            newNode = Node(value, None, None)
            self.head = newNode
            self.tail = newNode
        else:
            if self.cycle == False:
                newNode = Node(value, next = self.head, previous = None)
                self.head.previous = newNode
                self.head = newNode
            else:
                newNode = Node(value, next = self.head, previous = self.tail)
                self.tail.next = newNode
                self.head.previous = newNode
                self.head = newNode
        self.length += 1

    def addlast(self, value):
        if self.length == 0:
            newNode = Node(value, None, None)
            self.head = newNode
            self.tail = newNode
        else:
            if self.cycle == False:
                newNode = Node(value, next = None, previous = self.tail)
                self.tail.next = newNode
                self.tail = newNode
            else:
                newNode = Node(value, next = self.head, previous = self.tail)
                self.tail.next = newNode
                self.head.previous = newNode
                self.tail = newNode
        self.length += 1

    def add (self, value, index):
        if self.length == 0:
            self.addfirst(value)
            return
        if index > self.length:
            self.addlast(value)
            return
        if index <= 0:
            self.addfirst(value)
            return
        current = self.head
        for i in range(index - 1):
            current = current.next
        newNode = Node(value, next = current.next, previous = current)
        current.next.previous = newNode
        current.next = newNode
        self.length += 1

    def delfirst (self):
        if self.length ==0:
            return
        self.length -= 1
        if self.head == self.tail:
            self.head = None
            self.tail == None
            return
        if self.cycle == False:
            self.head = self.head.next
            self.head.previous = None
        else:
            self.head = self.head.next
            self.head.previous = self.tail
            self.tail.next = self.head

    def dellast (self):
        if self.length == 0:
            return
        self.length -= 1
        if self.length == self.tail:
            self.head = None
            self.tail == None
            return
        if self.cycle == False:
            self.tail = self.tail.previous
            self.tail.next = None
        else:
            self.tail = self.tail.previous
            self.tail.next = self.head
            self.head.previous = self.tail


    def delete (self, index):
        if index > self.length:
            self.dellast()
            return
        if index <= 0:
            self.delfirst()
            return
        current = self.head
        for i in range(index):
            current = current.next
        current.previous.next = current.next
        current.next.previous = current.previous
        self.length -= 1

    def delvalue (self, value):
        current = self.head
        if current.value == value:
            self.delfirst()
        while current != self.tail:
                if current.value == value:
                    current.next.previous = current.previous
                    current.previous.next = current.next
                    self.length -= 1
                current = current.next
        if current.value == value:
            self.dellast()     

    def __iter__(self):
        current = self.head
        for i in range(self.length):
            yield current
            current = current.next

    def index (self, index):
        if self.cycle == True:
            self.__indexCycle(index)
        else:
            self.__indexNonCycle(index)


    def __indexNonCycle (self, index):
        current = self.head
        if index <= self.length:
            for i in range(index):
                current = current.next
            return current
        else:
            raise IndexError
        
    def __indexCycle (self, index):
        current = self.head
        for i in range(index):
            current = current.next
        return current

    def reverse (self):
        current = self.tail
        newlist = DoubleLinkedList()
        for i in range(self.length):
            newlist.addlast(current.value)
            current = current.previous
        if self.cycle == True:
            newlist.setCycle()
        return newlist


l = DoubleLinkedList()
l.addfirst(5)
l.addlast(10)
l.add(7, 1)
l.addfirst(1)
l.addlast(20)
l.add(15, 4)
l.printlist()
l.delfirst()
l.dellast()
l.delete(2)
l.printlist()
l.delvalue(15)
l.printlist()
x = l.reverse()
x.printlist()

#swagg