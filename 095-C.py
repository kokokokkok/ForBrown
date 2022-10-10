import sys
import io

_INPUT = """\
1500 2000 500 90000 100000

"""
sys.stdin = io.StringIO(_INPUT)

a,b,c,x,y = map(int,input().split())
ret = 10000000000
maxi = max(x,y)
for i in range(10**5+1):
    cost = a*max(x-i,0) + b*max(y-i,0) + 2*c*i
    ret = min(ret,cost)
    #print(cost)
print(ret)