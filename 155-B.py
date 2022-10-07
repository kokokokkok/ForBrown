
import sys
import io
from traceback import print_tb

_INPUT = """\
3
28 27 24

"""
sys.stdin = io.StringIO(_INPUT)

n =  map(int, input().split())
A = list(map(int, input().split()))

flag = True
for i in A:
    if(i % 2 == 0):
        if not(i % 3 == 0 or i % 5 == 0):
            flag = False
if(flag == True):
    print("APPROVED")
else:
    print("DENIED")