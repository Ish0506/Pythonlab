#CODE:
t=int(input("Enter No of test cases: "))
for i in range(t):
    list2 = input().split()
    m=int(list2[0])
    n=int(list2[1])
    list1=list(range(2,n+1))
    for k in list1:
        for l in range(k**2,n+1):
            if l%k==0:
                list1.remove(l)
            else:
                continue
    for k in list1:
        if k>=m and k<=n:
            print(k,end=" ")
    print()
