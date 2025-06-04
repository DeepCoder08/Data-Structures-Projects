from object import*
from avl import*



class Bin:
    def __init__(self, bin_id, capacity):
        self.bin_id= bin_id
        self.capacity= capacity #current capacity of the bin
        self.objects= AVLTree_3() #tree to store objects according to their object_ids
        pass

    def add_object(self, object):
        # Implement logic to add an object to this bin
        x= object.object_id
        y= object.size
        c= object.size
        
        self.objects.insert_AVL(x,y)
        
        self.capacity -= x
        
        
        pass

    def remove_object(self, object_id):
        # Implement logic to remove an object by ID
        
        nodu= self.objects.search_ing(object_id)
        siz= nodu.value
        
        self.objects.delete_ion(object_id)
        
        self.capacity += siz
        
        
        
        pass
