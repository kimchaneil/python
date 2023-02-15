print('=============================')
print('회원가입')
print('=============================')

register = False

while not register:
  print('회원가입을 진행 하시겠습니까?\n y:진행 \t n:취소')
  register_input = input('>> ')
  register_input = register_input.lower()
  if register_input == 'y':
    register = True
    print('=============================')
    print('회원가입이 진행 됩니다')
    print('=============================')
  elif register_input == 'n':
    print('=============================')
    print('회원가입이 취소 됩니다')
    print('=============================')
    exit()

print('입력 값을 확인해주세요')

users = []

while True:
  user = {}

  username = input('ID: ')
  while True:
    password = input('PW: ')
    password_confirm = input('PW확인: ')
    if password == password_confirm:
      break
    else:
      print('비밀번호가 일치하지 않습니다. ')
  name = input('이름')
  while True:
    birth_date = input('생년월일(YYMMDD): ')
    if len(birth_date) ==6:
      break
    else:
      print('생년월일의 양식이 맞지 않습니다')
  email = input('이메일: ')
  user['username'] = username
  user['password'] = password
  user['name'] = name
  user['birth_date'] = birth_date
  user['email'] = email

  users.append(user)
  print(user)

  print("==========================")
  print(f"{user['name']}님 가입을 환영합니다!")
  print("==========================")

  print('회원가입을 추가로 진행하시겠습니까?')
  ending = input('\n y: 진행\t n: 정지\n >>')
  ending = ending.lower()
  if ending == 'ny':
    exit()
  else:
    pass