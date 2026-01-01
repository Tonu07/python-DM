#lab 5
'''
01 no
# Function to generate geometric sequence
def geometric_sequence(a1, r, n):
    return [a1 * (r**i) for i in range(n)]

# Function to calculate n-th term
def nth_term_gp(a1, r, n):
    return a1 * (r**(n-1))

# Function to calculate sum of first n terms
def sum_gp(a1, r, n):
    if r == 1:
        return a1 * n
    else:
        return a1 * (r**n - 1) / (r - 1)

# Example
a1 = 2   # first term
r = 2    # common ratio
n = 5    # number of terms

# Generate sequence
sequence = geometric_sequence(a1, r, n)
nth_term = nth_term_gp(a1, r, n)
sum_of_terms = sum_gp(a1, r, n)

print("Geometric Sequence:", sequence)
print(f"{n}th term of GP:", nth_term)
print(f"Sum of first {n} terms of GP:", sum_of_terms)

'''
'''
2 no
# Recursive implementation
def sequence_recursive(n):
    if n == 0:
        return 1
    else:
        return 3 * sequence_recursive(n-1) - 2

# Iterative implementation
def sequence_iterative(n):
    seq = [1]  # a0 = 1
    for i in range(1, n+1):
        next_term = 3 * seq[i-1] - 2
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
'''
3 no
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
n = 10

# Compute Lucas numbers
lucas_recursive_seq = [lucas_recursive(i) for i in range(n)]
lucas_iterative_seq = lucas_iterative(n)

# Print results
print("Lucas numbers (recursive):", lucas_recursive_seq)
print("Lucas numbers (iterative):", lucas_iterative_seq)

'''
'''
4 no
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