# slicing = create a substring by extracting elemnts from another string
#           indexing[] or slice()
#           [start:stop:step]

name = "Sehan AF"

first_name = name[: 5]
last_name = name[6:]
funcky_name = name[::2]
reversed_name = name[::-1]

print(first_name)
print(last_name)
print(funcky_name)
print(reversed_name)

#----------------------------------------------------------------#

website = "https://www.google.com"
website2 = "https://www.youtube.com"

slice = slice(12, -4)

print(website[slice])
print(website2[slice])