# Uses stack.py file present here
from stack import Stack

s = Stack()
visited = [0, 0, 0, 0, 0, 0, 0, 0, 0]
graph = [
    [1, 1, 0, 0, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 0, 0, 1],
    [0, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 0, 1],
    [0, 0, 0, 0, 1, 0, 1, 1, 0],
    [1, 0, 1, 0, 0, 0, 1, 0, 1]
]
s.push(0)
visited[0] = 1

pop = s.pop()
print(pop)

while True:
    for x in range(0, len(visited)):
        if graph[pop][x] == 1 and visited[x] == 0:
            visited[x] = 1
            s.push(x)
    if s.is_empty():
        break
    else:
        pop = s.pop()
        print(pop)
