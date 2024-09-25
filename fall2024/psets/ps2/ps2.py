class BinarySearchTree:
    # left: BinarySearchTree
    # right: BinarySearchTree
    # key: int
    # item: int
    # size: int
    def __init__(self, debugger = None):
        self.left = None
        self.right = None
        self.key = None
        self.item = None
        self._size = 1
        self.debugger = debugger

    @property
    def size(self):
         return self._size
       
     # a setter function
    @size.setter
    def size(self, a):
        debugger = self.debugger
        if debugger:
            debugger.inc_size_counter()
        self._size = a

    ####### Part a #######
    '''
    Calculates the size of the tree
    returns the size at a given node
    '''
    def calculate_sizes(self, debugger = None):
        # Debugging code
        # No need to modify
        # Provides counts
        if debugger is None:
            debugger = self.debugger
        if debugger:
            debugger.inc()

        # Implementation
        self.size = 1
        if self.right is not None:
            self.size += self.right.calculate_sizes(debugger)
        if self.left is not None:
            self.size += self.left.calculate_sizes(debugger)
        return self.size

    '''
    Select the ind-th key in the tree
    
    ind: a number between 0 and n-1 (the number of nodes/objects)
    returns BinarySearchTree/Node or None
    '''
    def select(self, ind):
        left_size = 0
        if self.left is not None:
            left_size = self.left.size
        if ind == left_size:
            return self
        elif ind < left_size and self.left is not None:
            return self.left.select(ind)
        elif ind > left_size and self.right is not None:
            return self.right.select(ind - left_size - 1)
        else:
            return None


    '''
    Searches for a given key
    returns a pointer to the object with target key or None (Roughgarden)
    '''
    def search(self, key):
        # if self is None:
        #     return None
        # elif self.key == key:
        #     return self
        # elif self.key < key and self.right is not None:
        #     return self.right.search(key)
        # elif self.left is not None:
        #     return self.left.search(key)
        # return None
        if self.key == key:
            return self
        elif key < self.key and self.left:
            return self.left.search(key)
        elif key > self.key and self.right:
            return self.right.search(key)
        return None
    

    '''
    Inserts a key into the tree
    key: the key for the new node; 
        ... this is NOT a BinarySearchTree/Node, the function creates one
    
    returns the original (top level) tree - allows for easy chaining in tests
    '''
    def insert(self, key):
        # if self.key is None:
        #     self.key = key
        # elif self.key > key: 
        #     if self.left is None:
        #         self.left = BinarySearchTree(self.debugger)
        #     self.left.insert(key)
        # elif self.key < key:
        #     if self.right is None:
        #         self.right = BinarySearchTree(self.debugger)
        #     self.right.insert(key)
        # self.calculate_sizes()
        # return self
        if not self.key:
            self.key = key
            self.size = 1
        elif key < self.key:
            if not self.left:
                self.left = BinarySearchTree(self.debugger)
            self.left.insert(key)
        elif key > self.key:
            if not self.right:
                self.right = BinarySearchTree(self.debugger)
            self.right.insert(key)
        self.size = 1
        if self.left:
            self.size += self.left.size
        if self.right:
            self.size += self.right.size
        return self
    
    ####### Part b #######

    '''
    Performs a `direction`-rotate the `side`-child of (the root of) T (self)
    direction: "L" or "R" to indicate the rotation direction
    child_side: "L" or "R" which child of T to perform the rotate on
    Returns: the root of the tree/subtree
    Example:
    Original Graph
      10
       \
        11
          \
           12
    
    Execute: NodeFor10.rotate("L", "R") -> Outputs: NodeFor10
    Output Graph
      10
        \
        12
        /
       11 
    '''
    def rotate(self, direction, child_side):
        # Your code goes here
        if child_side == "L":
            child = self.left
            if not child:
                return self
            if direction == "L":
                new_root = child.right
                if not new_root:
                    return self
                child.right = new_root.left
                if new_root.left:
                    new_root.left.parent = child
                new_root.left = child
                child.parent = new_root
                self.left = new_root
                child.size = ((child.left.size if child.left else 0) + 
                              (child.right.size if child.right else 0) + 1)
                new_root.size = child.size + (new_root.right.size if new_root.right else 0) + 1
            elif direction == "R":
                new_root = child.left
                if not new_root:
                    return self
                child.left = new_root.right
                if new_root.right:
                    new_root.right.parent = child
                new_root.right = child
                child.parent = new_root
                self.left = new_root
                child.size = ((child.left.size if child.left else 0) + 
                              (child.right.size if child.right else 0) + 1)
                new_root.size = (new_root.left.size if new_root.left else 0) + child.size + 1
        elif child_side == "R":
            child = self.right
            if child is None:
                return self
            if direction == "L":
                new_root = child.right
                if new_root is None:
                    return self
                child.right = new_root.left
                if new_root.left is not None:
                    new_root.left.parent = child
                new_root.left = child
                child.parent = new_root
                self.right = new_root
                child.size = ((child.left.size if child.left else 0) +
                            (child.right.size if child.right else 0) + 1)
                new_root.size = child.size + (new_root.right.size if new_root.right else 0) + 1
            elif direction == "R":
                new_root = child.left
                if new_root is None:
                    return self
                child.left = new_root.right
                if new_root.right is not None:
                    new_root.right.parent = child
                new_root.right = child
                child.parent = new_root
                self.right = new_root
                child.size = ((child.left.size if child.left else 0) +
                            (child.right.size if child.right else 0) + 1)
                new_root.size = (new_root.left.size if new_root.left else 0) + child.size + 1
        else:
            raise ValueError("child_side must be 'L' or 'R'")
        
        self.size = ((self.left.size if self.left else 0) +
                    (self.right.size if self.right else 0) + 1)
        
        return self

    def print_bst(self):
        if self.left is not None:
            self.left.print_bst()
        print( self.key),
        if self.right is not None:
            self.right.print_bst()
        return self