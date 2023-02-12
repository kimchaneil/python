score = "점수:90"
print(score.removeprefix("점수:")) #.removeprefix라는 함수는 ()안에 변수에서 삭제하고 싶은 부분을 작성하면 날릴 수 있음

score_2="75점"
print(score_2.removesuffix("점")) #.removesuffix라는 함수는 ()안에 변수에서 삭제하고자 하는 부분을 삭제 해줌
print(score.removesuffix("점수")) # 실행 결과가 '점수:90'이라고 나오는 것으로 suffix는 뒤에서 삭제하는 함수로 사용되는 것을 알 수 있음
##문자열 중간을 바꾸는 함수
city = "서울 중구"
print(city.replace("서울","서울시"))

si_1 = "용인"
gu_1 = "기흥"
address_1 = f"{si_1}시 {gu_1}구"
print(address_1)

si_2 = "서울"
gu_2 = "종로"

#서울시 종로구
#용인시 기흥구
#(시의 이름)시 (구의 이름)구 의 형태로 만드는 방법

print(f"{si_1}시 {gu_2}구")
print(f"{si_2}시 {gu_1}구")