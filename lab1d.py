
def implication(a,b):
    return (not a) or b
values=[True,False]
print("p\tq\tr\t(p∨q)\t((p∨q)→r")
print("-"*40)
for p in values:
    for q in values:
        or_result=p or q 
        for r in values:
            final_result=implication(or_result,r) 
            print(f"{p}\t{q}\t{r}\t{or_result}\t{final_result}")

