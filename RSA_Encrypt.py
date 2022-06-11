from __future__ import print_function
import sys
in_str=raw_input()
N,E,str=in_str.split(' ')
N=int(N)
E=int(E)
c = []
ans = []
def exp_mod(a,n,b):
    if(n==0):
        return 1%b
    if(n==1):
        return a%b
    t=exp_mod(a,n/2,b)
    t=(t*t)%b
    if((n&1)==1):
        t=t*a%b
    return t;

for i in range(len(str)):
    c.append(ord(str[i]))

for i in range(len(c)):
    ans.append(exp_mod(c[i],E,N))
for k in range(len(ans) -1):
               
    print(ans[k], end = '')
    print(',', end = '')
               
print(ans[len(ans)-1])



