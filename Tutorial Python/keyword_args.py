# keywords arguments = argument preceded by an identifier when we pass them to a function
#                      The order of the arguments doesn't matter, unlike positional arguments
#                      Python knows the names of the arguments that our function receives.

def hello(first,middle,last):
    print(f"Hello {first} {middle} {last}")
    
hello(last="Sehun", first="AF", middle="lala")