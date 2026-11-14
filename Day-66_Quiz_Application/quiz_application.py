print("--- PYTHON QUIZ APPLICATION ---")

questions = [
    {
        "question": "1. which language is used for python programming ?",
        "options": ["A. HTML", "B. Python programming", "C. CSS", "D. SQL"],
        "answer": "B"
    },
    {
        "question": "2. Which symbol is used for comments in Python ?",
        "options": ["A. //", "B. /", "C. #", "D. @"],
        "answer": "C"
    },
    {
        "question": "3. Which data type stores True or False ?",
        "options": ["A. string", "B. Integer", "C. List", "D. Boolean"],
        "answer": "D"
    },
    {
        "question": "4. Which keyword is used to create a function ?",
        "options": ["A. def", "B. function", "C. create", "D. fun"],
        "answer": "A"
    },
    {
        "question": "5. Which fuction is used to find length ?",
        "options": ["A. count()", "B. len()", "C. size()", "D. length()"],
        "answer": "B"
    }
]

score = 0

for q in questions:
    print("\n" + q["question"])
    for option in q["options"]:
        print(option)
    user_answer = input("Enter your answer (A/B/C/D): ").upper()
    if user_answer == q["answer"]:
        print("Correct Answer")
        score += 1
    else:
        print("Wrong Answer")
        print("Correct Answer is", q["answer"])

total = len(questions)
percentage = (score / total) * 100
print("--- Quiz Result ---")
print("Total Questions:", total)
print("Correct Answers:", score)
print("Wrong Answers:", total - score)
print("Your Score:", percentage, "%")

if percentage >= 80:
    print("Excellent Performance")
elif percentage >= 50:
    print("Good Performance")
else:
    print("Keep Practicing")
