## 클래스 - 설계
class Student:
  def __init__(self, name, major):
    self.name = name
    self.major = major
    self.is_graduated = False

  def study(self):
    print(f'{self.name} 학생은 공부중입니다')

  #인스턴스 변환방법
  def edit_major(self,new_major):
    student_1.major = new_major
    print(f'{student_1.major}로 변경되었습니다.')

#인스턴스 - 실체화된 사물

student_1 = Student('김찬일','정보보호학전공')
"""print(student_1) #<__main__.Student object at 0x01921D10>라고 나옴"""
##인스턴스 변환 방법
#student_1.major = '철학과'
#print(student_1.major)

#student_1.edit_major('철학과') #함수를 통한 변경


# student_1.study()
#student_1_name = student_1.name
#student_1_graduated = student_1.is_graduated
#print(student_1_name)
#print(student_1_graduated)


##상속 (Inheritance)
class ForeignStudent(Student):
  def __init__(self,name,major,country):
    super().__init__(name,major) #4~6번째 내용을 가져오는것
    self.country = country
  def study(self): #오버라이딩 : 상속 부모의 함수를 변경하여 사용하는 것
    print(f'{self.name} is studying now')
foreign_1 = ForeignStudent('paul', '국어 국문 학과','USA')

#print(foreign_1.name)
#print(foreign_1.major)
#print(foreign_1.is_graduated)
#print(foreign_1.country)
#foreign_1.study()