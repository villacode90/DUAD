#check_if_lists_have_an_equal
def check_if_lists_have_an_equal(list_a, list_b): #O(1)
	for element_a in list_a:                      #O(n) (n = len(list_a))
		for element_b in list_b:                  #O(m) (m = len(list_b))
			if element_a == element_b:            #O(1)
				return True                       #O(1)
				
	return False                                  #O(1)