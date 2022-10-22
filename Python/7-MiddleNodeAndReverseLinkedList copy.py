# Problem 1: Given a standard linked list, construct an in-place algorithm thats able to find the middle node
# Problem 2: Given a standard linked list, construct an in-place algorithm thats able to reverse it

class Node:

    def __init__(self, data):
        self.data = data
        self.next_node = None

    def __repr__(self):
        return str(self.data)


class LinkedList:

    def __init__(self):
        # this is the first node of the linked list
        # WE CAN ACCESS THIS NODE EXCLUSIVELY !!!
        self.head = None
        self.num_of_nodes = 0

    # O(1) constant running time
    def insert_start(self, data):
        self.num_of_nodes += 1
        new_node = Node(data)

        # the head is NULL (so the data structure is empty)
        if self.head is None:
            self.head = new_node
        # so this is when the linked list is not empty
        else:
            # we have to update the references
            new_node.next_node = self.head
            self.head = new_node

    # Problem 1: N / 2 => O(N)
    def get_middle_node(self):
      fast_pointer = self.head
      slow_pointer = self.head

      while fast_pointer.next_node and fast_pointer.next_node.next_node:
        fast_pointer = fast_pointer.next_node.next_node
        slow_pointer = slow_pointer.next_node
      
      return slow_pointer

    def get_middle_node_2(self):
      count = 0
      node = self.head
      while (count < self.num_of_nodes // 2):
        count+=1
        node = node.next_node

      return node

    # Problem 2: Reverse a LinkedList in O(N)
    def reverse(self):
        current_node = self.head
        previous_node = None
        next_node = None

        while current_node: # is not None
            next_node = current_node.next_node
            current_node.next_node = previous_node        
            previous_node = current_node
            current_node = next_node

        self.head = previous_node

    # O(N)
    def insert_end(self, data):
        self.num_of_nodes += 1
        new_node = Node(data)

        # check if the linked list is empty
        if self.head is None:
            self.head = new_node
        else:
            # this is when the linked list is not empty
            actual_node = self.head

            # this is why it has O(N) linear running time
            while actual_node.next_node is not None:
                actual_node = actual_node.next_node

            # actual_node is the last node: so we insert the new_node
            # right after the actual_node
            actual_node.next_node = new_node

    # O(1) constant running time
    def size_of_list(self):
        return self.num_of_nodes

    # O(N) linear running time
    def traverse(self):

        actual_node = self.head

        while actual_node is not None:
            print(actual_node)
            actual_node = actual_node.next_node

    # O(N) linear running time
    def remove(self, data):

        # the list is empty
        if self.head is None:
            return

        actual_node = self.head
        # we have to track the previous node for future pointer updates
        # this is why doubly linked lists are better - we can get the previous
        # node (here with linked lists it is impossible)
        previous_node = None

        # search for the item we want to remove (data)
        while actual_node is not None and actual_node.data != data:
            previous_node = actual_node
            actual_node = actual_node.next_node

        # search miss
        if actual_node is None:
            return

        # update the references (so we have the data we want to remove)
        # the head node is the one we want to remove
        if previous_node is None:
            self.head = actual_node.next_node
        else:
            # remove an internal node by updating the pointers
            # NO NEED TO del THE NODE BECAUSE THE GARBAGE COLLECTOR WILL DO THAT
            previous_node.next_node = actual_node.next_node


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insert_end(10)
    linked_list.insert_end(20)
    linked_list.insert_end(30)
    linked_list.insert_end(40)
    linked_list.insert_end(50)    
    # linked_list.insert_start(100)
    # linked_list.insert_start(1000)
    # linked_list.insert_end('Adam')
    # linked_list.insert_end(7.5)
    # linked_list.traverse()
    # print('-------')
    # linked_list.remove(1000)
    # linked_list.traverse()
    
    print(linked_list.get_middle_node().data)
    print(linked_list.get_middle_node_2().data)
    print('-------')
    linked_list.reverse()
    print(linked_list.traverse())
