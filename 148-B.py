import sys
import io

_INPUT = """\
8
hmhmnknk uuuuuuuu
"""
sys.stdin = io.StringIO(_INPUT)

n = int(input())
a,b =  map(str,input().split())
ret = ""
for i in range(2*n):
    if(i%2 == 0):
        ret += a[i//2]
        
    else:
        ret += b[i//2]
print(ret)