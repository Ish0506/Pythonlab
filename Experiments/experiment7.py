'''Given a non negative integer A, print all the pairs of integers(a,b) such that
a and b are positive integers
a<=b and
a^2 + b^2 = A
0 <= A
A<=1000

Problem statement is pretty clear, We just need to find such pairs who satisfies the Pythagoras theorem up-to that number.
The idea is to put two nested loops and print those numbers whose squared sum is equal to the given number.'''

#code

def sumSquare(n): 
c=0
for i in range(1,n+1):
    for j in range(1,n+1): 
        if(i*i+j*j==n and i<=j):
            print("{},{}".format(i,j)) 
            c=1
if(c==0):
    return False 
return True

n=int(input("Enter a number:")) 
if(sumSquare(n)==False):
    print("No such Pair exists")
