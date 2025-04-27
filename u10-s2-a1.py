'''
U- use bfs while tracking visited nodes and tracking a sum 
INput is start location and target location along with flight dictionary(adjacency matrix/graph)
Output: sum of path to target

P - while doing bfs check if the curr node is in 

'''
from collections import deque
def calculate_cost(flights, start, dest):
    q = deque()
    q.append((start, 0))
    
    visited = set()
    while q:
        curr, currSum = q.popleft()
        if curr not in visited:
            visited.add(curr)
            for target in flights[curr]:
                if target[0] not in visited:
                    q.append((target[0], target[1] + currSum))
                    if target[0] == dest:
                        return target[1] + currSum
    return -1

flights = {
    'LAX': [('SFO', 50)],
    'SFO': [('LAX', 50), ('ORD', 100), ('ERW', 210)],
    'ERW': [('SFO', 210), ('ORD', 100)],
    'ORD': [('ERW', 300), ('SFO', 100), ('MIA', 400)],
    'MIA': [('ORD', 400)]
}

print(calculate_cost(flights, 'LAX', 'MIA'))
