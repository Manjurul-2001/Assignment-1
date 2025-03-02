def total_marks(inc1,inc2,att,final):
    avg_inc=(inc1+inc2)/2
    if final>70 or final<0:
        return "Enter the value 0 to 70"
    else:
        marks=avg_inc+att+final
        if marks>=80:
            return "A+",4.00
        elif marks>=75:
            return "A",3.75
        elif marks>=70:
            return "A-",3.5
        elif marks>=65:
            return "B+",3.25
        elif marks>=60:
            return "B",3.00
        elif marks>=55:
            return "B-",2.75
        elif marks>=50:
            return "C+",2.5
        elif marks>=45:
            return "C",2.25
        elif marks>=40:
            return "D",2.00
        else:
            return "F",0.00
file=open('grade.txt')
student_data=[]
for line in file:
    data=line.split()
    roll=int(data[0])
    inc1=float(data[1])
    inc2=float(data[2])
    att=int(data[3])
    final=float(data[4])
    letter_grade,grade_point=total_marks(inc1,inc2,att,final)
    student_data.append([roll,letter_grade,grade_point])
print(f"{'roll':<12}{'lettergrade':<15}{'gradepoint':<15}")
for data in student_data:
    roll,letter_grade,grade_point=data
    print(f"{roll:<12}{letter_grade:<15}{grade_point:<15}")

        
