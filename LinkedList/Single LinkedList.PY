class Node:
    def __init__(self,dataval=None):
        self.dataval = dataval
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.headval = None

list1 = SingleLinkedList()
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("wed")

list1.headval.next = e2
e2.next = e3       
        
thisvalue = list1.headval
while thisvalue:
    print(thisvalue.dataval)
    thisvalue = thisvalue.next