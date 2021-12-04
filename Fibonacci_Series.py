def fib(n):
    if n < 0 or n == 0:
      return -1
    if n == 1:
      return 0
    if n == 2:
      return 1  
    a = 0
    b = 1
    if n >= 3:
      for i in range(n-2):
        sum = a + b
        a = b
        b = sum
    return sum

print("Fibonacci Series")
print("This program returns the n-th Fibonacci number")

num = (int(input("Put the number: ")))

print(fib(num))