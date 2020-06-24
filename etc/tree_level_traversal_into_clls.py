from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

        self.left = None
        self.right = None

def levelTraversalCircularLL(root):
    levels = []
    queue = deque([root])

    while queue:
        levelTail = None
        levelSize = len(queue)
        for _ in range(levelSize):
            cur = queue.popleft()
            
            if not levelTail: # First node of level, create CLL
                levelTail = cur
                levelTail.next = levelTail
            else:
                cur.next = levelTail.next
                levelTail.next = cur
                levelTail = levelTail.next

            if cur.left: queue.append(cur.left)
            if cur.right: queue.append(cur.right)

root = Node(0)

root.left = Node(1)
root.right = Node(2)

root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)

root.left.left.left = Node(7)
root.left.left.right = Node(8)
root.left.right.left = Node(9)
root.left.right.right = Node(0)
root.right.left.left = Node(1)
root.right.left.right = Node(2)
root.right.right.left = Node(3)
root.right.right.right = Node(4)

root.left.left.left.left = Node(5)
root.left.left.left.right = Node(6)
root.left.left.right.left = Node(7)
root.left.left.right.right = Node(8)
root.left.right.left.left = Node(9)
root.left.right.left.right = Node(0)
root.left.right.right.left = Node(1)
root.left.right.right.right = Node(2)
root.right.left.left.left = Node(3)
root.right.left.left.right = Node(4)
root.right.left.right.left = Node(5)
root.right.left.right.right = Node(6)
root.right.right.left.left = Node(7)
root.right.right.left.right = Node(8)
root.right.right.right.left = Node(9)
root.right.right.right.right = Node(0)

#                0
#        1               2
#    3       4       5       6
#  7   8   9   0   1   2   3   4
# 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0

levelTraversalCircularLL(root)
print(root.left.left.right.next.val) # 9
print(root.left is root.right.next) # True

root = Node(0)

root.left = Node(1)
root.right = Node(2)

root.left.left = Node(3)
# root.left.right = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)

# root.left.left.left = Node(7)
root.left.left.right = Node(8)
# root.left.right.left = Node(9)
# root.left.right.right = Node(0)
root.right.left.left = Node(1)
root.right.left.right = Node(2)
root.right.right.left = Node(3)
# root.right.right.right = Node(4)

# root.left.left.left.left = Node(5)
# root.left.left.left.right = Node(6)
# root.left.left.right.left = Node(7)
root.left.left.right.right = Node(8)
# root.left.right.left.left = Node(9)
# root.left.right.left.right = Node(0)
# root.left.right.right.left = Node(1)
# root.left.right.right.right = Node(2)
root.right.left.left.left = Node(3)
root.right.left.left.right = Node(4)
root.right.left.right.left = Node(5)
# root.right.left.right.right = Node(6)
root.right.right.left.left = Node(7)
root.right.right.left.right = Node(8)
# root.right.right.right.left = Node(9)
# root.right.right.right.right = Node(0)

#                0
#        1               2
#    3               5       6
#      8           1   2   3    
#       8         3 4 5   7 8    

levelTraversalCircularLL(root)
print(root.left.left.right.next.val) # 1
print(root.left.left.right is root.left.left.right.next.next.next.next) # True