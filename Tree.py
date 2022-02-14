#!/usr/bin/env python3 

import Node as nd


class Tree():
    
    def __str__(self):
        return self.name

    def __init__(self,
        name = None,
        parent = None,
        #has_right = False,
        #is_leaf = True,
        left_child_tree = None, 
        right_child_tree = None, 
        ):
        self.name = name
        self.node = nd.Node(name=name,parent= parent,child_left = left_child_tree, child_right= right_child_tree)


    def search(self,name):
        if(name == self.name):
            return True
        elif(self.name < name):
            if(self.node.has_leftchild()):
                return self.node.get_leftchild().search(name)
            else:
                return False
        elif(self.name > name):
            if(self.node.has_rightchild()):
                return self.node.get_rightchild().search(name)
            else:
                return False

    
    def insert(self,name):
        if(name == self.name):
            print("Already exist! Fail to insert")
        elif(self.name < name):
            if(self.node.has_leftchild()):
                self.node.get_leftchild().insert(name)
            else:
                newtree = Tree(name = name, parent = self.node)
                self.node.child_left = newtree
                #self.node.has_leftchild = True
                
        elif(self.name > name):
            if(self.node.has_rightchild()):
                self.node.get_rightchild().insert(name)
            else:
                newtree = Tree(name = name, parent = self.node)
                self.node.child_right = newtree
                # self.node.has_rightchild = True
    def sort(self):
        if(self.node.has_leftchild()):
            order_left = self.node.get_leftchild().sort()
        else:
            order_left = []
        if(self.node.has_rightchild()):
            order_right = self.node.get_rightchild().sort()
        else:
            order_right = []
        ordered = order_left + [self.name] + order_right
        return ordered

    def print_tree(self):
        print(self.sort())

                

          





    

        
    
        

    

    
