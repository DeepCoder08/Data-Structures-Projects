from node import Node

def comp_1_bins_tree(node_1, node_2):
    if node_1 and node_2:
        capi1, id1= node_1.key
        capi2, id2= node_2.key
    
        if capi1>capi2:
            return 1
    
        elif capi1<capi2:
            return -1
        
        elif capi1==capi2:
            if id1<id2:
                return -1
            
            if id1==id2:
                return 0
        
            if id1>id2:
                return 1
            
            
def comp_2_bins_tree(node_1, node_2):
    if node_1 and node_2:
        capi1, id1= node_1.key
        capi2, id2= node_2.key
    
        if capi1>capi2:
            return 1
    
        elif capi1<capi2:
            return -1
        
        elif capi1==capi2:
            if id1>id2:
                return -1
            
            if id1==id2:
                return 0
        
            if id1<id2:
                return 1
            

def comp_obj_tree(node_1,node_2):
    
    if node_1 and node_2:
        
        ide1= node_1.key
        ide2= node_2.key
    
        if ide1>ide2:
            return 1
            
        elif ide1==ide2:
            return 0
        
        else:
            return -1
        
# 1: first node is greater
# -1: second node is greater


        
        
    

class AVLTree_1:
    def __init__(self, compare_function=comp_1_bins_tree):
        self.root = None
        self.size = 0
        self.comparator = compare_function
        
    def get_height(self,root):#Accessor function for the height method of "node" class
        if not root:
            return 0
        return root.height
        
    def get_balance(self,root):
        if not root:#empty tree
            return
        return self.get_height(root.lchild)-self.get_height(root.rchild)
    
    def _is_balanced(self, node):
        return abs(self._left_height(node) - self._right_height(node)) <= 1
    
    def _left_height(self, node):
        if node.lchild:
            return node.lchild.height
        
        else:
            return 0

    def _right_height(self, node):
        if node.rchild:
            return node.rchild.height
        
        else:
            return 0
        
    


    
    

    

    def insert_AVL(self, key, value):#parameters passed are root of the avl tree and the key that we want to insert
        
        new_node= Node(key,value)
        
        if not self.root:
            self.root= Node(key,value)
            return
        
        par= None
        curr= self.root

        while curr:
            par=curr
        
            if self.comparator(new_node, curr)<0:
                curr= curr.lchild
            else:
                curr= curr.rchild
            
        if self.comparator(new_node, par)<0:
            par.lchild= new_node
        else:
            par.rchild= new_node
        
        new_node.parent= par
        self.rebalancing_node(new_node)


        
        
        
        
        
    def Search_AVL(self, key):#search for an object given its object_id

    
        current= self.root
        search_for_node= Node(key)

        while current:

            compare= self.comparator(current, search_for_node)
        
            if not current or compare==0:
                return current
        
         # If key is smaller than root's key, it lies in left subtree
            elif compare>0:
                current=current.lchild
                
        
        # If key is larger than root's key, it lies in right subtree
            elif compare<0:
                current= current.rchild

        return None
            
                
    
    
    def delete_AVL(self,root, key):
        #deletes the node storing key in it

        
        node_to_be_deleted= self.Search_AVL(key)
        compare= self.comparator(root, node_to_be_deleted)
        

        if not root:
            return root #empty tree
        
        elif compare>0:
            root.lchild= self.delete_AVL(root.lchild, key)

        elif compare<0:
            root.rchild= self.delete_AVL(root.rchild, key)
        
        #these steps are just like deletion in BST.
        
        elif compare==0:
            
        
            if root.lchild is None:
                temp= root.rchild
                root= None
                return temp
            
            elif root.rchild is None:
                temp= root.lchild
                root= None
                return temp #if node being deleted is "like" leaf node you say.
            
            tempo= self.get_min_val_node(root.rchild)
            root.value= tempo.value
            root.key= tempo.key
            root.rchild= self.delete_AVL(root.rchild, tempo.key) #if some other internal node is being deleted we first replace the node by it in-order traversal successor, that is the min value of the right child, and modify the rchild accordingly.

        #update the height of the ancestor node

        root.height= max(self.get_height(root.lchild), self.get_height(root.rchild))+1

        balance_f= self.get_balance(root) #get the balance factor of the root

        if balance_f>1 and self.get_balance(root.lchild)>=0:
            return self.right_rotate(root)  #LL Rotation

        if balance_f>1 and self.get_balance(root.lchild)<0:
            root.lchild= self.left_rotate(root.lchild)
            return self.right_rotate(root) #LR Rotation
        
        if balance_f<-1 and self.get_balance(root.rchild)<=0:
            return self.left_rotate(root) #RR Rotation
        
        if balance_f<-1 and self.get_balance(root.rchild)>0:
            root.rchild= self.right_rotate(root.rchild)
            return self.left_rotate(root) #RL Rotation
        
        #Note that the way we implemented the tree will imply that rotations will only be done if upon deletion of the node, the tree becomes imbalanced.
        
        return root
    
    def left_rotate(self, nodal):
        #function performing left rotation
        x= nodal.rchild
        nodal.rchild= x.lchild
        
        if x.lchild:
            x.lchild.parent = nodal
        x.parent = nodal.parent
        if nodal.parent is None:
            self.root = x
        elif nodal == nodal.parent.lchild:
            nodal.parent.lchild = x
        else:
            nodal.parent.rchild = x
        x.lchild = nodal
        nodal.parent = x

        nodal.height= 1+ max(self.get_height(nodal.lchild), self.get_height(nodal.rchild))
        x.height= 1+ max(self.get_height(x.lchild), self.get_height(x.rchild))

        
    
    def right_rotate(self, nodal):
        #function performing right rotation

        y= nodal.lchild
        nodal.lchild= y.rchild

        if y.rchild:
            y.rchild.parent = nodal
        y.parent = nodal.parent
        if nodal.parent is None:
            self.root = y
        elif nodal == nodal.parent.lchild:
            nodal.parent.lchild = y
        else:
            nodal.parent.rchild = y
        y.rchild = nodal
        nodal.parent = y

        nodal.height= 1+ max(self.get_height(nodal.lchild), self.get_height(nodal.rchild))
        y.height= 1+ max(self.get_height(y.lchild), self.get_height(y.rchild))

    def rebalancing_node(self, node):
        while node:
            node.height= 1+ max(self.get_height(node.lchild), self.get_height(node.rchild))
            if not self._is_balanced(node):
                if self._left_height(node) > self._right_height(node):
                    if self._left_height(node.lchild) < self._right_height(node.lchild):
                        self.left_rotate(node.lchild)
                    self.right_rotate(node)
                else:
                    if self._right_height(node.rchild) < self._left_height(node.rchild):
                        self.right_rotate(node.rchild)
                    self.left_rotate(node)
            node = node.parent
    
    
    def get_min_val_node(self,node):
        while node.lchild:
            node= node.lchild
        return node
        
        
        
    def get_max_val_node(self):
        root= self.root
        
        if root is None or root.rchild is None:
            return root
            
        return self.get_max_val_node(root.rchild)
        
    def insert_ion(self, key, value):
        return self.insert_AVL(key, value)

    def delete_ion(self, key):
        node_to_delete = self.Search_AVL(key)
        if not node_to_delete:
            return

        self._delete_node(node_to_delete)

    def _delete_node(self, node):
        if not node.lchild and not node.rchild: #no child means node is leaf
            self.delete_leaf(node)


        elif not node.lchild or not node.rchild:
            self.delete_1_child(node) #node has 1 child
        
        else:

            self.delete_2_child(node) #node has 2 child

    def delete_leaf(self, node):
        parent = node.parent
        if parent:
            if parent.lchild == node:
                parent.lchild = None
            else:
                parent.rchild = None
            self.rebalancing_node(parent)
        else:
            self.root = None

    def delete_1_child(self, node):

        if node.lchild:
            child= node.lchild
        
        else:
            child= node.rchild
        
        parent = node.parent
        if parent:
            if parent.lchild == node:

                parent.lchild = child
            else:
                parent.rchild = child
            child.parent = parent

            self.rebalancing_node(parent)
        else:
            self.root = child
            child.parent = None

    def delete_2_child(self, node):
        inorder_successor = self.get_min_val_node(node.rchild)
        node.key = inorder_successor.key
        node.value = inorder_successor.value
        self._delete_node(inorder_successor)


    def search_ing(self, key):
        return self.Search_AVL( key)
        
    def trav_inorder(self):
        return self._inorder(self.root)
        
    def _inorder(self, node):
        return self._inorder(node.lchild) +[(node.key)] + self._inorder(node.rchild)
    
    
    
    
