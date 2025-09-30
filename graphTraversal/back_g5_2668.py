from collections import defaultdict, deque
import sys
#그래프에서 고리 찾는 문제와 동일

N = int(sys.stdin.readline())

graph = defaultdict(list) #기억하기. 

for i in range(1, N+1):
    j = int(sys.stdin.readline())
    graph[j].append(i)


def find_loop(graph):
    total_list = []
    for i in range(1, N+1):
        visited = [False]*(N+1)    
        
        listt = dfs(i,graph,visited)
        
        if len(listt)>=1:
            total_list.extend(listt)
    
    pass
    return list(set(total_list))
    exit()

    return -1

def dfs(start, graph, visited):
    visited[start] = True
    for e in graph[start]:
        if not visited[e]:
            
            listt = dfs(e, graph, visited)
            
            if len(listt)>=1:
                listt.append(e)
                return listt
            visited[e] = False
        else :
            
            return [e]
    return []
 


t_list = find_loop(graph)
t_list.sort()
print(len(t_list))
for e in t_list:
    print(e)