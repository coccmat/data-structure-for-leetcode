from typing import Optional, List


class TreeNode:
    '''
    Class to define a binary tree node and methods to populate a tree.
    '''
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None, next: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next # some leetcode promblems use this pointer 

    def __str__(self):
        return f"TreeNode({self.val})"

    def newNode(self, val=0):
        '''
        Populate a sorted binary tree with a new node.
        '''
        if self.val < val:
            if self.right is None:
                new_node = TreeNode(val)
                self.right = new_node
                return
            self.right.newNode(val=val)
            return
        if self.left is None:
            new_node = TreeNode(val)
            self.left = new_node
            return
        self.left.newNode(val=val)
    def newNode_no_rep(self, val=0):
        '''
        Populate a sorted binary tree with no duplicated value.
        '''
        if self.val == val: 
            print(f"the value {val} is alredy in the tree")
            return 
        if self.val < val:
            if self.right is None:
                new_node = TreeNode(val)
                self.right = new_node
                return
            self.right.newNode(val=val)
            return
        if self.left is None:
            new_node = TreeNode(val)
            self.left = new_node
            return
        self.left.newNode(val=val)

    def newNode_not_sorted(self, arr: List)->Optional['TreeNode']:
        '''
        Populate a binary tree given a list of values, maintaining null pointers explicitly.
        '''
        if not arr:
            return None

        # Create nodes from the array
        nodes = [TreeNode(val) if val is not None else None for val in arr]

        # Use a queue to keep track of the parent nodes
        queue = deque()
        root = nodes[0]
        queue.append(root)

        index = 1  

        while queue and index < len(nodes):
            parent = queue.popleft()  # Get the current parent node

            if parent is not None:
                
                if index < len(nodes):
                    parent.left = nodes[index]
                    queue.append(nodes[index]) 
                    index += 1

                
                if index < len(nodes):
                    parent.right = nodes[index]
                    queue.append(nodes[index])  
                    index += 1

        return root