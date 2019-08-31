stu_id = input('Enter a student id: ')
math_s = int(input('Enter a score of mathematics: '))
sci_s = int(input('Enter a score of Science: '))
eng_s = int(input('Enter a score of  English: '))

total = math_s+sci_s+eng_s
avg = (math_s+sci_s+eng_s)/3
print("Student ID: ",stu_id)
print("Mathematics = ",math_s)
print("Science = ",sci_s)
print("English = ",eng_s)
print("Total = ",total)
print("Average = %.2f"%(avg))

if(avg > 60 and eng_s >= 70):
    print("The exam  result = PASS")
else:
    print("The exam  result = Fail")


