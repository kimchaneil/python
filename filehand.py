# 파일 읽기 쓰기

#f = open('filetxt/filehandex.txt','r',encoding = 'UTF-8') #절대 경로와 상대경로가있는데 차이는 알거임
#print(f.read())
#print(f.readline())
#print(f.readlines()) #각 줄의 문자들을 리스트로 정렬 후 출력
#f.close()
"""
with open('filetxt/filehandex.txt','r',encoding ='UTF-8') as f: #with를 사용하면 파일이 알아서 close됨
  print(f.read())
"""
#f = open('filetxt/filehandex2.txt','w', encoding='UTF-8')

#f.write("새로운 글이 작성 되었습니다.") # 문자열로 파일을 덮어쓰기가 되어버림
#f.close()

f = open('filetxt/filehandex2.txt','a', encoding='UTF-8')

f.write("\n새로운 글이 작성 되었습니다.") # 문자열로 파일을 이어쓰기가 됨
f.close()