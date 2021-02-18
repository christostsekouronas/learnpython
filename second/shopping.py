shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

for item in shopping_list:
    if item != "spam":
        print("Buy " + item)

# a different way to write the lines 3-5:

for item in shopping_list:
    if item == "spam":
        continue

    print("Buy " + item)