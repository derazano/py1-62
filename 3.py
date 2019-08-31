stu_id = input('Enter a student id: ')
subj_s =  input('Enter a subject: ')
score_s = int(input('Enter a score: '))

if(score_s >= 80):
    print(stu_id,subj_s,"Grade A")
elif(score_s >= 70):
    print(stu_id,subj_s,"Grade B")
elif(score_s >= 60):
    print(stu_id,subj_s,"Grade C")
elif(score_s >= 50):
    print(stu_id,subj_s,"Grade D")
else:
    print(stu_id,subj_s,"Grade F")
