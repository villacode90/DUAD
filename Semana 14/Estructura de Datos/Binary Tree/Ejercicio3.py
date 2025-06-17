# <!-- 3. Cree una estructura de objetos que asemeje un Binary Tree.
#     1. Debe incluir un método para hacer `print` de toda la estructura.
#     2. No se permite el uso de tipos de datos compuestos como `lists`, `dicts` o `tuples` ni módulos como `collections`. -->

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)

#Metodo para impresión simple. (in order traversal)

    # def print_tree(self):
    #     if self.left is not None:
    #         self.left.print_tree()
    #     print(self.data)
    #     if self.right is not None:
    #         self.right.print_tree()

#Metodo para impresión jerárquica

    def print_tree(self, level=0):
        if self.right is not None:
            self.right.print_tree(level + 1)
        print('    ' * level + str(self.data))
        if self.left is not None:
            self.left.print_tree(level + 1)

# Creating Tree
root = Node('g')
root.insert('c')
root.insert('b')
root.insert('a')
root.insert('e')
root.insert('d')
root.insert('f')
root.insert('i')
root.insert('h')
root.insert('j')
root.insert('k')

# Printing Tree
root.print_tree()
