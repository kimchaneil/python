# 튜플

tup = (1, 20, 40 ) #리스트와 다른점 : 내용을 바꿀 수 없음
#print(tup)
#print(tup[0])
#tup[0] = 100 #TypeError: 'tuple' object does not support item assignment 튜플의 자료구조는 변할 수 없음

#tup = (2, 21 ,42) #tup자체를 다시 선언해서 내용을 바꾸는 것은 가능하다
#print(tup)


#for x in tup:
#  print(x)


##튜플의 값을 리스트로 변환 시키는 과정

#list_1 = list(tup) #리스트로 감싸면 형변환 가능
#print(list_1)

#list_2 = [x for x in tup]
#print(list_2)

"""
list_3 = []
for x in tup:
  list_3.append(x)
  print(list_3)
"""