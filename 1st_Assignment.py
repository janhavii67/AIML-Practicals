import heapq

maze=[
    ['S',0,1,0],
    [0,0,1,0],
    [1,0,0,0],
    [0,0,0,'G']
]

def heuristic(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

start=(0,0)
goal=(3,3)


def astar(start,goal):
    openlist=[]
    heapq.heappush(openlist,(0,start))

    g={start:0}
    parent={}

    while openlist:
        f,current=heapq.heappop(openlist)

        if current==goal:
            path=[]
            while current in parent:
                path.append(current)
                current=parent[current]

            path.append(start)
            return path[::-1]
        r,c=current
        for dr,dc in [(0,1),(1,0),(-1,0),(0,-1)]:
            nr,nc=r+dr,c+dc

            if 0<=nr<4 and 0<=nc<4 and maze[nr][nc]!=1:
                neighbour=nr,nc
                new_g=g[current]+1

                if new_g < g.get(neighbour,float('inf')):
                    g[neighbour]=new_g
                    f=new_g+heuristic(neighbour,goal)

                    heapq.heappush(openlist,(f,neighbour))
                    parent[neighbour]=current

    return None

path=astar(start,goal)
if path:
    for position in path:
        print(position)

    for r,c in path:
        if maze[r][c]==0:
            maze[r][c]='*'

    for row in maze:
        print(*row)

print("*********** Selection Sort ******************")
array1=[86,25,55,33,67]

for i in range(0,len(array1)):
    minindex=i
    for j in range(i+1,len(array1)):
        if array1[j]<array1[minindex]:
            minindex=j
    array1[i],array1[minindex]=array1[minindex],array1[i]

print("Sorted array: ",array1)

print("************ Prims Algorithm **************")

graph = {
    'A': [('B', 2), ('E', 6)],
    'B': [('A', 2), ('C', 3), ('E', 5)],
    'C': [('B', 3), ('D', 1)],
    'D': [('C', 1), ('E', 4)],
    'E': [('A', 6), ('B', 5), ('D', 4)]
}

def prims(start):
    visited=set()
    minheap=[(0,start,None)]
    totalcost=0

    while minheap:
        weight,vertex,parent=heapq.heappop(minheap)

        if vertex in visited:
            continue

        visited.add(vertex)

        if parent is not None:
            print(parent," : ",vertex," : ",weight)
            totalcost+=weight

        for neighbour,weight in graph[vertex]:
            if neighbour not in visited:
                heapq.heappush(minheap,(weight,neighbour,vertex))
    return totalcost

print("Minimum Cost using Prims: ",prims('A'))


print("************** Kruskals Algorithm **************")

graph = [
    (2, 'A', 'B'),
    (6, 'A', 'E'),
    (3, 'B', 'C'),
    (5, 'B', 'E'),
    (1, 'C', 'D'),
    (4, 'D', 'E')
]

parent={}

def find(vertex):
    if parent[vertex]!=vertex:
        parent[vertex]=find(parent[vertex])
    return parent[vertex]


def kruskals():
    graph.sort()
    vertices={'A','B','C','D','E'}
    for v in vertices:
        parent[v]=v

    count=0
    totalcost=0

    for weight,u,v in graph:
        root1=find(u)
        root2=find(v)

        if root1 != root2:
            print(u," : ",v," : ",weight)
            totalcost+=weight
            count+=1

        if count==len(vertices)-1:
            break
    return totalcost

print("Minimum Cost using Kruskals: ",kruskals())

print("************ Dijkstras Algorithm ******************")

graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('A', 4), ('C', 1), ('D', 5)],
    'C': [('A', 2), ('B', 1), ('D', 8), ('E', 10)],
    'D': [('B', 5), ('C', 8), ('E', 2)],
    'E': [('C', 10), ('D', 2)]
}

def dijkstras(start):
    distances={}

    for vertices in graph:
        distances[vertices]=float('inf')

    distances[start]=0

    pq=[(0,start)]

    while pq:
        distance,current=heapq.heappop(pq)

        if distance>distances[current]:
            continue

        for neighbour,weight in graph[current]:
            newdistance=distance+weight

            if newdistance<distances[neighbour]:
                distances[neighbour]=newdistance
                heapq.heappush(pq,(newdistance,neighbour))

    for vertex in distances:
        print(start," : ",vertex," : ",distances[vertex])

dijkstras('A')

print("*************** Assignment : 4 ***********************")

from sklearn.model_selection import train_test_split
import pandas as pd

df=pd.read_csv("Heart.csv")

print("---------------------------------------------------------------------------")
print(df.head())
print()



print("-----------------------------------------------------------------------------")
print("Shape of Data: ",df.shape)
print()


print("-----------------------------------------------------------------------------")
print("Missing values: ",df.isnull().sum())
print()

print("-----------------------------------------------------------------------------")
print("Total Missing values: ",df.isnull().sum().sum())
print()

print("-----------------------------------------------------------------------------")
print("Data Type of each Column: ",df.dtypes)
print()

print("-----------------------------------------------------------------------------")
print("Finding out zeros: ")
print((df==0).sum(axis=0))
print()

print("-----------------------------------------------------------------------------")
print("Mean age of Patient: ",df['Age'].mean())
print()

print("-----------------------------------------------------------------------------")
df2=df[['Age','Sex','ChestPain','RestBP','Chol']]
print(df2.head())
print()

print("-----------------------------------------------------------------------------")
train_data,test_data=train_test_split(df2,random_state=42,train_size=0.25)
print("Training Data shape: ",train_data.shape)
print("Testing Data Shape: ",test_data.shape)
print()

print("***************** Assignment: 5 ************************")
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression,LogisticRegression
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error,accuracy_score

df=pd.read_csv("E:/AML practicals/temperatures.csv")

print(df.head())

X=df[['YEAR']]
Y=df['ANNUAL']

x_train,x_test,y_train,y_test=train_test_split(X,Y,random_state=42,test_size=0.25)

linear_model=LinearRegression()
linear_model.fit(x_train,y_train)

y_predict=linear_model.predict(x_test)

MSE=mean_squared_error(y_test,y_predict,)
MAE=mean_absolute_error(y_test,y_predict,)
RSquare=r2_score(y_test,y_predict)

print()
print()
print("Mean Squared Error: ",MSE)
print("Mean Absolute Error: ",MAE)
print("R2 Score: ",RSquare)
print()
print()
print("**************** Logistic Regression *****************")

median_temp=Y.median()
Y_category=(Y>=median_temp).astype(int)

x_log_train,x_log_test,y_log_train,y_log_test=train_test_split(
    X,Y_category,random_state=42,test_size=0.25
)

logmodel=LogisticRegression()
logmodel.fit(x_log_train,y_log_train)
y_log_predict=logmodel.predict(x_log_test)

print("****** Accuracy of Logistic regression *************")

accuracy_score1=accuracy_score(y_log_test,y_log_predict)
print("Accuracy of Logistic Regression: ",accuracy_score1)




