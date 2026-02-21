print("Student result calculator")

name = input("enter student name:")

m1 = int(input("enter the marks of subject 1:"))
m2 = int(input("enter the marks of subject 2:"))
m3 = int(input("enter the marks of subject 3:"))
m4 = int(input("enter the marks of subject 4:"))
m5 = int(input("enter the marks of subject 5:"))

total = m1+m2+m3+m4+m5
percentage = total/5

if m1<35 or m2<35 or m3<35 or m4<35 or m5<35:
    result = "fail"
    grade = "F"
else:
    result="pass"
    grade = "pass"

    if percentage>=90:
        result = "pass"
        grade = "A+"
    elif percentage>=80:
        result = "pass"
        grade = "A"
    elif percentage>=70:
        result = "pass"
        grade = "B"
    elif percentage>=60:
        result = "pass"
        grade = "C"
    else:
        grade = "E"
print("the name is :",name)
print("total marks is :",total)
print("percentage is :",percentage)
print("result is :",result)
print("grade is :",grade)


