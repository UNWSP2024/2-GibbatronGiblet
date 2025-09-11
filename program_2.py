
def average_age():
    # Get User Input
    Age_1 = float(input("What is you first friend's age?"))
    Age_2 = float(input("What is you second friend's age?"))
    Age_3 = float(input("What is you third friend's age?"))
    Age_4 = float(input("What is you fourth friend's age?"))
    Age_5 = float(input("What is you fifth friend's age?"))

    # Sum ages
    Average_friend_age = (Age_1 + Age_2 + Age_3 + Age_4 + Age_5) / 5
    # Average the ages

    print("You friends' average age is:", Average_friend_age)
    # Print the results
average_age()
# Line which calls the above function.
# Written by Logan Gibson on 9/9/25
# This program is titled "Average Friend Age"
