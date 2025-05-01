# 1. Cree una estructura de objetos que asemeje un Stack.
#     1. Debe incluir los métodos de `push` (para agregar nodos) y `pop` (para quitar nodos).
#     2. Debe incluir un método para hacer `print` de toda la estructura.
#     3. No se permite el uso de tipos de datos compuestos como `lists`, `dicts` o `tuples` ni módulos como `collections`.

from typing import Any

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
    
    def push(self, data: Any) -> None:
        node = Node(data)
        node.next = self.top
        self.top = node
        self.size += 1

    def pop_element(self):
        if self.top:
            node_removed = self.top.data
            self.top = self.top.next
            self.size -= 1
            return node_removed
        else:
            print("The stack is empty...")
            return None
    
    def show_stack(self):
        if self.top is None:
            print("The stack is empty...")
        else:
            iterator = self.top
            while iterator:
                print(iterator.data)
                iterator = iterator.next

if __name__ == "__main__":
    pancakes = Stack()

    pancakes.push("Pancake 1")
    pancakes.push("Pancake 2")
    pancakes.push("Pancake 3")

    pancakes.show_stack()

    print("\nPopped:", pancakes.pop_element())
    pancakes.show_stack()

    print("\nPopped:", pancakes.pop_element())
    pancakes.show_stack()

    print("\nPopped:", pancakes.pop_element())
    pancakes.show_stack()
