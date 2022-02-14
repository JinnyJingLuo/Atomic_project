#!/usr/bin/env python3 

class Node():
    
    def __str__(self):
        return self.name

    def __init__(self,
        name = None,
        parent = None, 
        child_left = None,
        child_right = None, 
        ):
        self.name = name
        self.parent = parent
        self.child_right = child_right
        self.child_left = child_left
    
    def compare(self, name):
        if self.name < name:
            return -1
        if self.name > name:
            return 1
        if self.name == name:
            return 0

    def get_name(self):
        return self.name
    
    def get_parent(self):
        return self.parent
    
    def get_leftchild(self):
        return self.child_left

    def get_rightchild(self):
        return self.child_right
    
    def has_leftchild(self):
        if(self.get_leftchild() == None):
            return 0
        else:
            return 1

    def has_rightchild(self):
        if(self.get_rightchild() == None):
            return 0
        else:
            return 1
        
    
        

    

    
