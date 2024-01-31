def factorial(n):
    x = 1
    for i in range(1,n+1):
        x *= i
    return x
num = 5
print("factorial of 5 is" , factorial(num) )   