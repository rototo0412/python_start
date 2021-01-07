# 2021.01.06 (수)
# 1. 문자열
sentence = '나는 소녀입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """나는 소녀이고

파이썬은 쉬워요"""
print(sentence3)
print('')



# 2. 슬라이싱
jumin = "980809-1234567"

print("성별 : " + jumin[7])
print("연 : " + jumin[0:2]) 
# [0:2] -> 0부터 2직전까지. 
#즉 0과 1번째 값만 가져온다.

print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])
print("생년월일" + jumin[0:6])
# 여기서 [0:6] = [:6]
# :a는 처음부터 a까지 가져온다라는 뜻.

print("뒤 7자리 : " + jumin[7:14])
# 여기서 [7:14] = [7:]
#[7:] -> 7부터 끝까지.

print("뒤 7자리 (뒤부터) : " + jumin[-7:])
# 맨 뒷자리는 -1번째임
# [-7:] :  맨 뒤에서 7번째부터 끝까지.



print('')



#3. 문자열 처리 함수
python = "Python is Amazing"
print(python.lower()) #다 소문자로
print(python.upper()) #다 대문자로
print(python[0].isupper()) #첫글자가 대문자야?
print(len(python)) #길이
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index=python.index("n", index + 1)
print(index)

print(python.find("Java"))
'''-> find는 내가 찾는 글자 없으면 -1을 반환해줌
하지만 index는 내가 찾는 글자 없으면 오류남.'''

print(python.count("n"))



print('')




# 4. 문자열 포맷
print("a" + "b")
print("a", "b")

#방법1
print("나는 %d살입니다." % 20)
# d는 항상 정수값만 넣을 수 있다.
print("나는 %s을 좋아해요." % "파이썬")
# s는 문자열, 문자, 숫자 다 넣을 수 있다.
print("Apple은 %c로 시작해요." % "A")
# c는 한 글자만 가져올 때 사용
print("나는 %s색과 %s색을 좋아해요" %("파란", "빨간"))


#방법2
print("나는 {}살입니다." .format(20))
print("나는 {}색과 {}색을 좋아해요" .format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요" .format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요" .format("파란", "빨간"))
#중괄호 속에 번호를 매겨주면 그 번호에 맞게 값이 들어가게 된다.


#방법3
print("나는 {age}살이며, {color}색을 좋아해요." .format(age=20, color="빨간"))
print("나는 {age}살이며, {color}색을 좋아해요." .format(color="빨간", age=20,))
#이름표를 달아주면 순서 상관없이 그 값이 들어가게 된다.


#방법4(v 3.6이상부터 가능)
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")
#실제 변수에 저장된 값을 가져다가 쓸 수 있음.




#5. 탈출문자
print("백문이 불여일견\n백견이 불여일타")
#\n -> 줄 바꿔쓰기

print('저는 "나도코딩"입니다.') #작은 따옴표로 큰 따옴표 대체하는 방법
print("저는 \"나도코딩\"입니다.") #역슬래쉬 사용하는 방법
print("저는 \'나도코딩\'입니다.") 
#\", \' : 문장 내에서 따옴표

#\\ : 문장 내에서는 하나의 \로 바뀌게 된다.
print("C:\\Users\\wjddb\\Desktop\\PythonWorkspace>")

#\r : 커서를 맨 앞으로 이동
print("Red Apple\rPine")

#\b : 백스페이스 역할(한 글자를 지우는 역할)
print("Redd\bApple")

# \t : 탭
print("Red\t Apple")
print("")

''' Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오
(http://naver.com같은 사이트)
- 규칙
1. http://부분은 제외 => naver.com처럼
2. 처음 만나는 점 이후 부분은 제외 => naver
3. 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성
'''


# 나의 풀이
wedsite = "http://naver.com"
print(wedsite)
sitename = wedsite[7:]
print(sitename)
realsitename=sitename[:sitename.find(".")]
print(realsitename)

print("생성된 비밀번호 : " 
+  realsitename[0:3] + str(len(realsitename)) + str(realsitename.count("e")) + "!") 


print("")
#해설
url = "http://naver.com"
my_str = url.replace("http://", "")
print(my_str)
my_str = my_str[:my_str.index(".")]
print(my_str)
password = my_str[0:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0}의 비밀번호는 {1}입니다." .format( url, password))
print("")

#6. 리스트 : 순서를 가지는 객체의 집합

subway = [10, 20, 30]
print(subway)

subway = ["유재석" , "조세호", "박명수"]
print(subway)

# 박명수씨가 몇 번째 칸에 타고 있는가?
print("박명수씨는 %d 칸에 위치해있습니다." % (subway.index("박명수")+1))

#하하가 다음 정류장에서 다음 칸에 탐
subway.append("하하") #리스트 맨 뒤에 하하 추가함
print(subway)

#정형돈씨를 유재석씨와 조세호씨 사이에 넣어보자
subway.insert(1, "정형돈")
print(subway)

#지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

print(subway.pop())
print(subway)


#같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

#정렬도 가능
num_list = [5, 2, 4, 3, 1]
num_list.sort() #순서대로 정렬해줌
print(num_list)

#순서뒤집기 가능
num_list.reverse()
print(num_list)

#모두 지우기
num_list.clear() #.clear로 다 지워버리기!
print(num_list)

#다양한 자료형 함께 사용가능
mix_list = ["수지", 20, True]
print(mix_list)

#리스트 확장 : 리스트끼리 합칠 수 있다.
family_list =["father", "mother", "sister"]
mix_list = ["수지", 20, True]
family_list.extend(mix_list)
print(family_list)
print("")



# 7. 사전 -> 키와 벨류가 있다. 키가 중복될 수는 없다.
#사전은 중괄호로 열닫.{}
cabinet = {3:"수지", 100:"김수현"}
print(cabinet[3])
print(cabinet[100])
print(cabinet.get(3)) #get도 동일한 역할로 사용 가능


print(cabinet.get(7))
print("haha")
'''cabinet[a]했을 때 a라는 키에 대해서 정해진 게 없으면
프로그램이 끝나버리지만
cabinet.gat(a)했을 때 a라는 키에 대해서 정해진 게 없으면
'None'이 출력되고 그 다음 코드를 실행할 수 있다.'''

#더불어 None대신 다른 값을 입력하고 싶으면 아래처럼 하면 됨.
print(cabinet.get(5, "사용가능"))

print(3 in cabinet) #3이라는 키가 캐비넷에 있는가?
print(7 in cabinet)
print("")

#키는 정수가 아닌 스트링도 가능
cabinet = {"a-3" : "수지", "b-100" : "김수현"}
print(cabinet["a-3"])
print(cabinet["b-100"])

#새 손님이 오셨다!
print(cabinet)
cabinet["a-3"] = "김종국" #a-3의 키의 값이 바뀜
cabinet["c-20"] = "공유"
print(cabinet)

#손님이 가셨다
del cabinet["a-3"] #a-3키를 가진 사람 정보 삭제
print(cabinet)

print("")

#key값만 출력
print(cabinet.keys()) #key만 알려줌

#value들만 출력
print(cabinet.values())

#key, value값 모두 출력
print(cabinet.items())

#목욕탕 폐점 -> 모든 정보 리셋
cabinet.clear()
print(cabinet)
