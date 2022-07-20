# Library containting Node, Linked List, Doubly Link List, Stack and Queue data structures
from multiprocessing import current_process


class Node:

    def __init__(self, value=None):
        self.value = value
        self.next_node = None        
    
    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node


class LinkedList:

    def __init__(self, head=None):
        self.head = head

    def peek(self):
        return self.head.get_value()

    def insert(self, value):

        payload = Node(value)
        current_node = self.head
        if current_node is None:
            self.head = payload
        else:
            while current_node is not None:
                if current_node.get_next_node() is None:
                    current_node.set_next_node(payload)
                    return
                else:
                    current_node = current_node.get_next_node()
            return                
    
    
    def remove(self, value):
        
        current_node = self.head
        if current_node is None:
            return
        
        prev_node = None
        while current_node is not None:
            if prev_node is None:
                if current_node.get_value() == value and current_node.get_next_node() == None:
                    self.head = None
                    return
                if current_node.get_value() == value:
                    next_node = current_node.get_next_node()
                    current_node = None
                    self.head = next_node
                    return
            else:
                if current_node.get_value() == value:
                    prev_node.set_next_node(current_node.get_next_node())
                    current_node = None
                    return
            
            prev_node = current_node
            current_node = current_node.get_next_node()

    
    def stringify_list(self):
        string_res = ''
        current_node = self.head
        while current_node is not None:
            value = current_node.get_value()
            if value != None:
                string_res += str(value) + '\n'
            current_node = current_node.get_next_node()
        return string_res    
    
    

        
        


    
        



