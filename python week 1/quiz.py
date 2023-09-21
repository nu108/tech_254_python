# Python quiz

question = ("What is the largest country in the world? :" ,
            "How many bones are their in a human body? :" ,
            "How many planets are there in the solar system ?:",
            "Whats the most eaten food in the world?:",
            "Which country has the tallest building in the world?: ")

options = (("A. Russia","B. India","C. United Kingdom","D. China"),
           ("A. 206", "B. 209", "C. 208", "D. 205"),
           ("A. 8", "B. 9", "C. 6", "D. 5"),
           ("A. Chicken", "B. Rice", "C. Pasta", "D. Lamb"),
           ("A. Dubai", "B. Saudi Arabia", "C. China", "D. United Kingdom"))




answers = ("A","A", "A", "B","A")
guesses = []
score = 0
question_num = 0

for questions in question:
    print("--------------------")
    print(question)

    for option in options [question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")

    else:
        print("INCORRECT")
        print(f"{answers[question_num]} is the correct answer")


    question_num += 1

print("---------------")
print("   RESULTS     ")
print("---------------")

print("answers: ", end="")
for answer in answers:
    print(answers, end=" ")
print()

print("guesses: ", end="")
for guess in guesses :
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")