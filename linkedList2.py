# This code, sorts a linked list using merge sort where items in odd positions are sorted ascendingly
# and items in even poistions are sorted descendingly

class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None	
	# Insert a node at the end of a linekd list
	def insertNode(self,val):
		newNode = Node(val)
		if self.head == None:
			self.head = newNode
		else:
			temp = self.head
			while(temp.next != None):
				temp = temp.next
			temp.next = newNode		
	def returnHead(self):
		return self.head

			
def divideInHalf(head):
	if self.head == None or self.head.next == None:
		return (self.head, None)
			
	slow = self.head
	fast = self.head
	pre = slow	
	while(fast != None and fast.next != None):
		pre = slow
		slow = slow.next
		fast = fast.next.next
			
	pre.next = None	
	return(self.head, slow)
		
def splitList(head):  # split into two lists where each contains every other item
	if head == None or head.next == None:
		return (head, None)
			
	head1 = temp1 = head
	head2 = temp2 = head.next
		
	while(temp2.next):
		temp1.next = temp2.next
		temp1 = temp1.next
		if temp1.next:
			temp2.next = temp1.next
			temp2 = temp2.next
		else:
			break
				
	temp1.next = None
	temp2.next = None	
		
	return head1, head2
		
		
def printList(head):
	while(head):
		print(head.val, end = ' ')
		head = head.next
	print('\n')
	
	
def sortList(head, reverse):
	head = divideRecursive(head, reverse)
	return head

def divideRecursive(head, reverse):
	
	if head == None:
		return head
	
	if head.next == None:
		return head
	
	slow = head
	fast = head
	pre = head
	while(fast!= None and fast.next!= None):
		pre = slow
		slow = slow.next
		fast = fast.next.next
	
	pre.next = None
		
	h1 = divideRecursive(head,reverse)
	h2 = divideRecursive(slow,reverse)
	if reverse:
		return(mergeRecursiveDes(h1,h2))
	else:
		return(mergeRecursiveAsc(h1,h2))
	
def mergeRecursiveAsc(h1,h2):
	if h1 == None:
		return h2
	if h2 == None:
		return h1
		
	if h1.val < h2.val:
		h1.next =  mergeRecursiveAsc(h1.next, h2)
		return h1
	else:
		h2.next = mergeRecursiveAsc(h1, h2.next)
		return h2
		
def mergeRecursiveDes(h1,h2):
	if h1 == None:
		return h2
	if h2 == None:
		return h1
		
	if h1.val > h2.val:
		h1.next =  mergeRecursiveDes(h1.next, h2)
		return h1
	else:
		h2.next = mergeRecursiveDes(h1, h2.next)
		return h2
		
	
def mergeTwoLinkedList(h1,h2):
	if h1 == None:
		return h2
	if h2 == None:
		return h1
	h1.next = mergeTwoLinkedList(h2, h1.next)
	return h1
	
		
	
llist = LinkedList() 
llist.insertNode(10) 
llist.insertNode(40) 
llist.insertNode(67) 
llist.insertNode(30) 
llist.insertNode(89) 
llist.insertNode(8) 
llist.insertNode(53) 
llist.insertNode(12)
head = llist.returnHead()
printList(head)

#head1, head2 = divideInHalf(head)
#printList(head1)
#printList(head2)

head1, head2 = splitList(head)
printList(head1)
printList(head2)


printList(sortList(head1, False))
printList(sortList(head2, True))
printList(mergeTwoLinkedList(head1,head2))