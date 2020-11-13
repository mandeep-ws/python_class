import datetime
mynow=datetime.datetime.now()
print(mynow)
x=10
y=20
z=30
print(x,y,z)
a , b, c = "Hello" , "world", "!!!!"
print(a,b,c)

sum1 = x + x
sum2 = a + a
print(sum1,sum2)


student = [1,2,3,4]

print(student[-1:])


mylist = [[10,20,30], "Hello" , [20,10.5,34]]

print(mylist[1][-3:])

print(sum(student)/len(student))
print(max(student))
student_grades = [9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9,9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9]
print(student_grades.count(9.9))

print(a.lower())

students_grade = {"Mary": 10, "sim": 8.8, "jhon": 9.8}
print(sum(students_grade.values())/ len(students_grade))

day_temperatures = {"morning": 10.5 , "noon": 11.5 , "evening": 8.5}

ok = (2 ,3,4)
print(ok[0])
print(student_grades.append(10), student_grades)

