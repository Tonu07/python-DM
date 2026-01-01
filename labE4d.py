def f(x):
    return x*x
domain=[-2,-1,0,1,2]
codomain=[0,1,2,3,4]
outputs=[f(x) for x in domain]
if len(outputs)==len(set(outputs)):
    print("Injective")
else:
    print("Not Injective")

if set(codomain).issubset(set(outputs)):
    print("Surjective")
else:
    print("Not Surjective")