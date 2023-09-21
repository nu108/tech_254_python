#get a number from the user
number = int(input("Enter a number: "))

# check if its a multiple of 2 and 5 (FizzBuzz)
if number % 3: == 0 and number % 5: == 0
    print("FizzBuzz")

# check if its a multiple of 2 (Fizz)
elif number % 2: == 0:
    print("Fizz")

# Check if its a multiple of 5 (Buzz)
elif number % 5: == 0:
    print("Buzz")

# if none of the conditions are met print the number itself
else:
    print(number)