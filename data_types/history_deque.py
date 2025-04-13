#swaagg style
from termcolor import colored 
from datetime import datetime
class Node():
    """
    Basic 'Node' class used in 'History' class as main data structure (n. - action)\n
    next: next action
    prev: previous action
    action_id: action id (actions are consecutive, counts as an index)
    timestamp: time of action cretion
    username: creator of action
    actiontype: type of action (ex. - 'fill')
    """
    def __init__(self, next, prev, actionid, timestamp, username, actiontype) -> None:
        self.next = next
        self.prev = prev
        self.action_id = actionid
        self.timestamp = timestamp
        self.username = username
        self.actiontype = actiontype

    def __str__ (self):
        return (f"{self.action_id} - {self.timestamp} - {self.actiontype} - {self.username}")
    
class History():
    """
    History class for managing paths of certain actions\n
    Actions are 'Node' objects\n
    head: first action
    tail: last action
    current: current action
    actions_map: dict of all maps (action_id: 'Node' object)
    """
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.current = None
        self.actions_map = {}

    def add_action (self, timestamp, username, actiontype):
        if self.head == None:
            newNode = Node(next=None, prev=None, actionid=1, timestamp=timestamp, actiontype=actiontype, username=username)
            self.actions_map[newNode.action_id] = newNode
            self.head = newNode
            self.tail = newNode
            self.current = newNode
        else:
            newNode = Node(next=None, prev=self.current, actionid=self.current.action_id+1, timestamp=timestamp, username=username, actiontype=actiontype)
            self.current.next = newNode
            if self.current != self.tail:
                deletion = self.current.action_id + 1
                while deletion:
                    try:
                        del self.actions_map[deletion]
                        deletion += 1
                    except KeyError:
                        deletion = None
            self.actions_map[newNode.action_id] = newNode
            self.tail = newNode
            self.current = self.tail

    def undo (self):
        if self.current != None:
            self.current = self.current.prev

    def redo (self):
        if self.current != None:
            self.current = self.current.next

    def findAction (self, id):
        return self.actions_map[id]
    
    def remove_action (self, id):
        nodeDeletion: 'Node' = self.actions_map[id]
        print(nodeDeletion)
        if nodeDeletion.prev != None:
            nodeDeletion.prev.next = nodeDeletion.next
        if nodeDeletion.next != None:
            nodeDeletion.next.prev = nodeDeletion.prev
        del self.actions_map[id]
        deletion = id+1
        while deletion:
            try:
                self.actions_map[deletion].action_id -= 1
                deletion += 1
            except KeyError:
                deletion = None
        newActions = {}
        for key in self.actions_map:
            newActions[self.actions_map[key].action_id] = self.actions_map[key]
        self.actions_map = newActions

    def filter_and_remove (self, actiontype):
        index = 1
        while index:
            try:
                if self.actions_map[index].actiontype == actiontype:
                    self.remove_action(index)
                index += 1
            except KeyError:
                index = None

    def __iter__ (self):
        for key, value in self.actions_map.items():
            yield value # self.actions_map[key]
            
    def getactions (self):
        color = 'green'
        for i in self:
            print (colored(i, color))
            if i == self.current:
                color = 'grey'

hist1 = History()
hist1.add_action(datetime.now(), 'user1', 'fill')
hist1.add_action(datetime.now(), 'user2', 'add rectangle')
hist1.add_action(datetime.now(), 'user2', 'fill')
hist1.add_action(datetime.now(), 'user1', 'draw line')
hist1.remove_action(2)
print ('\n')
hist1.undo()
hist1.redo()
hist1.undo()
hist1.add_action(datetime.now(), 1, 'add rectangle')
hist1.getactions()
