# code
def sumSquare(n): 
c=0
for i in range(1,n+1):
    for j in range(1,n+1): 
    if(i*i+j*j==n and i<=j):
print("{},{}".format(i,j)) c=1
if(c==0):
return False return True

n=int(input("Enter a number:")) if(sumSquare(n)==False):
print("No such Pair exists")
