t = int(input())
while t>0:
	expr = list(input())
	op = ['+','-','/','*','^']
	oplist = []
	output = ''
	for char in expr:
		if char in op:
			oplist.append(char)
		elif char == '(':
			continue
		elif char == ')':
			output += oplist.pop()
		else:
			output += char
	t -=1
