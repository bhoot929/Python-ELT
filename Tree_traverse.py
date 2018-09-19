class Node:
    # Utility to create new node
    def __init__(self , data):
        self.data = data
        self.left = None
        self.right = None


def minDepth(root):
    # Corner Case
    if root is None:
        return 0

        # Create an empty queue for level order traversal
    q = []

    # Enqueue root and initialize depth as 1
    q.append({'node': root, 'depth': 1})
    print(q)

    # Do level order traversal
    while (len(q) > 0):
        # Remove the front queue item
        queueItem = q.pop(0)

        # Get details of the removed item
        node = queueItem['node']
        depth = queueItem['depth']
        print(node)
        print(depth)
        # If this is the first leaf node seen so far
        # then return its depth as answer
        if node.left is None and node.right is None:
            return depth

            # If left subtree is not None, add it to queue
        if node.left is not None:
            q.append({'node': node.left, 'depth': depth + 1})

            # if right subtree is not None, add it to queue
        if node.right is not None:
            q.append({'node': node.right, 'depth': depth + 1})



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
print(minDepth(root) )


''This code will get minimum depth of the tree

     1
   /   \
  2     3
 / \   /
4   5 6 

so minimum depth is 3 here.
Time complexity of above solution is O(n) as it traverses the tree only once.
'''
