s1=input()
s2=input()
m=len(s1)+1
n=len(s2)+1
res=[[0 for a in range(n)]for a in range(m)]
#K = [[0 for x in range(W+1)] for x in range(n+1)] 
for i in range(1,m):
    for j in range(1,n):
            print(i,j)
            if(s1[i-1]==s2[j-1]):
                res[i][j]=res[i-1][j-1]+1
            else:
                res[i][j]=max(res[i-1][j],res[i][j-1])
res[m-1][n-1]
