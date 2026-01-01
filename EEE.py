import matplotlib.pyplot as plt
If=[0,0.04,0.05,0.06,0.07,0.08]
fib1=[4.9,132.5,158.5,185,205,223]
fib2=[40,150,177.4,199.6,211.2,223]
plt.plot(If,fib1,marker='o')
plt.plot(If,fib2,marker='o')
plt.xlabel('Field current(If)')
plt.ylabel('voltage(V)')
plt.title('OCC charecteristics')
plt.grid('true')
plt.show()