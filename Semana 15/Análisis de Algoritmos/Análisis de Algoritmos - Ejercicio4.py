#- **print_10_or_less_elements**
def print_10_or_less_elements(list_to_print):    #O(1)
	list_len = len(list_to_print)                #O(1)
	for index in range(min(list_len, 10)):       #O(1) (máximo 10)
		print(list_to_print[index])              #	O(1) por iteración