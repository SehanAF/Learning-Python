# logical operators (and, or, not) = used to check if two or more conditional statements is true

temp = int(input("What is the temperature outside? "))

if temp >= 0 and temp <= 30:
    print("the temperature is good today!")
elif temp <= 0 or temp >= 30 :
    print("the temperature is bad today!")
