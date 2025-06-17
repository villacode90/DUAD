#generate_list_trios
def generate_list_trios(list_a, list_b, list_c):                                      #O(1)
	result_list = []                                                                  #O(1)
	for element_a in list_a:                                                          #O(1)
		for element_b in list_b:                                                      #O(m)
			for element_c in list_c:                                                  #O(k)
				result_list.append(f'{element_a} {element_b} {element_c}')            #O(1) por iteración

	return result_list                                                                #O(n × m × k)