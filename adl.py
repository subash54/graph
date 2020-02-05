#sample programs
class adjNode:

    def __init__(self,vertices):
        self.data=vertices
        self.next=None
class Graph:
    def __init__(self,v):
        self.m=v
        self.arr=[None]*v
    def addnode(self,src,des):
        node=adjNode(des)
        node.next=self.arr[src]
        self.arr[src]=node
        node=adjNode(src)
        node.next=self.arr[des]
        self.arr[des]=node
    def printGraph(self):
        for i in range(self.m):

            temp=self.arr[i]
            print("v",i)
            while temp:

                print(temp.data,"->",end=" ")
                temp=temp.next
            print("")
    def bfs(self,s):
        print("The breadth first search is")
        ans=[]
        visited=[0]*self.m
        q=[]
        q.append(s)
        visited[s]=1
        while(len(q)!=0):
            print(q)
            d=q.pop(0)

            ans.append(d)
            #print(q)
            temp=self.arr[d]


            while(temp):
                if(visited[temp.data]==0):
                    visited[temp.data]=1
                    q.append(temp.data)
                temp=temp.next
        print(ans)

    def dfs(self,i,a):
        print(i)
        a[i] = 1
        print(a)


        temp=self.arr[i]


        while temp:
            j=temp.data
            if(a[j]==0):
                self.dfs(j,a)
            temp=temp.next











d=int(input("Enter the number of vertices:"))
g=Graph(d)
g.addnode(0,1)
g.addnode(0,2)
g.addnode(1,3)
g.addnode(3,5)
g.addnode(2,4)
g.addnode(4,5)

g.printGraph()
k=[0]*d

g.bfs(0)






