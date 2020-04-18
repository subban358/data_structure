from collections import deque

def push(i, l, d):
    while len(d):
        if d[-1][0] > l[i]:
            d.pop()
        else:
            break
    d.append([l[i], i])        
def query(d, left, right):
    while len(d):
        if d[0][1] < left:
            d.popleft()
        else:
            break
    return d[0][0]


def solve(l, k):
    d = deque([])
    for i in range(k):
        push(i, l, d)
    ans = []
    left = 0
    right = k - 1
    ans.append(query(d, left, right))
    for i in range(k, len(l)):
        left += 1
        push(i, l, d)
        ans.append(query(d, left, i))
    return ans  


l = [3, 5, 2, 1, 8, 7, 4, 9]
k = 3
print(solve(l, k))