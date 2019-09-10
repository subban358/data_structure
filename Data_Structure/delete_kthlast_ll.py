class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.start= None 

    def insert(self,value):
        node = Node(value)
        if self.start is None:
            self.start = node
        else:
            temp = self.start
            while temp.next:
                temp = temp.next
            temp.next = node         

    def show(self):
        if self.start is None:
            print("Empty !")
        else:
            temp = self.start
            while temp:
                print(temp.data,end=" ")
                temp = temp.next       

    def kth_last_Delete(self,pos):
        if self.start is None:
            print("Empty !")
        else:
            t1 = self.start
            t2 = self.start
            nxt = self.start.next
            prv = None
            c = 0
            while c<pos-1:
                t2 = t2.next
                c += 1
            while t2.next:
                prv = t1
                t1 = t1.next
                t2 = t2.next
                nxt = nxt.next
            prv.next =  nxt 


l = LinkedList()
l.insert(5)
l.insert(6)
l.insert(7)
l.insert(10)
l.insert(15)
l.show()      
print()
l.kth_last_Delete(4)    
print()
l.show()                 
