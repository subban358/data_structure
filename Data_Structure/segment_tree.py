def buildTree(lis, tree, start, end, index):
    if start == end:
        tree[index] = lis[start]
        return
    mid = (start + end) // 2
    buildTree(lis, tree, start, mid, 2 * index + 1)  
    buildTree(lis, tree, mid + 1, end, 2 * index + 2)

    tree[index] = min(tree[2 * index + 1], tree[2 * index + 2])

def query(tree, lower, higher, start, end, index):
    if lower <= start and higher >= end:
        return tree[index]
    if lower > end or higher < start:
        return 2**128
    mid = (start+end) // 2
    return min(query(tree, lower, higher, start, mid, 2*index+1), query(tree, lower, higher, mid+1, end, 2*index+2))


lis = [3, 5, 2, 1, 8, 7, 4, 9]
n = len(lis)
tree = [None] * (2*n - 1)
buildTree(lis, tree, 0, n - 1, 0)
print(tree)
print(query(tree, 1, 3, 0, n - 1, 0))
