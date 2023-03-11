import hashlib

def main():
	tmp = "".join([hashlib.sha256(b"ANDERSON").hexdigest()[x] for x in [4, 5, 3, 6, 2, 7, 1, 8]])
	print(tmp)

if __name__ == '__main__':
	main()
