sampleString=input("Enter any String:")
result=sampleString[len(sampleString)::-1]
print("Reversed string:"+ result)

name=input("Enter student's name:")
age=int(input("Enter age:"))
marks1=float(input("Enter marks of subject1:"))
marks2=float(input("Enter marks of subject2:"))
marks3=float(input("Enter marks of subject3:"))
marks4=float(input("Enter marks of subject4:"))
marks5=float(input("Enter marks of subject5:"))
avgMarks=(marks1+marks2+marks3+marks4+marks5)/5
print( "Average Marks is:",avgMarks) 
percent=((marks1+marks2+marks3+marks4+marks5)/500)*100
if (percent < 50):
     print("Fail")
else:
     print("Pass")





