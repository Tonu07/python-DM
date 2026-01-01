# Define the functions f(x)=3x+1 and g(x)=x-2
# one non answer
def f(x):
    return  3*x+1
def g(x):
    return x-2
def g_of_f(x):
    return g(f(x))
def f_of_g(x):
    return f(g(x))
x=input("Enter the value of x:")
x=int(x)
print("g of f(x):",g_of_f(x))
print("f of g(x):",f_of_g(x))