questions = [
    {
        "question": "What is the correct file extension for a Python file?",
        "options": ["A. .java", "B. .py", "C. .html", "D. .cpp"],
        "answer": "B"
    },
    {
        "question": "Which keyword is used to create a function in Python?",
        "options": ["A. function", "B. define", "C. def", "D. func"],
        "answer": "C"
    },
    {
        "question": "Which data type stores multiple values in an ordered collection?",
        "options": ["A. List", "B. Integer", "C. Boolean", "D. Float"],
        "answer": "A"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["A. //", "B. <!-- -->", "C. #", "D. **"],
        "answer": "C"
    },
    {
        "question": "What does len() do?",
        "options": [
            "A. Deletes data",
            "B. Counts the number of items",
            "C. Converts data",
            "D. Prints data"
        ],
        "answer": "B"
    }
]


def show_question(question_number, question):
    print(f"\nQuestion {question_number}")
    print(question["question"])

    for option in question["options"]:
        print(option)


def run_quiz():
    score = 0

    print("Python Quiz")
    print("--------------------")
    print("Answer each question by entering A, B, C, or D.")

    for number, question in enumerate(questions, start=1):
        show_question(number, question)

        while True:
            answer = input("Your answer: ").strip().upper()

            if answer in ["A", "B", "C", "D"]:
                break

            print("Please enter A, B, C, or D.")

        if answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer was {question['answer']}.")

    print("\nQuiz Finished")
    print("--------------------")
    print(f"Your score: {score}/{len(questions)}")

    percentage = (score / len(questions)) * 100
    print(f"Percentage: {percentage:.1f}%")

    if percentage >= 80:
        print("Great job!")
    elif percentage >= 60:
        print("Good effort!")
    else:
        print("Keep practicing Python!")


while True:
    run_quiz()

    again = input("\nWould you like to play again? (yes/no): ").strip().lower()

    if again != "yes":
        print("Thanks for playing.")
        break
