class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, head):
        self.head = head

    def print_structure(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def bubble_sort(self):
        if self.head is None:
            return

        swapped = True
        while swapped:
            swapped = False
            current = self.head
            while current.next is not None:
                if current.data > current.next.data:

                    current.data, current.next.data = current.next.data, current.data
                    swapped = True
                current = current.next



third_node = Node("Soy el tercer nodo")
first_node = Node("Soy el primer nodo", third_node)
second_node = Node("Soy el segundo nodo", first_node)

linked_list = LinkedList(second_node)

print("Antes de ordenar:")
linked_list.print_structure()

linked_list.bubble_sort()

print("\nDespués de ordenar:")
linked_list.print_structure()
