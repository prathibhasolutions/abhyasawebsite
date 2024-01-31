def factorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else: 
         fact = 1
         while(n > 1):
            
             n -= 1
             fact *= 1
             return fact
number=5
print("factorial of number is" ,factorial(number))         
