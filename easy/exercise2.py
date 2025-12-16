# Ask the user for a number. Depending on whether the number is even or odd,
#  print out an appropriate message to the user.
#  Hint: how does an even / odd number react differently when divided by 2?
# Extras:
# If the number is a multiple of 4, print out a different message.
#  Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
#  If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

# Even / Odd check
num = int(input("Enter a number to check if it is odd or even: "))

if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

if num % 4 == 0:
    print("The number is also a multiple of 4.")

num = int(input("Enter a number : "))
check = int(input("Enter a number to divide by : "))

if check == 0:
    print("You cannot divide by zero.")
elif num % check == 0:
    print(f"{num} divides evenly by {check}. Result = {num // check}")
else:
    print(f"{num} does NOT divide evenly by {check}.")

