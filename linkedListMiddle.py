class Node:
	def __init__(self, val):
		self.val = val
		self.next = None
		
class LinkedList:
	def __init__(self):
		self.head = None
		
	def insert_node(self, val):
		newNode = Node(val)
		if self.head == None:
			self.head = newNode
		else:
			temp = self.head
			while(temp.next):
				temp = temp.next
				
			temp.next = newNode
		
	def print_list(self):
		temp = self.head
		while(temp):
			print(temp.val, end=' ')
			temp = temp.next
			
	def divideMiddle(self):
		if self.head== None:
			return None
	
		if self.head.next == None:
			return None

		slow = self.head
		fast = self.head
		while(fast!= None and fast.next!= None):
			slow = slow.next
			fast = fast.next.next
		return (slow.val)
		
	def sortList(self):
		self.head = self.divideRecursive(self.head)

	def divideRecursive(self, head):
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
		
		h1 = self.divideRecursive(head)
		h2 = self.divideRecursive(slow)
		return(self.mergeRecursive(h1,h2))

	def mergeRecursive(self, h1, h2):
		if h1 == None:
			return h2
		if h2 == None:
			return h1
		if h1.val < h2.val:
			h1.next = self.mergeRecursive(h1.next, h2)
			return h1
		else:
			h2.next = self.mergeRecursive(h1, h2.next)
			return h2
		
		

				
myList = LinkedList()
myList.insert_node(10)
myList.insert_node(2)
myList.insert_node(-3)
myList.insert_node(4)
myList.insert_node(15)
myList.insert_node(6)
myList.insert_node(7)
myList.insert_node(-8)
myList.print_list()
print('\tmiddle: ', myList.divideMiddle())

myList.insert_node(9)
myList.print_list()
print('\tmiddle: ', myList.divideMiddle())

myList.sortList()
myList.print_list()
