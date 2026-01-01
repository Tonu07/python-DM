'''
import matplotlib.pyplot as plt

# Function to generate arithmetic sequence
def arithmetic_sequence(a1, d, n):
    return [a1 + i*d for i in range(n)]

# Function to generate geometric sequence
def geometric_sequence(a1, r, n):
    return [a1 * (r**i) for i in range(n)]
# Parameters
a1 = 2   # first term
d = 3    # common difference
r = 2    # common ratio
n = 10   # number of terms

# Generate sequences
arith_seq = arithmetic_sequence(a1, d, n)
geom_seq = geometric_sequence(a1, r, n)
terms = list(range(1, n+1))  # term numbers

# Plotting
plt.figure(figsize=(10,6))
plt.plot(terms, arith_seq, marker='o', linestyle='-', color='blue', label='Arithmetic Sequence')
plt.plot(terms, geom_seq, marker='s', linestyle='--', color='red', label='Geometric Sequence')
plt.title('Arithmetic and Geometric Sequences')
plt.xlabel('Term Number (n)')
plt.ylabel('Term Value')
plt.xticks(terms)
plt.grid(True)
plt.legend()
plt.show()
'''
import matplotlib.pyplot as plt
def arithmeticSeq(a,d,n):
    return [a+i*d for i in range(n)]
def geometricSeq(a,r,n):
    return [a*(r**i)for i in range(n)]
a=int(input("Enter the value of a:"))
r=int(input("Enetr the value of r:"))
d=int(input("Enter the value of d:"))
n=int(input("Enter the value of n:"))
aS=arithmeticSeq(a,d,n)
gs=geometricSeq(a,r,n)
terms=list(range(1, n+1))
print("The arithematic sequence=",aS)
plt.plot(terms,aS,marker='o',color='blue')
plt.plot(terms,gs,marker='o',color='red')
print("The geometrical sequence=",gs)
plt.title('Arithemetic and geometrical sequences')
plt.xlabel('Term Number(n)')
plt.ylabel('Term value')
plt.grid(True)
plt.show()