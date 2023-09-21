# create greeting
print("hello customer")

# Print a list starters


starter_list = ["Salad","Prawn Tempura","Spring roll"]
print(starter_list)

# Take an input for their starter
starter_list = input("Please enter your starter of choice")
print("You selected", starter_list)

# Print a list of mains

mains_list = ["T-bone steak","Spaghetti Bolgnese","Vegan Pasta"]
print(mains_list)

# Take an input for their mains
mains_list = input("Please enter your mains of choice")
print("You selected", mains_list)

# Print list of Deserts
desert_list = ["Chocolate cake", "Carrot cake","Apple pie"]
print(desert_list)

# Take an input for their dessert
desert_list = input("Please enter your dessert of choice")
print("You selected, desert_list")

# Print a list of drinks
drink_list =["Coke","Fanta","Sprite"]
print(drink_list)

# Take an input for their drinks
drink_list = input("Please enter your drink of choice")
print("You selected, drink_list")

input("final order of choice")
print("you selected",starter_list,mains_list,desert_list,drink_list)

list = (zip(mains_list,drink_list,drink_list,desert_list))
print(list)