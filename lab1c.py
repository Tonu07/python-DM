
values=[True,False]
print("p\t¬p\tp∨¬p ")
print("-"*25)
is_tautology=True
for p in values:
    neg_p=not p
    result=p or neg_p
    print(f"{p}\t{neg_p}\t{result}")
    if not result:
        is_tautology=False
if is_tautology:
    print("\nThe expression p∨¬p is a tautology.")
else:
    print("\nThe expression p∨¬pis NOT a tautology.")
