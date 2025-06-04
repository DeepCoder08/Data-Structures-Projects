class Node:
    def __init__(self,key,value=None):
        self.key=key #ID
        self.value=value #size
        
        
        self.parent=None
        self.lchild= None
        self.rchild= None
        self.height=1 #height of node is crucial for balancing the avl tree
    
    

        