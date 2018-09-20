## This code has two functionalities:
- First, we divide a linked list in half by using two pointers
	- While the slow pointer takes one step, the fast pointer takes two steps. By the time that fast pointer reaches to the end of the linked list, the slow one reaches to the middle of the list. It returns the pointer to the second half of the link. 
	- We have to also separate the first half from the second half. 
- Second, we sort the linked list using merge sort with constant space.
