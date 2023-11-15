class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self,data):
        newNode = Node(data,self.head)      # create a new node with next pointing to head
        self.head = newNode                 # make the new node as head
        
    def insert_at_end(self,data):
        if self.head is None:               # if list is empty make the new node as head
            self.head = Node(data,None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)          # traverse till the end and add the node
    
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            count += 1
        return count
    
    def remove_at(self,index):
        if index<0 or index>= self.get_length():
            raise Exception("Invalid index")
        if index == 0:
            self.head = self.head.next
        
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next    # disconnect the middle node between previous and next node
                return                                                  
            itr = itr.next
            count+=1
            
    def insert_at(self,index,data):
        if index<0 or index>= self.get_length():
            raise Exception("Invalid index")
        if index == 0:
            self.insert_at_begining(data)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(data,itr.next)
                itr.next = node
                break
            itr = itr.next
            count +=1
        
    def printlist(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        while itr:
            print(itr.data,end="-->")
            itr = itr.next
    
if __name__ == '__main__':
    ll = SingleLinkedList()
    ll.insert_at_begining(5)
    ll.insert_at_begining(6)
    ll.insert_at_begining(7)
    ll.insert_at_begining(8)
    ll.insert_at_begining(9)
    
    ll.insert_at_end(10)
    
    ll.printlist()
    print("\nLength = ",ll.get_length())
    ll.remove_at(2)
    print()
    print(ll.printlist())
    
    ll.insert_at(3,12)
    print(ll.printlist())