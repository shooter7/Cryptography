plan=raw_input("enter plan text: ")
c=0;
a=[0]*len(plan)
for i in plan:
    n=ord(i)
    a[c]=n;
    c+=1
print a

for i in a:
    n=chr(i)
    print(n)
