## 클래스 - 설계
class Student:
  def __init__(self, name, major, is_graduated):
    self.name = name
    self.major = major
    self.is_graduated = is_graduated

    def study(self):
      print(f'{self.name} 학생은 공부중입니다')

#인스턴스 - 실체화된 사물

student_1 = Student('김찬일','정보보호학전공',False)
print(student_1) #<__main__.Student object at 0x01921D10>라고 나옴

student_1_name = student_1.name
print(student_1_name)