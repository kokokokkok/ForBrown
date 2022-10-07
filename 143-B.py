import sys
import io

_INPUT = """\
3
3 1 2

"""
sys.stdin = io.StringIO(_INPUT)

n = int(input())
D =  list(map(int,input().split()))

sum = 0
for i in range(n):
    for j in range(i+1,n):
        sum += D[i]*D[j]
        #print(D[i]*D[j])
print(sum)