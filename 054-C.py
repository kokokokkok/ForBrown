import sys
import io

_INPUT = """\
7 7
1 3
2 7
3 4
4 5
4 6
5 6
6 7

"""
sys.stdin = io.StringIO(_INPUT)

import math
import itertools

n,m = map(int,input().split())
AB = []
G = [[] for i in range(n+1)]
l = [i+1 for i in range(n)]
num = 0

for i in range(n):
    AB.append(list(map(int,input().split())))

for i in range(n):
    G[AB[i][0]].append(AB[i][1])
    G[AB[i][1]].append(AB[i][0])
print(G)

for v in itertools.permutations(l, n):
    if(v[0]== 1):
        for i in range(n-1):
            print(v[i+1],G[i-1])
            if(v[i+1] not in G[i-1]):
                break
        num += 1

print(num)