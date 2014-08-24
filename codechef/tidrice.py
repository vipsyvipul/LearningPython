def main():
	t = int(input())
	while t>0 and t<=20:
		votes = int(input())
		d = {}
		for i in range(votes):
			voteValue = input().split()
			d[voteValue[0]] = voteValue[1]
		count = 0
		for value in d:
			if d[value] == '+':
				count += 1
			else:
				count -= 1
		print(count)
		t -= 1
if __name__ == '__main__': main()