class AVLTree_2:
    def __init__(self, compare_function=comp_2_bins_tree):
        self.root = None
        self.size = 0
        self.comparator = compare_function
        
    def get_height(self,root):#Accessor function for the height method of "node" class
        if not root:
            return 0
        return root.height
        
    def get_balance(self,root):
        if not root:#empty tree
            return
        return self.get_height(root.lchild)-self.get_height(root.rchild)
    
    def _is_balanced(self, node):
        return abs(self._left_height(node) - self._right_height(node)) <= 1
    
    def _left_height(self, node):
        if node.lchild:
            return node.lchild.height
        
        else:
            return 0

    def _right_height(self, node):
        if node.rchild:
            return node.rchild.height
        
        else:
            return 0
        
    


    
    

    

    def insert_AVL(self, key, value):#parameters passed are root of the avl tree and the key that we want to insert
        
        new_node= Node(key,value)
        
        if not self.root:
            self.root= new_node
            return
        
        par= None
        curr= self.root

        while curr:
            par=curr
        
            if self.comparator(new_node, curr)<0:
                curr= curr.lchild
            else:
                curr= curr.rchild
            
        if self.comparator(new_node, par)<0:
            par.lchild= new_node
        else:
            par.rchild= new_node
        
        new_node.parent= par
        self.rebalancing_node(new_node)


        
        
        
        
        
    def Search_AVL(self, key):#search for an object given its object_id

    
        current= self.root
        search_for_node= Node(key)

        while current:

            compare= self.comparator(current, search_for_node)
        
            if not current or compare==0:
                return current
        
         # If key is smaller than root's key, it lies in left subtree
            elif compare>0:
                current=current.lchild
                
        
        # If key is larger than root's key, it lies in right subtree
            elif compare<0:
                current= current.rchild

        return None
            
                
    
    
    def delete_AVL(self,root, key):
        #deletes the node storing key in it

        
        node_to_be_deleted= self.Search_AVL(key)
        compare= self.comparator(root, node_to_be_deleted)
        

        if not root:
            return root #empty tree
        
        elif compare>0:
            root.lchild= self.delete_AVL(root.lchild, key)

        elif compare<0:
            root.rchild= self.delete_AVL(root.rchild, key)
        
        #these steps are just like deletion in BST.
        
        elif compare==0:
            
        
            if root.lchild is None:
                temp= root.rchild
                root= None
                return temp
            
            elif root.rchild is None:
                temp= root.lchild
                root= None
                return temp #if node being deleted is "like" leaf node you say.
            
            tempo= self.get_min_val_node(root.rchild)
            root.value= tempo.value
            root.key= tempo.key
            root.rchild= self.delete_AVL(root.rchild, tempo.key) #if some other internal node is being deleted we first replace the node by it in-order traversal successor, that is the min value of the right child, and modify the rchild accordingly.

        #update the height of the ancestor node

        root.height= max(self.get_height(root.lchild), self.get_height(root.rchild))+1

        balance_f= self.get_balance(root) #get the balance factor of the root

        if balance_f>1 and self.get_balance(root.lchild)>=0:
            return self.right_rotate(root)  #LL Rotation

        if balance_f>1 and self.get_balance(root.lchild)<0:
            root.lchild= self.left_rotate(root.lchild)
            return self.right_rotate(root) #LR Rotation
        
        if balance_f<-1 and self.get_balance(root.rchild)<=0:
            return self.left_rotate(root) #RR Rotation
        
        if balance_f<-1 and self.get_balance(root.rchild)>0:
            root.rchild= self.right_rotate(root.rchild)
            return self.left_rotate(root) #RL Rotation
        
        #Note that the way we implemented the tree will imply that rotations will only be done if upon deletion of the node, the tree becomes imbalanced.
        
        return root
    
    def left_rotate(self, nodal):
        #function performing left rotation
        x= nodal.rchild
        nodal.rchild= x.lchild
        
        if x.lchild:
            x.lchild.parent = nodal
        x.parent = nodal.parent
        if nodal.parent is None:
            self.root = x
        elif nodal == nodal.parent.lchild:
            nodal.parent.lchild = x
        else:
            nodal.parent.rchild = x
        x.lchild = nodal
        nodal.parent = x

        nodal.height= 1+ max(self.get_height(nodal.lchild), self.get_height(nodal.rchild))
        x.height= 1+ max(self.get_height(x.lchild), self.get_height(x.rchild))

        
    
    def right_rotate(self, nodal):
        #function performing right rotation

        y= nodal.lchild
        nodal.lchild= y.rchild

        if y.rchild:
            y.rchild.parent = nodal
        y.parent = nodal.parent
        if nodal.parent is None:
            self.root = y
        elif nodal == nodal.parent.lchild:
            nodal.parent.lchild = y
        else:
            nodal.parent.rchild = y
        y.rchild = nodal
        nodal.parent = y

        nodal.height= 1+ max(self.get_height(nodal.lchild), self.get_height(nodal.rchild))
        y.height= 1+ max(self.get_height(y.lchild), self.get_height(y.rchild))

    def rebalancing_node(self, node):
        while node:
            node.height= 1+ max(self.get_height(node.lchild), self.get_height(node.rchild))
            if not self._is_balanced(node):
                if self._left_height(node) > self._right_height(node):
                    if self._left_height(node.lchild) < self._right_height(node.lchild):
                        self.left_rotate(node.lchild)
                    self.right_rotate(node)
                else:
                    if self._right_height(node.rchild) < self._left_height(node.rchild):
                        self.right_rotate(node.rchild)
                    self.left_rotate(node)
            node = node.parent
    
    
    def get_min_val_node(self,node):
        while node.lchild:
            node= node.lchild
        return node
        
        
    def get_max_val_node(self):
        root= self.root
        
        if root is None or root.rchild is None:
            return root
            
        return self.get_max_val_node(root.rchild)
        
    def insert_ion(self, key, value):
        return self.insert_AVL(key, value)

    def delete_ion(self, key):
        node_to_delete = self.Search_AVL(key)
        if not node_to_delete:
            return

        self._delete_node(node_to_delete)

    def _delete_node(self, node):
        if not node.lchild and not node.rchild: #no child means node is leaf
            self.delete_leaf(node)


        elif not node.lchild or not node.rchild:
            self.delete_1_child(node) #node has 1 child
        
        else:

            self.delete_2_child(node) #node has 2 child

    def delete_leaf(self, node):
        parent = node.parent
        if parent:
            if parent.lchild == node:
                parent.lchild = None
            else:
                parent.rchild = None
            self.rebalancing_node(parent)
        else:
            self.root = None

    def delete_1_child(self, node):

        if node.lchild:
            child= node.lchild
        
        else:
            child= node.rchild
        
        parent = node.parent
        if parent:
            if parent.lchild == node:

                parent.lchild = child
            else:
                parent.rchild = child
            child.parent = parent

            self.rebalancing_node(parent)
        else:
            self.root = child
            child.parent = None

    def delete_2_child(self, node):
        inorder_successor = self.get_min_val_node(node.rchild)
        node.key = inorder_successor.key
        node.value = inorder_successor.value
        self._delete_node(inorder_successor)

    def search_ing(self, key):
        return self.Search_AVL( key)
        
    def trav_inorder(self):
        return self._inorder(self.root)
        
    def _inorder(self, node):
        return self._inorder(node.lchild) +[(node.key)] + self._inorder(node.rchild)
    
    
  
    
    
    
    
