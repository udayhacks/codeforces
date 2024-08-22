#importing 
from collections import deque


#funct

def add_edge(adj,i,j):
    adj[j].append(i)
    adj[i].append(j)


#declaration]

n = 4 
adj = [[] for _ in range(n+1)]   
vst = [0]*(n+1)
que = deque([])
start = 0

add_edge(adj, 0, 1)
add_edge(adj, 0, 2)
add_edge(adj, 1, 3)
add_edge(adj, 1, 4)
add_edge(adj, 2, 4)









# implementation 
vst[start] = 1 
que.append(start)


while que :
    k = que.popleft()
    print(k,end="")
    for i in adj[k]:
        if vst[i] == 0 :
            vst[i] =1
            que.append(i)
    
    











print(adj,vst,que)