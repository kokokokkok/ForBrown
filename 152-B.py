import sys
import io

_INPUT = """\
7 7

"""
sys.stdin = io.StringIO(_INPUT)

a,b =  map(int,input().split())

if(b>a):
    print(str(a)*b)
elif(a>b):
    print(str(b)*a)
else:
    print(str(a)*a)