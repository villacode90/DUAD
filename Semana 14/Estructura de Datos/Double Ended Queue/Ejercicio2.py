# 2. Cree una estructura de objetos que asemeje un Double Ended Queue.
#     1. Debe incluir los métodos de `push_left` y `push_right` (para agregar nodos al inicio y al final) y `pop_left` y `pop_right` (para quitar nodos al inicio y al final).
#     2. Debe incluir un método para hacer `print` de toda la estructura.
#     3. No se permite el uso de tipos de datos compuestos como `lists`, `dicts` o `tuples` ni módulos como `collections`.

class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None  
        self.prev = None  

class Deque:
    def __init__(self):
        self.head = None  
        self.tail = None  
        self.size = 0      
    
    def push_left(self, data):
        node = Node(data)  
        if self.head is None:  
            self.head = node
            self.tail = node
        else:
            node.next = self.head  
            self.head.prev = node  
            self.head = node       
        self.size += 1  

    def push_right(self, data):
        node = Node(data)  
        if self.tail is None:  
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail  
            self.tail.next = node  
            self.tail = node       
        self.size += 1  

    def pop_left(self):
        if self.head is None:  
            print("Deque is empty...")
            return None
        node_removed = self.head  
        self.head = self.head.next  
        if self.head: 
            self.head.prev = None  
        else:
            self.tail = None  
        self.size -= 1  
        return node_removed.data  

    def pop_right(self):
        if self.tail is None:  
            print("Deque is empty...")
            return None
        node_removed = self.tail  
        self.tail = self.tail.prev  
        if self.tail:  
            self.tail.next = None  
        else:
            self.head = None  
        self.size -= 1  
        return node_removed.data  

    def show_deque(self):
        if self.head is None:  
            print("Deque is empty...")
        else:
            current = self.head  
            while current:  
                print(current.data)  
                current = current.next  

if __name__ == "__main__":
    dq = Deque()

    dq.push_left(1)  
    dq.push_right(2) 
    dq.push_left(3)
    dq.push_right(4)
    dq.push_left(5)  

    dq.show_deque()  

    print("\nPopped from left:", dq.pop_left())  
    dq.show_deque()  

    print("\nPopped from right:", dq.pop_right())  
    dq.show_deque()  