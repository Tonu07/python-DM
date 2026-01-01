#Write a program to check whether (p ∨ q) ∧ (¬p ∨ q) is equivalent to q.
import itertools
def evaluate_expression(p,q):
    return (p or q)and((not p)or q)
values=[True,False]
print("p\tq\t(p∨q)∧(¬p∨q) \tq\t\tEquivalent?")
print("-"*60)
for p in values:
    for q in values:
     result=evaluate_expression(p,q)
     equivalent=result==q
     print(f"{p}\t{q}\t{result}\t\t{q}\t\t{equivalent}")
