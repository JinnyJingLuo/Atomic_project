#!/usr/bin/env python3 
import Tree as tr
# import Tree class

# initialization test
Tree_A = tr.Tree(15)
# insert test
Tree_A.insert(100)
Tree_A.insert(2)
Tree_A.insert(30)
# test repeated number 
Tree_A.insert(30)

# test search 
print(Tree_A.search(2))
print(Tree_A.search(32))
# test print
Tree_A.print_tree()