from __future__ import print_function
import sys
import math
in_str=raw_input()
a, b, c = in_str.split(' ')
a = int(a)
b = int(b)
c=c.split(',')
a_bar = int(a**0.5) +1
x = math.ceil(math.sqrt(a))
y = x**2 - a
while not math.sqrt(y).is_integer():
    x += 1
    y = x**2 - a
p=x + math.sqrt(y)
q=x - math.sqrt(y)

r=((int(p-1))*(int(q-1)))

def ext_euclid(a, b):
    if b == 0:
        return 1, 0, a
    else:
        x, y, q = ext_euclid(b, a % b) # q = gcd(a, b) = gcd(b, a%b)
        x, y = y, (x - (a // b) * y)
    return (x,y,q)
answer=ext_euclid(b, r)
d=abs(answer[0])
ans = ''
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
for k in range(len(c)):
    m=int(exp_mod(int(c[k]),d,a))
    ans+=chr(m)
print(ans)

