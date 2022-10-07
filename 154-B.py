import sys
import io

_INPUT = """\
sardine
"""
sys.stdin = io.StringIO(_INPUT)

n =  len(input())
ret = ""
for i in range(n):
    ret += "x"
print(ret)