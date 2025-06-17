def bubble_sort(list_to_sort): # O(1)

  for outer_index in range(0, len(list_to_sort) - 1): #O(n²)

    has_made_changes = False #O(1)

    for index in range(0, len(list_to_sort) - 1 - outer_index): #O(n²) en el peor caso

      current_element = list_to_sort[index]
      next_element = list_to_sort[index + 1] #O(1)

      print(f'-- Iteracion {outer_index}, {index}. Elemento actual: {current_element}, Siguiente elemento: {next_element}') #O(1) 


      if current_element > next_element: #O(1)
        print('El elemento actual es mayor al siguiente. Intercambiandolos...') #O(1)
        list_to_sort[index] = next_element #O(1)
        list_to_sort[index + 1] = current_element #O(1)
        has_made_changes = True #O(1)


    if not has_made_changes:
      return                 #O(1)


my_test_list = [1, 2, 3, 10, 4, 5, 6, 7, 8]
bubble_sort(my_test_list)

print(my_test_list)