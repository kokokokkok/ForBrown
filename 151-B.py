import sys
import io

_INPUT = """\
5 10 7
8 10 3 6
"""
sys.stdin = io.StringIO(_INPUT)

n,k,m = map(int,input().split())
A = list(map(int,input().split()))
flag = True
sum = sum(A)
need = m*n - sum 
#print(m*n,sum)


if(need>k):
    flag = False
if(need<0):
    need = 0

if(flag == True):
    print(need)
else:
    print(-1)