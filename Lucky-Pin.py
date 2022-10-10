import sys
import io
import math

_INPUT = """\
4
0224
"""
sys.stdin = io.StringIO(_INPUT)

n = input()
s = set(input())
print(len(s))
ret = math.factorial(len(s),3)
print(ret)
