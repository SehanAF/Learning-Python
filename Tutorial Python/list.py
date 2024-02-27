# list = used to store multiple items in a single variable

food = ["pizza", "cheese", "chicken", "leaf", "tomato"]

food[0] = "sushi"

food.append("ice cream")
food.remove("tomato")
food.pop()
food.insert(1, "cake")
food.sort()
food.clear()

for i in food:
    print(i)