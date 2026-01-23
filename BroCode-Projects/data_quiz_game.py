questions = (
    "Which role is the one who build Data Pipeline?",
    "Where is the messiest place that store data?",
    "What is the meaning of 'L' in ETL?",
    "Which programing language is the greatest for query the data?",
    "What is the second step of Data Science Cycle?"
)

options = (
    ("A. Data Engineer", "B. Data Scientist", "C. Data Analyst", "D. AI Engineer"),
    ("A. Database", "B. Data Lake", "C. Data Warehouse", "D. Data Mart"),
    ("A. List", "B. Loop", "C. Load", "D. Link"),
    ("A. Python", "B. C++", "C. R", "D. SQL"),
    ("A. Transform", "B. Visualize", "C. Cleaning", "D. Collect")
)

answers = ("A", "B", "C", "D", "D")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT")
    else:
        print("INCORRECT")
        print(f"{answers[question_num]} is the correct answer")

    question_num += 1

print("----------------------------------")
print("             RESULTS              ")
print("----------------------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")