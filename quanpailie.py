
A = [1,2,3,4]
B = []
def permute(A):
	for i in A:
		A.remove(i)
		A.insert(0,i)
		if A not in B:
			B.append(A)
		else:
			permute(A)
	return B



print(permute(A))
