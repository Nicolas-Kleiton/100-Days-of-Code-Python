# Tip Calculator

print("Welcome to the tip calculator!")

total = float(input("What was the total bill? $ "))
tip = int(input("How much tip would you like to give? (10 , 12 or 15) % "))
people = int(input("How many people to split the bill? "))
value = total * tip / 100 + total

print(f"Each person should pay: ${value / people:.2f}")