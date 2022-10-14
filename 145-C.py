import sys
import io
import math
import itertools

_INPUT = """\
3
0 0
1 0
0 1

"""
sys.stdin = io.StringIO(_INPUT)
import math
import itertools
xy = []
n = int(input())
for i in range(n):
    o = list(map(int,input().split()))
    xy.append(o)


l = [i for i in range(n)]
dist = 0
    
for v in itertools.permutations(l, n):
    print(v)
    for j in range(n-1):
        dist += math.sqrt( (xy[v[j]][0] - xy[v[j+1]][0])**2 + (xy[v[j]][1] -xy[v[j+1]][1])**2 )        
        #print(xy[v[j]][0],xy[v[j+1]][0], xy[v[j]][1] ,xy[v[j+1]][1])
    #print(dist)
print(dist/math.factorial(n))


