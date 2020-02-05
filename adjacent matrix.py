def bfs(a):
    q=[]
    i=0
    visited=[0]*len(a)
    q.append(i)
    visited[i]=1
    t1 = False
    p=[-1]*len(a)
    p[0]=0
    while(len(q)>0):
        d=q.pop(0)
        print(d,visited)
        i=d
        temp=i
        for j in range(len(a)):
             if(a[i][j]==1) and (visited[j]==0):
                visited[j]=1
                q.append(j)
                p[j]=d
                print(p)
             elif(a[i][j]==1) and (p[i]!=j):
                 return True
    return False










d=int(input("Enter the number of vertex"))
a=[]
for i in range(d):
 a.append([0]*d)
s=int(input("Enter the no graph vertices:"))
for i in range(s):
    temp1,temp2=input().split()
    temp1=int(temp1)
    temp2=int(temp2)
    a[temp1][temp2]=1
    a[temp2][temp1]=1
    print(a)

print(bfs(a))






