def sum_to_k(lst ,k):
	j = len(lst) - 1
	i = 0
	while i < j and i != j:
		if lst[i] + lst[j] < k:
			i += 1
		elif lst[i] + lst[j] > k:
			j -= 1
		else:
			return True
	return False
