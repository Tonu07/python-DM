#Implement a program to verify ¬(∀xP(x)) ≡ ∃x(¬P(x)).
def negate_forall(domain,P):
    return any(not P(x) for x in domain)
def exists_negate(domain,P):
    return any((not P(x)) for x in domain)
P=lambda x: x%2==0
domain=list(range(1,10))
left_side=negate_forall(domain,P)
right_side=exists_negate(domain,P)
print("Equivalence?:",left_side==right_side)