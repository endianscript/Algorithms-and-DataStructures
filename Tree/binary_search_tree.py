from binary_tree import BinaryNode, BinaryTree

class BinarySearchNode(BinaryNode):

    def add(self, value):
        if value <= self.value:
            self.left = self.add_to_subtree(self.left, value)
        else:
            self.right = self.add_to_subtree(self.right, value)

    def add_to_subtree(self, parent, value):
        if parent:
            return parent.add(value)
        return BinaryNode(value)

    def remove(self, value):
        if value < self.value:
            self.left = self.remove_from_subtree(self.left, value)
        elif value > self.value:
            self.right = self.remove_from_subtree(self.right, value)
        else:
            if self.left is None:
                return self.right

            child = self.left
            while child.right:
                child = child.right

            child_key = child.value
            self.left = self.remove_from_subtree(self.left, child_key)
            self.value = child_key

        return self

    def remove_from_subtree(self, parent, value):
        if parent:
            return parent.remove(value)
        return None


class BinarySearchTree(BinaryTree):

    def add_node(self, value):
        if self.root is None:
            self.root = BinarySearchNode(value)
        else:
            self.root.add(value)

    def remove_node(self, value):
        if self.root is None:
            raise Exception ('The Tree is empty. Cannot delete.')
        else:
            self.root.remove(value)

