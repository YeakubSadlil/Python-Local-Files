class Daynames:
    def __init__(self,dataval=None):
        self.dataval = dataval
        self.next = None
        
e1= Daynames('Mon')
e2 = Daynames('Tue')
e3 = Daynames('Wed')
e4 = Daynames("Thu")

e1.next = e2
e2.next = e3
e3.next = e4

thisvalue = e1

while thisvalue:
    print(thisvalue.dataval)
    thisvalue = thisvalue.next