list=[34,56,67,78]
new_list=[]
j=0
for i in range(1,len(list)):
     j+=list[i]
     new_list.append(j)
print("length of list" , new_list)     