'''
(b) (A ∪ B)′ = A′ ∩ B′
'''
U = {1, 2, 3, 4, 5, 6}
A = {1, 2, 3}
B = {3, 4, 5}
LHS=U.difference(A.union(B))
RHS=(U.difference(A)).intersection(U.difference(B))
if(LHS==RHS):
    print("True")
else:
    print("False")
    