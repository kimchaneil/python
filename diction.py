#Dictionary

"""student = {
  "student_no" : "20230213",
  "major" : "information secu",
  "grade" : 3
}
"""

#print(student["student_no"]) 
#student["student_no"] = "20220213"
#print(student)
#print(student["student_no"]) 

##추가
#student["gpa"] = 4.5 #마지막에 추가됨
#print(student)


##수정
#student["gpa"] = 4.3
#print(student)

##삭제
#del student["gpa"] 
#print(student)

#print(student.get("major"))
#print(student.get("gpa","해당 키-값 쌍이 없습니다")) #dictionary.get("키","x") x의 자리에는 키에 해당한 키-값쌍이 없다면 x를 출력

##딕셔너리 키를 반환
#print(student.keys())
#print(list(student.keys()))

##딕셔너리의 값을 반환
#print(student.values())
#print(list(student.values()))

##딕셔너리 반복문
tech = {
  "HTML" : "Advanced",
  "JS" : "Intermediate",
  "Python" : "expert",
  "GO" : "Novice"
}
#for i in tech:
#  print(i) #key 값만 포함 시킴
#for key, val in tech:
#  print(f'{key} - "{val}') #ValueError: too many values to unpack (expected 2) 
#for key , val in tech.items():
#  print(f'{key} - {val}')

##중첩(Nesting)
"""student_1 = {
  "student_no" : "1",
  "gpa" : "4.3"
}
student_2 = {
  "student_no" : "2",
  "gpa" : "3.8"
}
"""
#students = [student_1, student_2]
#print(students)

#for student in students:
#  print(student)

"""for student in students:
  student['graduated'] = False #모든 학생의 graduated라는 key에 False라는 vlaue를 부여
  print(student['student_no'])
  print(student)
"""
#student = {
#  "subjects": ["math","programming"]

#}
#print(student["subjects"])
#subjects_list = student["subjects"]
#for subject in subjects_list:
#  print(subject)

##dictionary in dictionary
student = {
  "scholarship" :{
    "name" : "국가장학금",
    "amount" : "100,000"
  }
}
print(student)
print(student["scholarship"])
for key in student.keys():
  print(key)
for val in student.values():
  print(val)
for val in student.values():
  for val_2 in val.values():
    print(val_2)
