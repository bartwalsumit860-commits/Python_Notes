#program for student grade calculation

marks = int(input("Enter your Marks: "))

if marks > 90:
    print("A")
elif marks >80:
    print("B")
elif marks > 65:
    print("C")
elif marks > 50:
    print("D")
else:
    print("NC")