class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

def sumtr(root):
    if root is None:
        return 0
    return sumtr(root.left) + sumtr(root.right) + root.key


if __name__ == '__main__':
    root = Node(10)
    root.left=  Node(20)
    root.right=  Node(30)
    root.left.left = Node(40)
    root.left.right = Node(50)
    root.right.left = Node(60)
    root.right.right = Node(70)
    root.right.left.right = Node(80)

    total_sum = sumtr(root)
    print(f"sum of all the nodes is: {total_sum}")