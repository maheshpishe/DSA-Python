class node:
	def __init__(self,data):
		self.data=data
		self.next=None

class linkedlist:
	def __init__(self):
		self.head=None

	def insert_at_end(self,data):
		newnode=node(data)
		if self.head is None:
			self.head=newnode
		else:
			cur=self.head
			while cur.next is not None:
				cur=cur.next
			cur.next=newnode

	def gethead(self):
		return (self.head)

	def printlist(self):
		if self.head is None:
			print("empty list")
		else:
			cur=self.head
			while cur:
				print(cur.data,end=" -->")
				cur=cur.next

	def insert_at_beg(self,data):
		node1=node(data)
		if self.head is None:
			self.head=node1
		else:
			node1.next=self.head
			self.head=node1

	def findlength(self):
		cnt=0
		if self.head is None:
			print(0)
		else:
			cur=self.head
			while cur:
				cnt+=1
				cur=cur.next
		print("\n")	
		print(cnt)	

	def delete_at_beginning(self):
		if self.head is None:
			print("no elements")
		else:
			self.head=self.head.next
	
	def insert_at_position(self,data,pos):
		node1=node(data)
		if self.head is None:
			self.head=node1
		else:
			
			cur=self.head
			for i in range(pos-2):
				cur=cur.next
			node1.next=cur.next
			cur.next=node1

	def del_at_position(self,pos):
		if self.head is None:
			print("empty list")
		cur=self.head
		for i in range(pos-2):
			cur=cur.next
		cur.next=cur.next.next

	def del_with_val(self,val):
		if self.head is None:
			print("empty list")
		cur=self.head
		while cur.next:
			if cur.next.data==val:
				cur.next=cur.next.next
			cur=cur.next

	def reverse(self):
		prev=None
		cur=self.head
		
		while cur:
			nxt=cur.next
			cur.next=prev
			prev=cur
			cur=nxt
		self.head=prev

l=linkedlist()
l.insert_at_beg(1)
l.insert_at_beg(2)
l.insert_at_beg(3)
l.insert_at_position(9,2)
l.del_at_position(2)
l.del_with_val(4)
l.reverse()
l.insert_at_end(11)
l.printlist()