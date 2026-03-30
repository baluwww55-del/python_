# projects using python 
marks = int(input("Enter your marks: "))

if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 90:
    print("Grade A+ - Topper mindset")
elif marks >= 75:
    print("Grade A - Strong work")
elif marks >= 50:
    print("Grade B - Decent, push harder")
else:
    print("Fail - Reality check")

# this is the simple marks card grade evaluator using python 