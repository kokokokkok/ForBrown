import sys
import io

_INPUT = """\
33
ABCCABCBABCCABACBCBBABCBCBCBCABCB
"""
sys.stdin = io.StringIO(_INPUT)

n = int(input())
s = input()
ret = 0
for i in range(n-2):
    if(s[i] == "A" and s[i+1] == "B" and s[i+2] == "C"):
        ret += 1
print(ret)