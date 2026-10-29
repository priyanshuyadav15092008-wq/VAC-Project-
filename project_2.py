subjects = ["English", "Hindi", "Maths", "Science", "Social Studies"]
marks = []

print("=== Student Marks & Grade Calculator ===")
print("Har subject ke marks 0 se 100 ke beech daalo.\n")

for subject in subjects:
    while True:
        try:
            score = float(input(f"{subject} ke marks: "))
            if 0 <= score <= 100:
                marks.append(score)
                break
            print("Marks 0 se 100 ke beech hone chahiye.")
        except ValueError:
            print("Please valid number daalo.")

total = sum(marks)
percentage = total / len(subjects)

if any(score < 33 for score in marks):
    status = "Fail"
    grade = "F"
elif percentage >= 90:
    status = "Pass"
    grade = "A+"
elif percentage >= 80:
    status = "Pass"
    grade = "A"
elif percentage >= 70:
    status = "Pass"
    grade = "B"
elif percentage >= 60:
    status = "Pass"
    grade = "C"
elif percentage >= 33:
    status = "Pass"
    grade = "D"
else:
    status = "Fail"
    grade = "F"

print("\n=== Result ===")
print(f"Total marks: {total:g} / 500")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")
print(f"Status: {status}")