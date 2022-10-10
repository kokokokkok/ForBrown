import sys
import io

_INPUT = """\
2
1
2 0
1
1 0
"""
sys.stdin = io.StringIO(_INPUT)

n = int(input())
A = []
#-1は未確定、1は正直者、0は真偽不明

for i in range(n):
    an = int(input())
    mono_A = []
    for j in range(an):
        mono_A.append(list(map(int,input().split())))
    A.append(mono_A)
#print(A)
maxi = 0
for i in range(2**n):
    num = 0
    flag = True
    As = [-1 for i in range(n)]
    for j in range(n):
        if(i & 1 << j):#1が立っている時は正直者
            num += 1
            for k in range(len(A[j])):
                if(As[A[j][k][0]-1] == -1 or As[A[j][k][0]-1] == A[j][k][1]):
                    #print(As[A[j][k][1]-1],A[j][k][1],A[j][k][0]-1)
                    As[A[j][k][0]-1] = A[j][k][1]
                else:
                    #print(As[A[j][k][1]-1],A[j][k][1],A[j][k][0]-1)
                    flag = False
                    break
    print(As)
    for j in range(n):
        if(As[j] == 1):
            for k in range(len(A[j])):
                print(As[A[j][k][1]-1],A[j][k][1],A[j][k][0]-1)
                    
                if(As[A[j][k][0]-1] == -1 or As[A[j][k][0]-1] == A[j][k][1]):
                    #print(As[A[j][k][1]-1],A[j][k][1],A[j][k][0]-1)
                    As[A[j][k][0]-1] = A[j][k][1]
                else:
                    print(As[A[j][k][1]-1],A[j][k][1],A[j][k][0]-1)
                    flag = False
                    break
    if(flag==True):
        maxi = max(maxi,num)
    print("----------------------------")
print(maxi)