import sys
import io

_INPUT = """\
5 2
3 1 2 5
2 2 3
1 0
"""
sys.stdin = io.StringIO(_INPUT)

n,m = map(int,input().split())
KS = []
for i in range(m):
    KS.append(list(map(int,input().split())))
P = list(map(int,input().split()))

#print(n,m)
#print(KS)
#print(P)
ret = 0
for i in range(2**n):
    for j in range(m):
        num = 0
        for k in range(1,len(KS[j])):
            #print(i,1<<KS[j][k]-1)
            if(i & (1 << (KS[j][k]-1))):
                #print(i,KS[j][k]-1)
                num += 1
        #print("num: ",num)
        if(num%2 != P[j]):
            #print("bre")
            break
        if(j == m-1):
            ret += 1
    #print("-----------------------")
print(ret)