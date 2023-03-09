def fib(n):
	a, b = 0, 1
	result = []
	while a < n:
		result.append(a)
		a, b = b, a + b
	return result

#the condition below makes a Python module to be an executable script
if __name__ == "__main__":
	import sys
	fib(int(sys.argv[1]))
