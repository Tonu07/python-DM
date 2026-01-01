#Write a function to compute an = 3an−1 − 2 with a0 = 1.
'''
def sequence_recursive(n):
    if n==0:
        return 1
    else:
        return 3*sequence_recursive(n-1)-2
def sequence_iterative(n):
    seq=[1]  
    for i in range(1,n+1):
        next_term=3*seq[i-1]-2
        seq.append(next_term)
    return seq

# Number of terms
n = 10

# Compute sequence
seq_recursive = [sequence_recursive(i) for i in range(n+1)]
seq_iterative = sequence_iterative(n)

# Print results
print("Sequence (recursive):", seq_recursive)
print("Sequence (iterative):", seq_iterative)
'''
def seq(n):
    if(n==0):
        return 1
    else:
        return 3*seq(n-1)-2
n=int(input("enter the value of n:"))
s=seq(n)
print(s)
