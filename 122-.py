import sys
import io

_INPUT = """\
ACACACACACACAC
"""
sys.stdin = io.StringIO(_INPUT)

S = input()
num = 0
maxi = 0
for i in range(len(S)):
    if(S[i] in ["A","C","G","T"]):
        #print(S[i])
        num += 1
        if(i == len(S)-1):
            maxi = max(num,maxi)
    
    else:
        maxi = max(num,maxi)
        num = 0
print(maxi)