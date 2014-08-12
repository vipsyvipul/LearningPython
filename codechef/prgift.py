def main():
	t = int(input())
	while t >= 1 and t <= 10:
		first = [int(x) for x in input().split()]
		n,k = map(int, first)
		if n >= 1 and n <= 50:
			arr = [int(x) for x in input().split()]
			if len(arr) == n:
				count = 0
				for x in arr:
					if x%2 == 0:
						count += 1
				if k == 0:
					if count <= n:
						print("YES")
					else:
						print("NO")
				else:
					if count >= k:
						print("YES")
					else:
						print("NO")
		t -= 1

if __name__ == "__main__": main()
