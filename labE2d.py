#Extend the domain to strings and test a predicate P(s): “s starts with a vowel.”
def forall(d,p):
 return all(p(x) for x in d)
def forexist(d,p):
  return any(p(x) for x in d)
p =lambda x:x.lower() in "s starts with vowel"
domain= [chr(i) for i in range(ord('a'),ord('f')+1)]
print("For All?:",forall(domain,p))
print("For Exist?:",forexist(domain,p))

