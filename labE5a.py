
#Derive a formula for the n th term and sum of a geometric progression using code verification.
def geo(a,r,n):
    return [a*(r**i) for i in range(n) ]
def nTerms(a,r,n):
    return a*r**(n-1)
def gsum(a,r,n):
    if(r==1):
        return a*n
    else:
        return a*(r**n-1)/(r-1)
a=int(input("Enter the value of a:"))
r=int(input("Enter the value of r:"))
n=int(input("Enter the value of n: "))
sequence=geo(a,r,n)
print("sequence :",sequence)
nth=nTerms(a,r,n)
print("n th terms : ",nth)
s=gsum(a,r,n)
print("The sum of the geometric progression : ",s)
