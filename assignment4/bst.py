# Name:Michael Green
# OSU Email: greemich@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 4
# Due Date: Feb 23, 2026
# Description: Implementation of BST with add, variations of remove to support different cases, contains,
# inorder_traversal, find_min, find_max, is_empty, and make_empty methods. 
# Recursive methods are allowed and implemented for the inorder traversal, but iterative methods are used for add, remove, and contains.



from platform import node
import random
from queue_and_stack import Queue, Stack


class BSTNode:
    """
    Binary Search Tree Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """

    def __init__(self, value: object) -> None:
        """
        Initialize a new BST node
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.value = value  # to store node's data
        self.left = None    # pointer to root of left subtree
        self.right = None   # pointer to root of right subtree

    def __str__(self) -> str:
        """
        Override string method
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'BST Node: {}'.format(self.value)


class BST:
    """Binary Search Tree class"""

    def __init__(self, start_tree=None) -> None:
        """
        Initialize new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._root = None

        # populate BST with initial values (if provided)
        # before using this feature, implement add() method
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    def __str__(self) -> str:
        """
        Override string method; display in pre-order
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        values = []
        self._str_helper(self._root, values)
        return "BST pre-order { " + ", ".join(values) + " }"

    def _str_helper(self, node: BSTNode, values: []) -> None:
        """
        Helper method for __str__. Does pre-order tree traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if not node:
            return
        values.append(str(node.value))
        self._str_helper(node.left, values)
        self._str_helper(node.right, values)

    def get_root(self) -> BSTNode:
        """
        Return root of tree, or None if empty
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._root

    def is_valid_bst(self) -> bool:
        """
        Perform pre-order traversal of the tree.
        Return False if nodes don't adhere to the bst ordering property.

        This is intended to be a troubleshooting method to help find any
        inconsistencies in the tree after the add() or remove() operations.
        A return of True from this method doesn't guarantee that your tree
        is the 'correct' result, just that it satisfies bst ordering.

        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        stack = Stack()
        stack.push(self._root)
        while not stack.is_empty():
            node = stack.pop()
            if node:
                if node.left and node.left.value >= node.value:
                    return False
                if node.right and node.right.value < node.value:
                    return False
                stack.push(node.right)
                stack.push(node.left)
        return True

    def print_tree(self):
        """
        Prints the tree using the print_subtree function.

        This method is intended to assist in visualizing the structure of the
        tree. You are encouraged to add this method to the tests in the Basic
        Testing section of the starter code or your own tests as needed.

        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if self.get_root():
            self._print_subtree(self.get_root())
        else:
            print('(empty tree)')

    def _print_subtree(self, node, prefix: str = '', branch: str = ''):
        """
        Recursively prints the subtree rooted at this node.

        This is intended as a 'helper' method to assist in visualizing the
        structure of the tree.

        DO NOT CHANGE THIS METHOD IN ANY WAY
        """

        def add_junction(string):
            """
            Adds a 'junction marker' to a string prefix as a connecting line
            to visually represent branches between nodes in a subtree

            Helper method for _print_subtree() to aid in tree formatting

            DO NOT CHANGE THIS METHOD IN ANY WAY
            """
            if len(string) < 2 or branch == '':
                return string
            junction = '|' if string[-2] == '|' else '`'
            return string[:-2] + junction + '-'

        if not node:
            print(add_junction(prefix) + branch + "None")
            return

        if len(prefix) > 2 * 16:
            print(add_junction(prefix) + branch + "(tree continues)")
            return

        if node.left or node.right:
            postfix = ' (root)' if branch == '' else ''
            print(add_junction(prefix) + branch + str(node.value) + postfix)
            self._print_subtree(node.right, prefix + '| ', 'R: ')
            self._print_subtree(node.left, prefix + '  ', 'L: ')
        else:
            print(add_junction(prefix) + branch + str(node.value) + ' (leaf)')

    # ------------------------------------------------------------------ #

    def add(self, value: object) -> None:
        '''
        Adds a new value to the BST by iterative traversal.
        Adapted from the insert() pseudocode in the exploration.
        :param self: The BST instance
        :param value: The value to add to the BST
        '''
        # initialize to track new node's parent (p) and start at the root of the tree
        p = None
        n= self._root
        # traverse unitl we hit a leaf (None) and keep track of the parent
        while n is not None:
            p = n
            if value < n.value:
                n = n.left
            else:          # a duplicate value will be added to the right subtree
                n = n.right
        # create new node containing the value
        new_node = BSTNode(value)
        if p is None:          # tree was empty, new node becomes root
            self._root = new_node  
        # compare and place 
        elif value < p.value:
            p.left = new_node
        else:
            p.right = new_node  # a duplicate value will be added to the right subtree

    def remove(self, value: object) -> bool:
        """
        Removes a value from the BST. by calling the appropriate helper method based on the number of subtrees of the node to be removed.
        This method and the helper methods are adapted from the remove() pseudocode in the exploration.
        :param self: The BST instance
        :param value: The value to remove from the BST
        :return: True if the value was removed, False if the value was not found
        """
        # find the node to remove and its parent
        p = None
        n = self._root
        # same traversal as add() but stops if we locate the value
        while n is not None and n.value != value:
            p = n
            if value < n.value:
                n = n.left
            else:         
                n = n.right

        if n is None:  # value not found
            return False

        # determine which removal method to use and call it

        # there are no subtrees 
        if n.left is None and n.right is None:
            self._remove_no_subtrees(p, n)
        # either a left or right subtree 
        elif n.left is None or n.right is None:
            self._remove_one_subtree(p, n)
        # two subtrees
        else:
            self._remove_two_subtrees(p, n)

        return True

    def _remove_no_subtrees(self, remove_parent: BSTNode, remove_node: BSTNode) -> None:
        '''
        Removes a leaf node
        :param self: The BST instance
        :param remove_parent: The parent of the node to be removed
        :param remove_node: The node to be removed
        '''
        # remove ONLY leaf node
        if remove_parent is None:  # removing the root node which is a leaf
            self._root = None
        elif remove_parent.left == remove_node: #removing left child leaf node
            remove_parent.left = None
        elif remove_parent.right == remove_node: #removing right child leaf node
            remove_parent.right = None


    def _remove_one_subtree(self, remove_parent: BSTNode, remove_node: BSTNode) -> None:
        '''
        Removes a node with one subtree
        :param self: The BST instance
        :param remove_parent: The parent of the node to be removed
        :param remove_node: The node to be removed
        '''

        # Store the child "c" of the node to be removed to preserve the subtree
        if remove_node.left is not None:
            c = remove_node.left
        else:
            c = remove_node.right

        if remove_parent is None:  # removing the root node which has one subtree
            self._root = c  

        # reconnect the parent of the removed node to the child of the removed node 
        elif remove_parent.left == remove_node:
            remove_parent.left = c
        elif remove_parent.right == remove_node:
            remove_parent.right = c 

    def _remove_two_subtrees(self, remove_parent: BSTNode, remove_node: BSTNode) -> None:
        '''
        Removes a node with two subtrees and replaces it with its inorder successor.
        :param self: The BST instance
        :param remove_parent: The parent of the node to be removed
        :param remove_node: The node to be removed
        '''
        # find the inorder successor "s" and its parent(of successor) "ps"
        ps = remove_node
        s = remove_node.right
        # the successor is always the leftmost node in the right subtree of the node to be removed.
        while s.left is not None:
            ps = s
            s = s.left

        # update the sucessor's pointer to the left subtree of the node to be removed
        s.left = remove_node.left
       
        if s is not remove_node.right:  
            ps.left = s.right
            s.right = remove_node.right

        # connect the parent of the removed node to the successor 
        if remove_parent is None:  # removing the root node 
            self._root = s
        elif remove_parent.left == remove_node:
            remove_parent.left = s
        else:
            remove_parent.right = s

    
              
    def contains(self, value: object) -> bool:
        """
        Checks if a value is present in the BST by iteratively traversing the tree.
        Adapted from the find() pseudocode in the exploration.
        :param self: The BST instance
        :param value: The value we are searching for
        :return: True if the value is found, False otherwise
       """
        
        n= self._root
        while n is not None:
            if value == n.value:
                return True # value found
            # move left or right based on comparison
            elif value < n.value:
                n = n.left
            else:         
                n = n.right
        return False 
    

    def inOrder(self, node: BSTNode, result: Queue) -> None:
        '''
        Helper method for recursive inorder traversal of the BST adapted from the inOrder() pseudocode in the exploration. 
        :param self: The BST instance
        :param node: The current node being visited in the traversal
        :param result: The Queue to store the values in sorted order
        '''
        if node is not None:
            self.inOrder(node.left, result)  
            result.enqueue(node.value)       
            self.inOrder(node.right, result) 

    def inorder_traversal(self) -> Queue:
        """
        Performs an inorder traversal of the BST using inOrder() helper method and stores the values in a Queue to return them in sorted order.
        :param self: The BST instance
        :return: A Queue containing the values of the BST in sorted order
        """
        result = Queue()
        self.inOrder(self._root, result)
        
        return result         
    
    def find_min(self) -> object:
        """
        Finds the minimum value in the BST by iteratively traversing the leftmost path of the tree from the root
        similar to how we find the correct successor in the _remove_two_subtrees().
        :param self: The BST instance
        :return: The minimum value in the BST, or None if the tree is empty.
        """
        n= self._root
        if n is None:
            return None
        while n.left is not None:
            n = n.left
        return n.value

    def find_max(self) -> object:
        """
        Finds the maximum value in the BST by iteratively traversing the rightmost path of the tree from the root.
        similar to how we find the correct predecessor in the _remove_two_subtrees().
        :param self: The BST instance
        :return: The maximum value in the BST, or None if the tree is empty.
        """
        n= self._root
        if n is None:
            return None
        while n.right is not None:
            n = n.right
        return n.value

    def is_empty(self) -> bool:
        """
        Checks if the BST is empty by checking if the root is None.
        :return: True if the BST is empty, False otherwise
        """
        if self._root is None:
            return True
        else:
            return False

    def make_empty(self) -> None:
        """
        Empties the BST by setting the root to None.
        :param self: The BST instance
        """
        self._root = None



