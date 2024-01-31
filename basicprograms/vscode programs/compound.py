def a(p, t, r):
    return p*(1+r/100)**t
p = float(input("enter the principle value: "))
t = float(input("enter the time taken:  "))
r = float(input("enter the rate:  "))
a = p*(1+r/100)**t
compound_inerest = a - p
print("amount is ", a)
print("compound interest is", compound_inerest) 