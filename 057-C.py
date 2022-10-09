import sys
import io
import math

_INPUT = """\
9876543210
"""
sys.stdin = io.StringIO(_INPUT)

def F(a,b):
    a,b = int(a),int(b) 
    return max(len(str(a)),len(str(b)))

n = int(input())
ret = 100000000000
#print(n//2+1)
for i in range(1,int(math.sqrt(n))+1):
    if(n%i==0):
        ret = min(ret,F(n/i,i))
        
print(ret)

# memo: nの約数を全て求める場合はO(√n)で求まる！