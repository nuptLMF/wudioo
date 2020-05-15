def zeros(n):
	if n/5 != 0:
		return int(n/5 +zeros(n/5))
	else:
		return n/5
def main():
	print(zeros(444))

if __name__=='__main__':
	main()

