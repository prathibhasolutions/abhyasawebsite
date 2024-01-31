def si(p,t,r): a(si,p)
    return (p*t*r)/100,(si+p)
p = float(input("enter the principle"))
t = float(input("enter the  time period"))
r = float(input("enter the rate"))
simple_interest=(p*t*r)/100
print("simple interest for amount" , simple_interest)
amount = si + p
print("total amount with interest" , amount)