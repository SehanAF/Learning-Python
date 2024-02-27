# set = collections which is unordered, unindexed. No duplicate values

utensils = {"fork", "spoon","knife"}
dishes = {"bowl", "plate","cup", "knife"}

# utensils.add("napkin")
# utensils.add("fork")
# utensils.remove("spoon")
# utensils.clear()

# menggabungkan 2 set menjadi 1 set
# dishes.update(utensils)

# menggabungkan 2 set menjadi 1 set baru
# dinner_table = utensils.union(dishes)

# mencari perbedaan antara 2 set
# print(utensils.difference(dishes))

print(utensils.intersection(dishes))

for x in dishes:
    print(x)