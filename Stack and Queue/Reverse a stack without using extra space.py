class StackNode:
	def __init__(self, data):
		self.data = data
		self.next = None

class Stack:
	def __init__(self):
		self.top = None

	def push(self, data):
		if (self.top == None):
			self.top = StackNode(data)
			return
		s = StackNode(data)
		s.next = self.top
		self.top = s
	
	def pop(self):
		s = self.top
		self.top = self.top.next
		return s

	def display(self):
		s = self.top
		while (s != None):
			print(s.data, end=' ')
			s = s.next

	def reverse(self):
		prev = self.top
		cur = self.top
		cur = cur.next
		succ = None
		prev.next = None
		while (cur != None):
			succ = cur.next
			cur.next = prev
			prev = cur
			cur = succ
		self.top = prev

s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)

print("Original Stack :")
s.display()
print()

s.reverse()
print("Reversed Stack :")
s.display()
