import sys
import io

_INPUT = """\
11
"""
sys.stdin = io.StringIO(_INPUT)

n = int(input())
ret = 0
for i in range(1,n+1):
    if(len(str(i))%2==1):
        ret += 1

print(ret)