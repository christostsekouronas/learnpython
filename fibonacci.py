nterms = int(input("How many terms? "))

n_1, n_2= 0, 1
count = 0

if nterms <= 0:
    print("Please enter a positive integer")
else if nterms == 1:
    print("Fibonacci sequence upto", nterms, ":")
    print(n_1)
else:
    print("Fibonacci sequence:")
    print(n_1)
    n_th = n_1 + n_2
    n_1 = n_2
    n_2 = n_th
    count += 1

