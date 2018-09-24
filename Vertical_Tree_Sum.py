'''
This code will get summation of Tree elements vertically.

https://algorithms.tutorialhorizon.com/print-the-vertical-sum-in-binary-tree/

'''
class Node:
    def __init__(self,key):
        self.value = key
        self.left = None
        self.right = None

    def printtree(root):
        buf= []
        output_dict  = {}

        if not root:
            print('$')
        else:
            buf.append(root)
            count = 1

            while count > 0:
                node = buf.pop(0)
                if node.value not in(output_dict):
                    count -= 1
                    output_dict[node.value] = 0
                if node and node.left:
                    buf.append(node.left)
                    output_dict[node.left.value] = output_dict[node.value] + 1
                    count += 1
                else:
                    buf.append(None)
                if node and node.right:
                    buf.append(node.right)
                    output_dict[node.right.value] = output_dict[node.value] - 1
                    count += 1
                else:
                    buf.append(None)
                count -= 1

            print(output_dict)

            sum_dict = {}
            for i,j in output_dict.items():
                if j not in(sum_dict):
                    sum_dict[j] = i
                else:
                    sum_dict[j] += i
            print(sum_dict)

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    Node.printtree(root)


'''
Output:

Original Dict: {1: 0, 2: 1, 3: -1, 4: 2, 5: 0, 6: 0, 7: -2}
Sum Dict: {0: 12, 1: 2, -1: 3, 2: 4, -2: 7}

'''
