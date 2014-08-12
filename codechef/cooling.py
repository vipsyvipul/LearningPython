def main():
	t = int(input())
	while t>0 and t <= 30:
		n = int(input())
		if n > 0 and n <= 30:
			piewt = sorted([int(x) for x in input().split()])
			rackwt = sorted([int(x) for x in input().split()])
			if len(piewt) == n and len(rackwt) == n:
				i = 0
				j = 0
				max1 = 0
				while i < n and j < n:
					if piewt[i] <= rackwt[j]:
						max1 += 1
						i += 1
					j += 1
				print(max1)
				t -= 1

if __name__ == "__main__":
	main()
