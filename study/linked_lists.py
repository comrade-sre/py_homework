#!/usr/bin/env python3
class EmptyList(Exception):
      def __init__(self, message, exit_code):
         self.message = message
         self.exit = exit_code
         print(message)
         exit(self.exit)
class Node(object):
      def __init__(self, data=None, next=None):
         self.data = data
         self.next = next
class List(object):
    def __init__(self, name):
        self.name = name
        self.head = None
    def insertNode(self, data, next=None):
       new = Node(data, next)
       if not next and not self.head:
          self.head = new
       elif self.head and next:
            current = self.head
            print(f"head is {current}")
            while current.next:
                  if current.next == next:
                     current.next = new
                     print("current node is {current}")
                     print("inserted node is {new}")
                     break
                  current.next = current
            else:
                raise EpmtyList(f"there is  no {next} node in the list", 1)
       elif not self.head and next:
            raise EpmtyList(f"there is  no nodes yet", 2)
       else: # head is exists and next equal None
           current = self.head
           while current.next:
               current = current.next
           current.next = new

    def searchNode(self, data):
        if self.head:
           current = self.head
           while current:
                 for val  in current.data.values():
                     if data == val:
                        return current.data
                 current = current.next
        else:
            raise EmptyList("there is an empty list", 3)
    def removeNode(self, data):
        if self.head:	
           current = self.head
           prev = None
           while current:
                 for val in current.data.values():
                     if data == val:
                         if current.next and prev:
                             prev.next = current.next
                         elif self.head == current:
                              self.head = current.next
                         else: #prev exixsts and currnet.next is None(in case of tail of the list)
                             prev.next = None
                 current, prev = current.next, current
        else:
            raise EmptyList("there is an empty list", 3)
                        
# test
employees = List("test")
employees.insertNode({"name": "Andrei", "position": "SRE", "age": "30"})
employees.insertNode({"name": "Artem", "position": "SRELead", "age": "36"})
employees.insertNode({"name": "Roman", "position": "SRE", "age": "29"})
print("search method test\n", employees.searchNode("Artem"))
employees.removeNode("Roman")
node = employees.head
while node:
    print(node.data)
    node = node.next

