from binary_search_tree import BinarySearchNode, BinarySearchTree

class AvlNode(BinarySearchNode):
    def __init__(self, value):
        super.__init__(self, value)
        self.height = 0

    def compute_height(self):
        height = -1

        if self.left:
            height = max(height, self.left.height)
        if self.right:
            height = max(height, self.right.height)

        self.height = 1 + height

    def compute_height_difference(self):
        left_target = 0
        right_target = 0

        if self.left:
            left_target = 1 + self.left.height
        if self.right:
            right_target = 1 + self.right.height

        return left_target - right_target

    def rotate_right(self):
        child = self.left
        grandchild = child.right
        self.left = grandchild
        child.right = self

        self.compute_height()
        return child

    def rotate_left(self):
        child = self.right
        grandchild = child.left
        self.right = grandchild
        child.left = self

        self.compute_height()
        return child

    def rotate_left_right(self):
        child = self.left
        new_root = child.right
        grand_one = new_root.left
        grand_two = new_root.right

        new_root.left = child
        child.right = grand_one

        new_root.right = self
        self.left = grand_two

        child.compute_height()
        self.compute_height()

        return new_root

    def rotate_right_left(self):
        child = self.right
        new_root = child.left
        grand_one = new_root.left
        grand_two = new_root.right

        new_root.right = child
        child.left = grand_two

        self.right = grand_one
        new_root.left = self

        child.compute_height()
        self.compute_height()

        return new_root

    def add(self, value):

        new_root = self

        if value <= self.value:
            self.left = self.add_to_subtree(self.left, value)
            if self.compute_height_difference() == 2:
                if value <= self.left.value:
                    new_root = self.rotate_right()
                else:
                    new_root = self.rotate_left_right()
        else:
            self.right = self.add_to_subtree(self.right, value)
            if self.compute_height_difference() == -2:
                if value <= self.right.value:
                    new_root = self.rotate_right_left()
                else:
                    new_root = self.rotate_left()

        new_root.compute_height()
        return new_root


class AvlTree(BinarySearchTree):
    pass