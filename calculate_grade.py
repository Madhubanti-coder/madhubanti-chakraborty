def calculate_grade(marks):
    total = sum(marks)
    percentage = (total / (len(marks) * 100)) * 100
    if percentage >= 80:
        grade = 'A'
    elif percentage >= 70:
        grade = 'B'
    elif percentage >= 60:
        grade = 'C'
    elif percentage >= 40:
        grade = 'D'
    else:
        grade = 'E'
    return total, percentage, grade

# Example usage:
marks = []
for i in range(3):
    marks.append(float(input(f"Enter marks for subject {i+1}: ")))
total, percentage, grade = calculate_grade(marks)
print(f"Total Marks: {total}, Percentage: {percentage:.2f}%, Grade: {grade}")