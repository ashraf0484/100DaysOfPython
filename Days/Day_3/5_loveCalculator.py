 # 🚨 Don't change the code below 👇
print("\n\nWelcome to the Love Calculator!")
name1 = input("\nWhat is your name? \n")
name2 = input("\nWhat is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name = name1.lower()
name += name2.lower()

love = name.count("l")
love += name.count("o")
love += name.count("v")
love += name.count("e")

true = name.count("t")
true += name.count("r")
true += name.count("u")
true += name.count("e")

score = int(str(true) + str(love))

if score <= 10 or score >= 90:
   print(f"\nYour score is {score}, you go together like coke and mentos.") 
elif score >= 40 and score <= 50:
    print(f"\nYour score is {score}, you are alright together.")
else:
    print(f"\nYour score is {score}")
