def main():
	t = int(input())
	while t>0:
		num = int(input())
		fact = 1
		for i in range(1,num+1):
			fact *= i
		print(fact)
		t -= 1

if __name__ == "__main__":
	main()
