# OPTION 2 - IMPLEMENT STACK
# DO NOT SHARE

# 2. Implement a growable integer stack (without using container libraries like vector, list, etc.)
#    that satisfies the following requirements:

class Node:
    def __init__(self, data, before_node=None, after_node=None):
        self.data = data
        self.next:Node = after_node
        self.before:Node = before_node

# `push` adds a given value to the top
# `pop`  returns and removes the value at the top
# `peek` returns the value at the top
# `size` returns the count of values
class IntStack:
    def __init__(self):
        # Intializing values for head and end of stack
        self.end = None
        self.head = Node(None, after_node=self.end)

    def push(self, value):
        curr_node = self.head
        while curr_node.next != None:
            curr_node = curr_node.next
        new_node = Node(value, before_node=curr_node)
        curr_node.next = new_node
        self.end = new_node

    
    def pop(self):
        pop_val = self.end.data
        if self.end.before == None:
            return None
        self.end.before.next = None
        self.end = self.end.before
        return pop_val


    def peek(self):
        return self.end.data
    
    def size(self):
        curr_node = self.head.next
        stack_len = 0
        while curr_node != None:
            stack_len += 1
            curr_node = curr_node.next
        return stack_len

    # def return_whole_stack(self):
    #     """
    #     Used to test the program, has no effect on push, pop, peek, and size functions
    #     """
    #     curr_node = self.head.next
    #     items = []
    #     while curr_node != None:
    #         items.append(curr_node.data)
    #         curr_node = curr_node.next
    #     return items

    
