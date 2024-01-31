n = 121
p = n
total = 0
while n != 0:
    x = n % 10
    n = n // 10
    total = total*10 + x
if total == p:
    print("true")
else:
    print("false")
