# when only 20 for exaple is inside range the program starts from 0 and ends to 19 because 0 is the default
for i in range(20):
    print(i)

# begins from 1 and stops to 20
for i in range(1, 20):
    print("i is now {}".format(i))

# begins from 0 goes to 10 with a 2 step
for i in range(0, 10, 2):
    print("i is now {}".format(i))

# begins from 10 goes to 0 with a -2 step
for i in range(10, 0, -2):
    print("i is now {}".format(i))
