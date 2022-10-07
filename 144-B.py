import sys
import io

_INPUT = """\
10
"""
sys.stdin = io.StringIO(_INPUT)

n = int(input())
flag = False

for i in range(1,10):
    for j in range(1,10):
        #print(n,i*j)
        if(n == i*j):
            flag = True

if(flag == True):
    print("Yes")
else:
    print("No")