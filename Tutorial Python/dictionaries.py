# Dictionaries =    A changeable , unordered collection of unique key:value pairs
#                   Fast because they use hashing, allow us to access a value quickly

capitals = {"Indonesia": "Jakarta", 
            "USA": "Washington",
            "India": "New Delhi",
            "Russia": "Moscow"}

capitals.update({"Germany": "Berlin"})
capitals.update({"USA": "Las Vegas"})
capitals.pop("Indonesia")

#print(capitals["Germany"])
# print(capitals.get("Germany"))
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())

for key,value in capitals.items():
    print(key,value)