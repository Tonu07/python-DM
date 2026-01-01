def check_forall_exists(domain,P,Q):
    forall_true=all(P(x) for x in domain)
    exists_true=any(Q(x) for x in domain)
    return forall_true and exists_true
P=lambda x: x%2==0                   
Q=lambda x: x%3==0 and x%5==0     
domain=[2,4,6,8,10,12,15]
result=check_forall_exists(domain,P,Q)
print("domain satisfy?:",result)
