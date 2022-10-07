import sys
import io

_INPUT = """\
0
ABCXYZ


"""
sys.stdin = io.StringIO(_INPUT)

n = int(input())
s = input()

#print(ord("A"),ord("Z"))
ret = ""
for i in range(len(s)):
    ords = ord(s[i]) + n
    #print(ords)
    if(ords > 90):
        ret += chr(ords - 26)
        #print(ords - 96)
    else:
        ret += chr(ords)
print(ret)