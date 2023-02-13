#리스트(list)

mbti = ['INFP','ENFP','ISTJ','ESTP'] #리스트 생성
print(mbti)
print(mbti[1]) #ENFP가 나오는 이유는 컴퓨터에서는 0부터 카운트 함

mbti[0] = 'INFJ' #특정 index의 값을 변환 할 수 있음
print(mbti[0])

my_list =[123,'apple'] #자료형의 구분이 없음
print(my_list)

#color = ['red','blue','green']
##수정
#color[0] = 'black'
#print(color)
##추가
#color.append('purple') #append는 리스트의 마지막에 추가하는 방식
#print(color)
#color.insert(2,'yellow') #insert는 리스트 원하는 위치에 넣을 때
#print(color)
##제거
#del color[0] #del은 index값을 넣어 삭제하는 방식
#print(color)
#delcolor = color.pop(0) #del과 pop의 차이는 값을 반환하여 사용자가 사용 가능한 형태로 만들어 주는가 의 차이 
#print(color)
#print(delcolor) #pop된 data가 변수 delcolor에 저장되는 것
#color.remove('red') #특정한 값(data)를 지정해서 삭제하는 방식
#print(color)


colors =['blue','red','gray','black','yellow','orange']
##리스트 정렬
#colors.sort() #원본의 데이터가 정렬된 상태로 변경되어 버림
#print(colors)
#colors.sort(reverse=True) # 역순 정렬
#print(colors)
#sorted(colors) #기존 배열을 코드에서만 변환하고 원본의 데이터는 살림
#print(colors)
#print(sorted(colors,reverse=True))

#리스트 길이 - 요소의 개수
#print(len(colors))
#print(colors[8]) #IndexError: list index out of range 라는 오류 발생 {마지막 인덱스 참조하려할 때 생기는 오류로 colors[-1]이라고 작성하는 것이 편함}


##리스트 슬라이싱
#print(colors[1:5]) #실제로는 colors[1]-colors[4]까지
#print(colors[:4]) 
#print(colors[2:]) #colors[2]부터 끝까지
#print(colors[-1])
#print(colors[-3])
#print(colors[-5:])
#colors_2 = colors[:] #범위를 지정해서 리스트 변수로 지정할 수 있음
#colors_2 = colors로 하면 같은 메모리 공간을 참조하기 때문(colors을 변경해도 colors_2에 영향을 받음)
#print(colors_2)
scores=[80,100,96,43,60,74]
#scores.sort(reverse=True)
#print(scores)
##리스트 흐름과 제어
"""
for score in scores :
  if score >= 80:
    print(score)
  else:
    print("fail")
"""
##최대값 최소값

max_val = max(scores)
min_val = min(scores)
sum_val = sum(scores) #for문으로도 구할수는 있으나 너무 길어짐
print(max_val,'',min_val,'',sum_val)
avg_val = sum(scores) / len(colors)
print(avg_val)
