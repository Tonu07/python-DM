#Modify the Fibonacci function to compute Lucas numbers.
'''
# Recursive implementation of Lucas numbers
def lucas_recursive(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas_recursive(n-1) + lucas_recursive(n-2)

# Iterative implementation of Lucas numbers
def lucas_iterative(n):
    if n == 0:
        return [2]
    elif n == 1:
        return [2, 1]
    
    seq = [2, 1]
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq[:n]

# Number of terms
n = 5

# Compute Lucas numbers
lucas_recursive_seq = [lucas_recursive(i) for i in range(n)]
lucas_iterative_seq = lucas_iterative(n)

# Print results
print("Lucas numbers (recursive):", lucas_recursive_seq)
print("Lucas numbers (iterative):", lucas_iterative_seq)
'''
def locus(n):
    if(n==1):
        return 2
    elif(n==2):
        return 1
    else:
         return locus(n-1)+locus(n-2) 
n=int(input("Enter the value of n:"))
l=locus(n)
print("n th locus number=",l)