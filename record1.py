name = input("Enter the students name  : ")
n = int(input("Enter the number of subjects : "))
total = 0
for i in range (1, n+1):
    mark = float(input(f"Enter the marks for the subjects{i} : "))
    total += mark
percentage = total / n
if percentage >= 90:
    grade = "A+"
    performance = "Outstanding"
elif percentage >= 80:
    grade = "A"
    performance = "Excellent"
elif percentage >= 70:
    grade = "B"
    performance = "very good"
elif percentage >= 60:
    grade = "C"
    performance = "Good"
elif percentage >= 50:
    grade = "D"
    performance = "Average"
else:
    grade = "F"
    performance = "Needs improvement"

print("n---Academic Performance---")
print("Students name    :   ",name)
print("Total marks      :   ",total)
print("Percentage       :   ",round(percentage,2), "%")
print("Grade            :   ", grade)
print("Performance      :   ", performance)