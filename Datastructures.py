
# ------------------Stack Data Structure in Python--------------

# class Stack():
#     def __init__(self):
#         self.items = []

#     def push(self, data):
#         self.items.append(data)
    
#     def pop(self):
#         return self.items.pop()

#     def get_stack(self):
#         return self.items

#     def is_empty(self):
#         return self.items == []


#     def peek(self, index):
#         return self.items[index]

#     def length(self):
#         return len(self.items)

# s1 = Stack()
# s1.push(5)
# s1.push(4)
# print(s1.get_stack())
# print(s1.is_empty())

#-------------------------------------------------------------------------------------------------- 
# 2) ------------------------------------LinkedList in Python-------------------------------------

# Create Node class
# class Node:
#     def __init__(self, data=None):
#         self.data = data
#         self.next = None

# # Create LinkedList class
# class LinkedList:
#     def __init__(self):
#         self.head = Node()

#     def append(self, data):
#         new_node = Node(data)
#         cur = self.head
#         while cur.next != None:
#             cur = cur.next
#         cur.next = new_node
            
#     def length(self):
#         cur = self.head
#         total = 0
#         while cur.next!= None:
#             total += 1
#             cur = cur.next
#         return total
    
#     def display(self):
#         elems = []
#         cur = self.head
#         while cur.next!= None:
#             cur = cur.next
#             elems.append(cur.data)
#         print(elems)

#     def get(self, index):
#         if index >= self.length():
#             return "Error : List index out of range"
#         cur = self.head
#         count = 0
#         while cur.next!= None:
#             cur = cur.next
#             if count == index: return cur.data
#             count += 1
        
#     def remove(self, nod):
#         if nod >= self.length():
#             print("Error : List index out of range")
#             return 
#         cur = self.head
#         count = 0
#         while True:
#             last_node = cur
#             cur = cur.next
#             if count == nod:
#                 last_node.next = cur.next
#                 return 
#             count += 1
                  


# List1 = LinkedList()
# List1.append("Rajesh")
# List1.append(23)

# # List1.display()
# # print(List1.length())
# List1.append(22)
# List1.append(24)
# List1.append(25)
# List1.append(26)

# List1.display()
# print(List1.get(4))
# List1.remove(5)
# List1.remove(4)
# List1.display()

# ---------------------------------------------------------------------------------------

