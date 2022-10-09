import sys
import io

_INPUT = """\
8 12 2
"""
sys.stdin = io.StringIO(_INPUT)

a,b,k = map(int,input().split())
Li = []
mini = min(a,b)
for i in range(1,mini+1):
    if(a%i==0 and b%i==0):
        Li.append(i)
#print(Li)
print(Li[-k])