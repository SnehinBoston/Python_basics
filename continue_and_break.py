for number in range(10):
    if number > 5:
        break
    print(number)

scores = [90, 30, 50, 70, 85, 35]

num_failed_scores = 0
failed_score = 60
needs_tutoring = "No"
for score in scores:
    if score < failed_score:
        num_failed_scores += 1
    if num_failed_scores >= 2:
        needs_tutoring = "Yes"
        break
    
print(f"Does the student need tutoring? {needs_tutoring}")

import random
guesses_left = 4
random_number = random.randint(1, 10)
while True:
    if guesses_left <= 0:
        print(
            "You ran out of guesses! "
            f"The correct number was {random_number}"
        )
        break
    guess = input("Guess a number between 1 and 10, or enter q to quit: ")
    if guess == "q":
        print("Successfully exited game.")
        break
    elif not (guess.isnumeric()):
        print("Please enter a valid value.")
    elif int(guess) == random_number:
        print("Congratulations, you picked the correct number!")
        break
    else:
        print("Sorry, your guess was incorrect.")
        guesses_left -= 1
        print(f"You have {guesses_left} guesses left.")

scores = [
    [90, 30, 80, 100],
    [100, 80, 95, 87],
    [75, 84, 77, 50],
]

failed_score = 60
num_failed_students = 0
for student_score_list in scores:
    for score in student_score_list:
        if score < failed_score:
            num_failed_students += 1
            break
print(f"Number of students who failed a test: {num_failed_students}")

for index in range(6):
    if index % 2 == 0:
        continue
    print(index)



