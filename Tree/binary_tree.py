class BinaryNode:
    def __init__(self, value = None):
        self.right = None
        self.value = value
        self.left = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def in_order_traversal(self):
        current = self.root
        stack = []
        result = []
        done = False

        while not done:
            if current:
                stack.append(current)
                current = current.left
            else:
                if len(stack) > 0:
                    current = stack.pop()
                    result.append(current.value)
                    current = current.right
                else:
                    done = False

        return result

    def pre_order_traversal(self):
        current = self.root
        stack = []
        result = []
        stack.append(current)

        while (len(stack) > 0):
            current = stack.pop()
            result.append(current.value)

            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

        return result

    def post_order_traversal(self):

        current = self.root
        stack_one = []
        stack_two = []
        result = []
        stack_one.append(current)

        while (len(stack_one) > 0):

            current = stack_one.pop()
            stack_two.append(current)

            if current.left:
                stack_one.append(current.left)
            if current.right:
                stack_one.append(current.right)

        while (len(stack_two > 0)):
            current = stack_two.pop()
            result.append(current.value)

        return result

    @staticmethod
    def is_tree_similar(node_a, node_b):
        if node_a and node_b is None:
            return True
        if node_a and node_b is not None:
            return (node_a.value == node_b.value) and BinaryTree.is_tree_similar(node_a.left, node_b.left) and BinaryTree.is_tree_similar(node_a.right, node_b.right)

        return False

    @staticmethod
    def mirror_tree(node):
        if node is None:
            return None
        BinaryTree.mirror_tree(node.left)
        BinaryTree.mirror_tree(node.right)
        node.left, node.right = node.right, node.left

    @staticmethod
    def tree_size(node):
        if node is None:
            return 0
        return(BinarySearchTree.tree_size(node.left) + 1 + BinarySearchTree.tree_size(node.right))

    def __len__(self):
        return BinarySearchTree.tree_size(self.root)

