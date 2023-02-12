a = 2
b = 3
print(a+b)
print(a-b)
print(a*b)
print(a/b)

print(a ** b) #제곱
print((a+b)*b) #사칙연산 우선 순위

print(a // b) # 몫
print(a%b) # 나머지

#float (십진 부동 소수점)

x = 0.6
y = 0.3
z = 1
print(x+y) #0.8999999999999 로 나오는 이유는 컴퓨터의 한계 때문임

print(x+z)
#실수 연산을 하게 되면 실수로 결과값이 나옴

price = 123_490_000_000 # 숫자 데이터를 구분하기 위해 3자리 마다 _ 를 이용하여 구분할 수 있음
print(price)
# 상수(contants)
PI = 3.141592 #대문자로 표현 한 상수는 데이터 변경해서는 안된다는 뜻

#문자열-숫자 간 변환

a = 100
b = "100"
c = "0.453"

a = str(a)
b = int(b)
c = float(c)