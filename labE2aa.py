#Translate and evaluate the following using Python:
'''
(a) “All even numbers are divisible by 2.”
(b) “There exists a number divisible by 3 and 5.”
'''
def forall(domain,predicate):
    return all(predicate(x) for x in domain)
def exists(domain,predicate):
    return any(predicate(x) for x in domain)
def negate_forall(domain,predicate):
    return any(not predicate(x) for x in domain)
def negate_exists(domain,predicate):
    return all(not predicate(x) for x in domain)
domain =list(range(1,21))
predicate1=lambda x:(x%2==0)
predicate2=lambda x:(x%3==0 and x%5==0) 
print("forall x (x divisible by 2):",forall(domain,predicate1))
print("exists x (x divisible by 3 and 5):",exists(domain,predicate2))
print("Negation of forall:",negate_forall(domain,predicate1))
print("Negation of exists :",negate_exists(domain,predicate2))
