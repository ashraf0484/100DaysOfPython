# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

# def greet():
#     print("\n\nHello")
#     print("Hope you are doing good")
#     print("All the best for your future")

# greet()
    
# def greet_with_name(a, b):
#     print(f"\n\nHello {a}")
#     print(f"How is {b} ?")
#     print("All the best for your future")    
    
# name1 = "Beeraan kutty"
# greet_with_name(name1, "Paathumma" )

def greet_with_name(a, b):
    print(f"\n\nHello {a}")
    print(f"How is {b} ?")
    print("All the best for your future")  

name1 = "Beeraan kutty"
# Keyword argument
greet_with_name(b = "Paathumma", a = name1)