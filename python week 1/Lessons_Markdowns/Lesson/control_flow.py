# Control Flow- Control the flow of your code- make decisions

#if/ elif/ else

# if
age = 4
if age >= 18:
   print("You are old enough to watch this movie")


#elif
elif age < 18:
  print("sorry, you are not old enough to watch this movie")

film_rating = "U"

if film_rating.lower() == "u":
    print("All age groups can watch this movie")
# elif - Less processing power and runs only if if condition is not met.
elif film_rating.lower() == "pg":
    print("Parental guidance is advised for this movie")
elif film_rating.lower() == "12" or "12a":
    print("People over the age of 12 can watch this movie unsupervised")
elif film_rating.lower() == "15":
    print("People aged 15 or over can watch this movie")
elif film_rating.lower() == "18":
    print("People aged 18 can watch this movie")

#else
else:
  print("this is not a valid rating, please use 'u','pg','12','12a'")