# ------------------- BASIC TESTING -----------------------------------------


if __name__ == '__main__':

    print("\nPDF - method add() example 1")
    print("----------------------------")
    test_cases = (
        (1, 2, 3),
        (3, 2, 1),
        (1, 3, 2),
        (3, 1, 2),
    )
    for case in test_cases:
        tree = BST(case)
        print(tree)
        tree.print_tree()

    print("\nPDF - method add() example 2")
    print("----------------------------")
    test_cases = (
        (10, 20, 30, 40, 50),
        (10, 20, 30, 50, 40),
        (30, 20, 10, 5, 1),
        (30, 20, 10, 1, 5),
        (5, 4, 6, 3, 7, 2, 8),
        (range(0, 30, 3)),
        (range(0, 31, 3)),
        (range(0, 34, 3)),
        (range(10, -10, -2)),
        ('A', 'B', 'C', 'D', 'E'),
        (1, 1, 1, 1),
    )
    for case in test_cases:
        tree = BST(case)
        print('INPUT  :', case)
        print('RESULT :', tree)

    print("\nPDF - method add() example 3")
    print("----------------------------")
    for _ in range(100):
        case = list(set(random.randrange(1, 20000) for _ in range(900)))
        tree = BST()
        for value in case:
            tree.add(value)
        if not tree.is_valid_bst():
            raise Exception("PROBLEM WITH ADD OPERATION")
    print('add() stress test finished')

    print("\nPDF - method remove() example 1")
    print("-------------------------------")
    test_cases = (
        ((1, 2, 3), 1),
        ((1, 2, 3), 2),
        ((1, 2, 3), 3),
        ((50, 40, 60, 30, 70, 20, 80, 45), 0),
        ((50, 40, 60, 30, 70, 20, 80, 45), 45),
        ((50, 40, 60, 30, 70, 20, 80, 45), 40),
        ((50, 40, 60, 30, 70, 20, 80, 45), 30),
    )
    for case, del_value in test_cases:
        tree = BST(case)
        print('INPUT  :', tree, 'DEL:', del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 2")
    print("-------------------------------")
    test_cases = (
        ((50, 40, 60, 30, 70, 20, 80, 45), 20),
        ((50, 40, 60, 30, 70, 20, 80, 15), 40),
        ((50, 40, 60, 30, 70, 20, 80, 35), 20),
        ((50, 40, 60, 30, 70, 20, 80, 25), 40),
    )
    for case, del_value in test_cases:
        tree = BST(case)
        print('INPUT  :', tree, 'DEL:', del_value)
        tree.print_tree()
        tree.remove(del_value)
        print('RESULT :', tree)
        tree.print_tree()
        print('')

    print("\nPDF - method remove() example 3")
    print("-------------------------------")
    case = range(-9, 16, 2)
    tree = BST(case)
    for del_value in case:
        print('INPUT  :', tree, del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 4")
    print("-------------------------------")
    case = range(0, 34, 3)
    tree = BST(case)
    for _ in case[:-2]:
        root_value = tree.get_root().value
        print('INPUT  :', tree, root_value)
        tree.remove(root_value)
        if not tree.is_valid_bst():
            raise Exception("PROBLEM WITH REMOVE OPERATION")
        print('RESULT :', tree)

    print("\nPDF - method remove() example 5")
    print("-------------------------------")
    for _ in range(100):
        case = list(set(random.randrange(1, 20000) for _ in range(900)))
        tree = BST(case)
        for value in case[::2]:
            tree.remove(value)
        if not tree.is_valid_bst():
            raise Exception("PROBLEM WITH REMOVE OPERATION")
    print('remove() stress test finished')

    print("\nPDF - method contains() example 1")
    print("---------------------------------")
    tree = BST([10, 5, 15])
    print(tree.contains(15))
    print(tree.contains(-10))
    print(tree.contains(15))

    print("\nPDF - method contains() example 2")
    print("---------------------------------")
    tree = BST()
    print(tree.contains(0))

    print("\nPDF - method inorder_traversal() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree.inorder_traversal())

    print("\nPDF - method inorder_traversal() example 2")
    print("---------------------------------")
    tree = BST([8, 10, -4, 5, -1])
    print(tree.inorder_traversal())

    print("\nPDF - method find_min() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Minimum value is:", tree.find_min())

    print("\nPDF - method find_min() example 2")
    print("---------------------------------")
    tree = BST([8, 10, -4, 5, -1])
    print(tree)
    print("Minimum value is:", tree.find_min())

    print("\nPDF - method find_max() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Maximum value is:", tree.find_max())

    print("\nPDF - method find_max() example 2")
    print("---------------------------------")
    tree = BST([8, 10, -4, 5, -1])
    print(tree)
    print("Maximum value is:", tree.find_max())

    print("\nPDF - method is_empty() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print("Tree is empty:", tree.is_empty())

    print("\nPDF - method is_empty() example 2")
    print("---------------------------------")
    tree = BST()
    print("Tree is empty:", tree.is_empty())

    print("\nPDF - method make_empty() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)

    print("\nPDF - method make_empty() example 2")
    print("---------------------------------")
    tree = BST()
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)
