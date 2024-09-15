#Creating a game as similar to Kaun Banega Carorpati
#You can add more questions according to your preference 

from optparse import Option
from random import gammavariate
from secrets import choice


print("""Choose from the following:/n
1 - Start the Game
2 - End the Game""")
choice = int(input("Enter your choice: "))
score = 0
if choice == 1:
    #Question 1
    print("What is the capital to India?")
    print("""1 - Delhi
2 - Jaunpur
3 - Kanpur
4 - Lucknow""")
    Options = int(input("Enter your choice: "))
    if Options == 1:
        print("Correct Answer!/n You earned 10Crore")
        score += 10
    else:
        print("Wrong Answer / You loose 5Crore")
        score -= 5
    #Question 2
    print("Which is the National Animal of India?")
    print("""1 - Owl
2 - Elephant
3 - Lion
4 - Bear""")
    Options = int(input("Enter your choice: "))
    if Options == 3:
        print("Correct Answer!/n You earned 10Crore")
        score += 10
    else:
        print("Wrong Answer / You loose 5Crore")
        score -= 5
    print(f"The total score is: {score} Crore")
elif choice == 2:
    print("You have exited the Kaun banega Carorpati Game")
else:
    print("Enter the valid choice!")
