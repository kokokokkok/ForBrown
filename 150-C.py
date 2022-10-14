import sys
import io
_INPUT = """\
3
1 2 3
1 2 3
"""
sys.stdin = io.StringIO(_INPUT)

import itertools
n = int(input()) 
P = tuple(map(int,input().split()))
Q = tuple(map(int,input().split()))
l = [i+1 for i in range(n)]
for i, v in enumerate (itertools.permutations(l, n)):
    #print(v)
    if(v == P):
        p = i
    if(v == Q):
        q = i
#print(p,q)
print(abs(p-q))

