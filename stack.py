stack = Stack()
stack.push('4')
stack.push('3')
stack.push('2')
n = stack.pop()
m = stack.pop()
l = stack.pop()
stack.push(m)
stack.push(l)
stack.push(m)
l = stack.pop()
while not stack.is_empty():
	print(stack.pop(), end='')