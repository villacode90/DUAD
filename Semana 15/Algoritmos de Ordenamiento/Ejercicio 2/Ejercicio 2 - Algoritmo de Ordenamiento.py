#Modifica el bubble_sort para que funcione de derecha a izquierda, ordenando los números menores primero (como en la imagen de abajo).
def reverse_bubble_sort(list_to_sort):
    for outer_index in range(len(list_to_sort) - 1):
        has_made_changes = False

        for index in range(len(list_to_sort) - 1, outer_index, -1):
            current_element = list_to_sort[index]
            previous_element = list_to_sort[index - 1]
            print(f'-- Iteración {outer_index}, {index}. Elemento actual: {current_element}, Elemento previo: {previous_element}')

            if previous_element > current_element:
                print('El elemento previo es mayor al actual. Intercambiándolos...')
                list_to_sort[index] = previous_element
                list_to_sort[index - 1] = current_element
                has_made_changes = True

        if not has_made_changes:
            return

# Prueba
my_test_list = [2, 1, 3, 5, 4, 10, 8, 7, 6]
reverse_bubble_sort(my_test_list)

print(my_test_list)
