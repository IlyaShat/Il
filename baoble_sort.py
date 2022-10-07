a=[9,8,7,6,5,4,3,1,2]
for i in range(len(a)-1):
    for i in range(len(a)-i-1):
        if a[i]>a[i+1]:
            a[i],a[i+1]=a[i+1],a[i]
            
print(a)