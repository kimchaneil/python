## 함수
#매개변수(파라미터),인자(인수)
"""
def print_name(name):
    print(f'학생의 이름은 {name} 입니다') #name => 매개변수(파라미터) 

student1 = input("학생1의 이름을 작성해 주십시오:")
print_name(student1)
print_name("아무개") #sutdent1, "아무개" 는 인자(인수)
"""
"""
def print_ex_exstring():
    print('예시 문자열입니다')
print_ex_exstring()
"""

"""
def print_name_age(name,age):
    print(f'이름은 {name}이고 나이는 {age}세 입니다')

print_name_age("아무개","83")
print_name_age() #TypeError: print_name_age() missing 2 required positional arguments: 'name' and 'age' 이라는 오류
"""
"""
def order_coffee(qty,option='hot'): #option에 hot이라는 기본값을 주어진 것 기본값을 지정할 때는 기본값이 없는 파라미터가 앞에 나와야 한다
    print(f'{qty}잔 / {option}')
order_coffee(3,'iced')
order_coffee(3)
order_coffee(option='iced',qty=4) #파라미터를 직접 지정하여 함수를 콜 할 수도 있음
"""

"""
def get_id(email):
    if email.endswith('@test.com'): #endswith라는 함수는 해당 값으로 끝나는지 검증하는 것
        email_id =email.removesuffix('@test.com')
        print(email_id)
        return email_id
    else:
        print('처리할 수 없는 이메일 주소입니다')
"""
#user1_id = get_id('user@test.com') #함수에 return을 통해 값을 반환 받을 때 활용할 수 있는 것
#print(user1_id)