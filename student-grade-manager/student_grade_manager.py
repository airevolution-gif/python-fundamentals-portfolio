def calculate_average(grades):
    return sum(grades) / len(grades)


def get_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


students = {}

print("Student Grade Manager")
print("----------------------")

while True:
    name = input("\nEnter student name (or 'done' to finish): ")

    if name.lower() == "done":
        break

    grades = []

    for i in range(3):
        while True:
            try:
                grade = float(input(f"Enter grade {i + 1}: "))

                if 0 <= grade <= 100:
                    grades.append(grade)
                    break
                else:
                    print("Please enter a grade between 0 and 100.")

            except ValueError:
                print("Please enter a valid number.")

    students[name] = grades


print("\nStudent Results")
print("----------------------")

for name, grades in students.items():
    average = calculate_average(grades)
    letter_grade = get_grade(average)

    print(f"\nStudent: {name}")
    print(f"Grades: {grades}")
    print(f"Average: {average:.2f}")
    print(f"Final Grade: {letter_grade}")

print("\nProgram finished.")
