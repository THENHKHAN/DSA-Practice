from typing import *
class Node :# our node will contains only two things value and next pinter which can  point to either null or next node's address
    def __init__(self, val) -> None:
        self.val = val 
        self.next = None # or null
    
# now lets create Linked list (SLL):
class LinkedList:
    # initially linked list will be empty until a new node is created
    def __init__(self) -> None:
        self.head = None
        self.count = 0 # this will tell the number of nodes in the linked list. Zero initially since head is at null so empty linked list.

    def __len__(self): # length Of SLL
        return self.count 



l1 = LinkedList() # linked list created.
print(len(l1))# 0: initially zero since head is pointing to null.

# empty linked list means there is no nodes available whihc means headshould  point to null/None
# collection or one(or more) node called linked list
# length of linked list is number of nodes in the linked list.

# MAIN Operation on SLL:
'''
1- Insert 
2- Traversal
3- Delete
4- Search

'''