class AVLTree_3:
    def __init__(self, compare_function=comp_obj_tree):
        self.root = None
        self.size = 0
        self.comparator = compare_function
        
    def get_height(self,root):#Accessor function for the height method of "node" class
        if not root:
            return 0
        return root.height
        
    def get_balance(self,root):
        if not root:#empty tree
            return
        return self.get_height(root.lchild)-self.get_height(root.rchild)
    
    def _is_balanced(self, node):
        return abs(self._left_height(node) - self._right_height(node)) <= 1
    
    def _left_height(self, node):
        if node.lchild:
            return node.lchild.height
        
        else:
            return 0

    def _right_height(self, node):
        if node.rchild:
            return node.rchild.height
        
        else:
            return 0
        
    


    
    

    

    def insert_AVL(self, key, value):#parameters passed are root of the avl tree and the key that we want to insert
        
        new_node= Node(key,value)
        
        if not self.root:
            self.root= new_node
            
            return
        
        par= None
        curr= self.root

        while curr:
            par=curr
        
            if self.comparator(new_node, curr)<0:
                curr= curr.lchild
            else:
                curr= curr.rchild
            
        if self.comparator(new_node, par)<0:
            par.lchild= new_node
        else:
            par.rchild= new_node
        
        new_node.parent= par
        self.rebalancing_node(new_node)


        
        
        
        
        
    def Search_AVL(self, key):#search for an object given its object_id

    
        current= self.root
        search_for_node= Node(key)

        while current:
            compare= self.comparator(current, search_for_node)
            if compare==0:
                return current
            elif compare>0:
                current=current.lchild
            elif compare<0:
                current= current.rchild

        
        
        return None
            
                
    
    
    def delete_AVL(self,root, key):
        #deletes the node storing key in it

        
        node_to_be_deleted= self.Search_AVL(key)
        compare= self.comparator(root, node_to_be_deleted)
        

        if not root:
            return root #empty tree
        
        elif compare>0:
            root.lchild= self.delete_AVL(root.lchild, key)

        elif compare<0:
            root.rchild= self.delete_AVL(root.rchild, key)
        
        #these steps are just like deletion in BST.
        
        elif compare==0:
            
        
            if root.lchild is None:
                temp= root.rchild
                root= None
                return temp
            
            elif root.rchild is None:
                temp= root.lchild
                root= None
                return temp #if node being deleted is "like" leaf node you say.
            
            tempo= self.get_min_val_node(root.rchild)
            root.value= tempo.value
            root.key= tempo.key
            root.rchild= self.delete_AVL(root.rchild, tempo.key) #if some other internal node is being deleted we first replace the node by it in-order traversal successor, that is the min value of the right child, and modify the rchild accordingly.

        #update the height of the ancestor node

        root.height= max(self.get_height(root.lchild), self.get_height(root.rchild))+1

        balance_f= self.get_balance(root) #get the balance factor of the root

        if balance_f>1 and self.get_balance(root.lchild)>=0:
            return self.right_rotate(root)  #LL Rotation

        if balance_f>1 and self.get_balance(root.lchild)<0:
            root.lchild= self.left_rotate(root.lchild)
            return self.right_rotate(root) #LR Rotation
        
        if balance_f<-1 and self.get_balance(root.rchild)<=0:
            return self.left_rotate(root) #RR Rotation
        
        if balance_f<-1 and self.get_balance(root.rchild)>0:
            root.rchild= self.right_rotate(root.rchild)
            return self.left_rotate(root) #RL Rotation
        
        #Note that the way we implemented the tree will imply that rotations will only be done if upon deletion of the node, the tree becomes imbalanced.
        
        return root
    
    def left_rotate(self, nodal):
        #function performing left rotation
        x= nodal.rchild
        nodal.rchild= x.lchild
        
        if x.lchild:
            x.lchild.parent = nodal
        x.parent = nodal.parent
        if nodal.parent is None:
            self.root = x
        elif nodal == nodal.parent.lchild:
            nodal.parent.lchild = x
        else:
            nodal.parent.rchild = x
        x.lchild = nodal
        nodal.parent = x

        nodal.height= 1+ max(self.get_height(nodal.lchild), self.get_height(nodal.rchild))
        x.height= 1+ max(self.get_height(x.lchild), self.get_height(x.rchild))

        
    
    def right_rotate(self, nodal):
        #function performing right rotation

        y= nodal.lchild
        nodal.lchild= y.rchild

        if y.rchild:
            y.rchild.parent = nodal
        y.parent = nodal.parent
        if nodal.parent is None:
            self.root = y
        elif nodal == nodal.parent.lchild:
            nodal.parent.lchild = y
        else:
            nodal.parent.rchild = y
        y.rchild = nodal
        nodal.parent = y

        nodal.height= 1+ max(self.get_height(nodal.lchild), self.get_height(nodal.rchild))
        y.height= 1+ max(self.get_height(y.lchild), self.get_height(y.rchild))

    def rebalancing_node(self, node):
        while node:
            node.height= 1+ max(self.get_height(node.lchild), self.get_height(node.rchild))


            if not self._is_balanced(node):

                if self._left_height(node) > self._right_height(node):

                    if self._left_height(node.lchild) < self._right_height(node.lchild):
                        self.left_rotate(node.lchild)
                    self.right_rotate(node)
                else:

                    if self._right_height(node.rchild) < self._left_height(node.rchild):
                        self.right_rotate(node.rchild)
                    self.left_rotate(node)
            node = node.parent
    
    
    def get_min_val_node(self,node): #get the min value node of the tree
        
        while node.lchild:
            node= node.lchild
        return node
        
        
        
    def get_max_val_node(self):
        root= self.root
        
        if root is None or root.rchild is None:
            return root
            
        return self.get_max_val_node(root.rchild)
        
    def insert_ion(self, key, value): #performs insertion in the tree
        return self.insert_AVL(key, value)

    def delete_ion(self, key):
        node_to_delete = self.Search_AVL(key)
        if not node_to_delete:
            return

        self._delete_node(node_to_delete)

    def _delete_node(self, node):
        if not node.lchild and not node.rchild: #no child means node is leaf
            self.delete_leaf(node)


        elif not node.lchild or not node.rchild:
            self.delete_1_child(node) #node has 1 child
        
        else:

            self.delete_2_child(node) #node has 2 child

    def delete_leaf(self, node):
        parent = node.parent
        if parent:
            if parent.lchild == node:
                parent.lchild = None
            else:
                parent.rchild = None
            self.rebalancing_node(parent)
        else:
            self.root = None

    def delete_1_child(self, node):

        if node.lchild:
            child= node.lchild
        
        else:
            child= node.rchild
        
        parent = node.parent
        if parent:
            if parent.lchild == node:

                parent.lchild = child
            else:
                parent.rchild = child
            child.parent = parent

            self.rebalancing_node(parent)
        else:
            self.root = child
            child.parent = None

    def delete_2_child(self, node):
        inorder_successor = self.get_min_val_node(node.rchild)
        node.key = inorder_successor.key
        node.value = inorder_successor.value
        self._delete_node(inorder_successor)


    def search_ing(self, key):
        return self.Search_AVL( key)
        
    def trav_inorder(self):
        return self._inorder(self.root)
        
    def _inorder(self, node):
        if node is not None:

            return self._inorder(node.lchild) +[(node.key)] + self._inorder(node.rchild)
        
        else:
            return []
    
    
 
    