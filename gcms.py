from bin import Bin
from avl import*
from object import Object, Color
from exceptions import NoBinFoundException

class GCMS:
    def __init__(self):
        # Maintain all the Bins and Objects in GCMS
        self.Bin_Tree_1= AVLTree_1()#for least cap, least id and greatest cap, greatest id
        self.Bin_Tree_2= AVLTree_2()#for greatest cap, least id and least cap, greatest id
        self.Bin_Tree_3= AVLTree_3()#bin id bin tree
        self.Obj_Tree_4= AVLTree_3()#objectid binid tree

        
        

    def add_bin(self, bin_id, capacity):
        
        
            
        bini= Bin(bin_id, capacity)
        key_tuple= (capacity, bin_id)
        
        self.Bin_Tree_1.insert_AVL((capacity, bin_id), bini)
        self.Bin_Tree_2.insert_AVL((capacity, bin_id), bini)
        
        self.Bin_Tree_3.insert_AVL(bin_id, bini)
        
        
        

    def add_object(self, object_id, size, color):

        
        
        
        if color==Color.BLUE:

            best_fit= None
            roty= self.Bin_Tree_1.root
            
            
            while roty!= None:
                if roty.value.capacity>= size:
                    best_fit= roty
                    roty= roty.lchild
                else:
                    roty= roty.rchild
            
            if best_fit== None: #no bin was found for the object
                raise NoBinFoundException()
        
            else:
                bin_obji= best_fit.value
                old_bin= bin_obji
        
                x= bin_obji.bin_id
                our_object= Object(object_id, size, color)
                self.Obj_Tree_4.insert_AVL(object_id, bin_obji.bin_id) #this object goes into bin having this binid
        
                #bin_obj gets updated
                bin_obji.objects.insert_AVL(object_id, size)
        
                #updated bin gets added to all the avl trees
        
                self.Bin_Tree_1.delete_ion((bin_obji.capacity, bin_obji.bin_id))
                self.Bin_Tree_2.delete_ion((bin_obji.capacity, bin_obji.bin_id))
                self.Bin_Tree_3.delete_ion(bin_obji.bin_id)

                bin_obji.capacity -=size
        
                self.Bin_Tree_1.insert_AVL((bin_obji.capacity, bin_obji.bin_id), bin_obji)
                self.Bin_Tree_2.insert_AVL((bin_obji.capacity, bin_obji.bin_id), bin_obji)
                self.Bin_Tree_3.insert_AVL(bin_obji.bin_id, bin_obji)
            
            
            
            
        if color==Color.YELLOW:
            
            roty= self.Bin_Tree_2.root
            
            best_fit= None
            
            while(roty!= None):
                if roty.value.capacity>= size:
                    best_fit= roty
                    roty= roty.lchild
                else:
                    roty= roty.rchild
        

            if best_fit== None: #no bin was found for the object
                raise NoBinFoundException()
        
            else:
                bin_obji= best_fit.value
                old_bin= bin_obji
        
                x= bin_obji.bin_id
                our_object= Object(object_id, size, color)
                self.Obj_Tree_4.insert_AVL(object_id, bin_obji.bin_id) #this object goes into bin having this binid
        
                #bin_obj gets updated
                bin_obji.objects.insert_AVL(object_id, size)
        
                #updated bin gets added to all the avl trees
        
                self.Bin_Tree_1.delete_ion((bin_obji.capacity, bin_obji.bin_id))
                self.Bin_Tree_2.delete_ion((bin_obji.capacity, bin_obji.bin_id))
                self.Bin_Tree_3.delete_ion(bin_obji.bin_id)

                bin_obji.capacity -=size
        
                self.Bin_Tree_1.insert_AVL((bin_obji.capacity, bin_obji.bin_id), bin_obji)
                self.Bin_Tree_2.insert_AVL((bin_obji.capacity, bin_obji.bin_id), bin_obji)
                self.Bin_Tree_3.insert_AVL(bin_obji.bin_id, bin_obji)
            
        
        if color==Color.RED:
            
            roty= self.Bin_Tree_2.root
            best_fit= None
            
            
            while(roty!= None):
                if roty.value.capacity>= size:
                    best_fit= roty
                roty= roty.rchild
                
            if best_fit== None: #no bin was found for the object
                raise NoBinFoundException()
        
            else:
                bin_obji= best_fit.value
                old_bin= bin_obji
        
                x= bin_obji.bin_id
                our_object= Object(object_id, size, color)
                self.Obj_Tree_4.insert_AVL(object_id, bin_obji.bin_id) #this object goes into bin having this binid
                bin_obji.objects.insert_AVL(object_id, size)
                #bin_obj gets updated
        
                #updated bin gets added to all the avl trees
        
                self.Bin_Tree_1.delete_ion((bin_obji.capacity, bin_obji.bin_id))
                self.Bin_Tree_2.delete_ion((bin_obji.capacity, bin_obji.bin_id))
                self.Bin_Tree_3.delete_ion(bin_obji.bin_id)

                bin_obji.capacity -=size
        
                self.Bin_Tree_1.insert_AVL((bin_obji.capacity, bin_obji.bin_id), bin_obji)
                self.Bin_Tree_2.insert_AVL((bin_obji.capacity, bin_obji.bin_id), bin_obji)
                self.Bin_Tree_3.insert_AVL(bin_obji.bin_id, bin_obji)
            
        
        
        if color==Color.GREEN:
            
            roty= self.Bin_Tree_1.root
            best_fit= None
            
            
            while(roty!= None):
                if roty.value.capacity>= size:
                    best_fit= roty
                roty= roty.rchild
        
        
            if best_fit== None: #no bin was found for the object
                raise NoBinFoundException()
        
            else:
                bin_obji= best_fit.value
                old_bin= bin_obji
        
                x= bin_obji.bin_id
                our_object= Object(object_id, size, color)
                self.Obj_Tree_4.insert_AVL(object_id, bin_obji.bin_id) #this object goes into bin having this binid
                bin_obji.objects.insert_AVL(object_id, size)
                #bin_obj gets updated
        
                #updated bin gets added to all the avl trees
        
                self.Bin_Tree_1.delete_ion((bin_obji.capacity, bin_obji.bin_id))
                self.Bin_Tree_2.delete_ion((bin_obji.capacity, bin_obji.bin_id))
                self.Bin_Tree_3.delete_ion(bin_obji.bin_id)

                bin_obji.capacity -=size
        
                self.Bin_Tree_1.insert_AVL((bin_obji.capacity, bin_obji.bin_id), bin_obji)
                self.Bin_Tree_2.insert_AVL((bin_obji.capacity, bin_obji.bin_id), bin_obji)
                self.Bin_Tree_3.insert_AVL(bin_obji.bin_id, bin_obji)
            
                    
            

    def delete_object(self, object_id):
        # Implement logic to remove an object from its bin
        
        bini= self.Obj_Tree_4.Search_AVL(object_id)
        if bini:
            
            ide= bini.value #id of the required bin
            
            node= self.Bin_Tree_3.Search_AVL(bini.value) #search for that id in the all bin tree
            
            if node:
                bin_obj= node.value
                old_bin= bin_obj
                x= bin_obj.capacity
                
                siz= (bin_obj.objects.Search_AVL(object_id)).value #got the object size
                bin_obj.remove_object(object_id)
                
                new_cap= x+siz
                
                self.Obj_Tree_4.delete_ion(object_id)
                
                self.Bin_Tree_1.delete_ion((x,ide))
                self.Bin_Tree_2.delete_ion((x,ide))
                self.Bin_Tree_3.delete_ion((ide))
                
                self.Bin_Tree_1.insert_AVL((bin_obj.capacity, bin_obj.bin_id), bin_obj)
                self.Bin_Tree_2.insert_AVL((bin_obj.capacity, bin_obj.bin_id), bin_obj)
                self.Bin_Tree_3.insert_AVL(bin_obj.bin_id, bin_obj)
                
                
                
                
                
        
        
        
        

    def bin_info(self, bin_id):
        # returns a tuple with current capacity of the bin and the list of objects in the bin (int, list[int])
        y= bin_id
        bin= self.Bin_Tree_3.Search_AVL(bin_id)
        
        bini= bin.value

        cap= bini.capacity

        if bini:
            A= bini.objects.trav_inorder()
            return (cap, A)
        
        return None
        
        

    def object_info(self, object_id):
        # returns the bin_id in which the object is stored
        obj_node= self.Obj_Tree_4.Search_AVL(object_id)
        if obj_node:
            
            x= obj_node.value
            return x
        
            
    
    