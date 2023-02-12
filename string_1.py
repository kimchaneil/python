city = "seoul"
print(city)
print(city.upper())

city = city.upper() #city라는 변수에 upper함수가 적용된 것을 다시 선언 하는 격
print(city)

print(city.lower())
city = city.lower() #이렇게 되면 다시 city 변수가 소문자로 돌아가는 것

occupation = "developer  "# "developer" 와는 다른 것
#공백 처리 함수
print(occupation)
occupation.rstrip()
print(occupation.rstrip()) #우측 공백 지우기
occupation.lstrip() # 좌측 공백 지우기
print(occupation.lstrip())
occupation.strip() #앞 뒤 공백을 다 지우는 함수
