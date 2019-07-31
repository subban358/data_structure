class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.start = None

    def add_lst(self,value):
        new_node = Node(value)  
        if self.start is None:
            self.start = new_node
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node     

    def add_begining(self,data):
    	new_node = Node(data)
    	new_node.next = self.start
    	self.start = new_node    

    def add_location(self,pos,data):
    	new_node = Node(data)	  
    	if self.start != None and pos is 0:
    		self.add_begining(data)
    				
    	else:
    		prv = None
    		temp = self.start
    		count=0
    		while temp and count is not pos:
    			prv = temp
    			temp = temp.next
    			count+=1
    		if temp is None:
    			print("The location you entered is out of range !")
    			return
    		prv.next = new_node
    		new_node.next = temp
    		return			     

    def add_after_node(self,prv_node,data):
    	new_node = Node(data)
    	temp = self.start
    	while temp and temp.data is not prv_node:
    		temp = temp.next	
    	if not temp:
    		print("Previous Node not found !")
    		return
    	new_node.next = temp.next
    	temp.next = new_node
    			
    def delete_first(self):
        if self.start is None:
            print("Empty !")
            return
        else:
            self.start = self.start.next
            return    
    
    def delete_value(self,key):
        if self.start is None:
            print ("List is empty !")
        elif self.start != None and self.start.data == key:
            self.start = self.start.next
        else:
            temp = self.start
            prv = None
            while temp and temp.data is not key:
                prv = temp
                temp = temp.next
            if temp is None:
                print("\n%d is not present in the List !" % key)
                return    
            prv.next = temp.next 
            temp = None     
    
    def delete_pos(self,pos):
        if self.start is None:
            print ("List is empty !")
        elif pos is 0:
            self.start = self.start.next
        else:
            temp = self.start
            prv = None
            count = 0
            while temp and count is not pos:
                prv = temp
                temp = temp.next
                count+=1
            if temp is None:
                print("\n%d is not present in the List !" % key)
                return    
            else:
                prv.next = temp.next    
                temp = None                 

    def show(self):
        if self.start is None:
            print("Empty !")
        else:
            temp = self.start
            while temp is not None:
                print(temp.data,end=" ")
                temp = temp.next

    def delete_last(self):
    	if self.start is None:
    		print("List is Empty !")
    		return
    	else:
    		if self.start.next is None:
    			self.start = None
    			return
    		temp = self.start	
    		while temp.next.next:
    			temp = temp.next
    		temp.next = None
    		return		            

    def length(self):
    	count = 0
    	temp = self.start
    	while temp:
    		temp = temp.next
    		count+=1
    	print("\nlength is: %d" % count)	
    	return count		

    def reverse(self):
    	prv = None
    	temp = self.start
    	while temp:
    		nxt = temp.next
    		temp.next = prv 
    		prv = temp
    		temp = nxt	
    	self.start = prv	

if __name__ == '__main__':
    l = LinkedList()
    l.add_lst(5)
    l.add_lst(10)
    l.add_begining(1)
    print()
    l.show()
    print()
    l.reverse()
    print()
    l.show()
    input()