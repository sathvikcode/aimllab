name = input("Enter Student Name: ")
marks = [float(input(f"Enter Marks in Subject {i}: ")) for i in range(1, 6)]

total = sum(marks)
percentage = total / 5

print("Name:", name)
print("Total:", total)
print("Percentage:", percentage)

if min(marks) < 35:
    print("Status: FAIL")
else:
    print("Status: PASS")
    if percentage >= 90:
        print("Grade: O")
        print("Scholarship: Eligible")
    elif percentage >= 80:
        print("Grade: A+")
    elif percentage >= 70:
        print("Grade: A")
    elif percentage >= 60:
        print("Grade: B")
    elif percentage >= 50:
        print("Grade: C")
    else:
        print("Grade: D")
