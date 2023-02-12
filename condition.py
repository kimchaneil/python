"""if True :
    print("True")
else:
    print("False")
    """
"""if 4<3:
    print("a") #조건이 True일 때 출력
else:
    print("b") #조건이 False일 때 출력
    """
"""value = input("값을 입력 해 주십시오: ")
#input으로 받은 value는 문자열 처리
if int(value) > 80:
    print("80 이상입니다")
else:
    print("80 이하입니다")
"""

value = input("본인의 MBTI를 입력 해 주십시오: ")
value = value.upper()
if value == "INFP":
    print("INFP") #대소문자를 구분하기때문에 값이 나오지 않음
