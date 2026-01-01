def imp(p,q):
    return (not p)or q
def ModP(p,q):
    return p and imp(p,q)
def ModT(p,q):
    return (not q)and imp(p,q)
p=True
q=True
print("Modus ponens result=",ModP(p,q))
print("Modus Tollens result=",ModT(p,q))
#p,q using propositional logic try

