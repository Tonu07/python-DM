#Construct the truth table for (p ∧ q) → (p ∨ q) using the Python script
def implication(a,b):
    return(not a)or b
print("p\t q\t(p∧q)\t       (p∨q)\t       (p∧q)→(p∨q)")
print("-" * 50)
values=[True,False]
for p in values:
    for q in values:
        and_result=p and q
        or_result= p or q
        final_result=implication(and_result,or_result)
        print(f"{p}\t{q}\t{and_result}\t\t{or_result}\t\t{final_result}")
