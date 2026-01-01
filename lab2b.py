def negate_forall(domain, predicate):
  return any(not predicate(x) for x in domain)
def negate_exists(domain, predicate):
  return all(not predicate(x) for x in domain)
domain=[1,2,3,4,5]
predicate1=lambda x: x**2<=16
predicate2=lambda x: x**2==25
print("Negation of forall x (x^2 <= 16):", negate_forall(domain,predicate1))
print("Negation of exists x (x^2 == 25):", negate_exists(domain,predicate2))