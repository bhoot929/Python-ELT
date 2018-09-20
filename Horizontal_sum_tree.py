'''This code will provide sum at each level for tree:

     1
   /   \
  2     3
 / \   /
4   5 6   
'''

class Node:
    def __init__(self,key):
        self.value = key
        self.left = None
        self.right = None

    def printtree(root):
        buf= []
        output = []

        if not root:
            print('$')
        else:
            buf.append(root)
            count = 1
            nextcount = 0
            while count > 0:
                node = buf.pop(0)
                if node:
                    output.append(node.value)
                    count -= 1
                    print(node.value)
                else:
                    output.append('$')
                if node and node.left:
                    buf.append(node.left)
                    nextcount += 1
                else:
                    buf.append(None)
                if node and node.right:
                    buf.append(node.right)
                    nextcount += 1
                else:
                    buf.append(None)
                if(count ==0):
                    print(str(output))
                    print("total sum="+str(sum(output)))
                    output = []
                    count = nextcount
                    nextcount = 0



if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    Node.printtree(root)

'''output:

[1]
total sum=1

[2, 3]
total sum=5

[4, 5, 6]
total sum=15'''

