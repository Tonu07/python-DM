#set
'''
Verify the following identities using Python:
(a) A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)
(b) (A ∪ B)
′ = A′ ∩ B′
'''
A={1,2,3}
B={3,4,5}
C={9}
LHS=A.intersection(B.union(C))
RHS=(A.intersection (B)).union(A.intersection (C))
if (LHS==RHS):
    print("True")
else:
    print("False")
