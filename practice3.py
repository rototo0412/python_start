# 2021-01-07 (목)
# 강의 1시간 40분~2시간 47분


# 1. 튜플
''' -> 리스트와 달리 내용변경이나 추가는 못하지만 속도가 리스트보다 빠르다
변경되지 않는 목록에 활용한다.'''

menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])
# menu.add("생선까스") -> 오류남. 불가하다.

name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)




# 2. 집합(set)
# 중복 안됨, 순서 없음
my_set = {1, 2, 3, 3, 3}
print(my_set)

java = {"수지", "아이유", "김수현"}
python = set(["수지", "공유"]) #이렇게도 표현가능

#교집합 (java와 python 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python)) #.intersection()을 이용할 수도 있음

#합집합 (java나 python을 할 수 있는 개발자)
print(java | python)
print(java.union(python)) #.union()을 이용할 수도 있음

#차집합 (java는 할 수 있으나 python은 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python)) #.difference()를 이용할 수도 있음

#python할 줄 아는 개발자가 늘어남
python.add("하하")
print(python)

#java를 까먹은 개발자가 생김
java.remove("아이유")
print(java)



# 3. 자료 구조의 변경
menu = {"커피", "우유", "주스"}
print(menu, type(menu)) #출력보면 type이 set임

menu = list(menu)
print(menu, type(menu)) #출력보면 type이 list로 바뀜

menu = tuple(menu)
print(menu, type(menu)) #출력에서 보면 type이 tuple로 바뀜

''' 위 세개의 출력을 보면 set은 {}, list는 [],
tuple은 ()로 괄호가 바뀌는 것을 볼 수 있음'''

menu = set(menu)
print(menu, type(menu))






''' Quiz
학교에서 파이썬 코딩 대회를 주최한다.
참여도를 높이기 위해서 댓글 이벤트를 진행한다.
댓글 작성자들 중에서 추첨을 통해서 1명은 취킨, 3명은 커피 쿠폰을 준다.
추첨 프로그램을 작성하라

조건)
1. 편의상 댓글은 20명이 작성하였고 아이디는 1~20이라고 가정
2. 댓글 내용과 상관없이 무작위로 추첨하되 상품중복불가
3. random 모듈의 shuffle과 sample을 활용

출력 예제)
-- 당첨자 발표 --
치킨 당첨자 : 1
커피 당첨자 : [2, 3, 4]
--축하합니다--
'''

# 활용 예제)
from random import *
lst = [1, 2, 3, 4, 5]
print(lst)
shuffle(lst) #무작위로 섞어주는 것
print(lst)
print(sample(lst, 1)) #n개를 추첨해주는 것
print(sample(lst, 3))


# my solve
from random import *
id = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(id)
shuffle(id)
print(id)
gift = sample(id, 4)

print("-- 당첨자 발표 --")
print("치킨 당첨자 : {}" .format(gift[0]))
print("커피 당첨자 : %s" % gift[1:])
print("-- 축하합니다 --")


#해설
from random import *
users = range(1, 21) # 1부터 20까지 숫자를 생성
users = list(users)
print(users)
shuffle(users)
print(users) # 잘 섞어졌는지 결과 확인해보기
winners = sample(users, 4) #4명 중에서 1명은 치킨, 3명은 커피

print("-- 당첨자 발표 --")
print("치킨 당첨자 : {}" .format(winners[0]))
print("커피 당첨자 : {}" .format(winners[1:]))
print("-- 축하합니다 --")



# 4. if문(분기 : 상황을 판단해서 그 상황에 맞는 코드를 사용)
weather = "미세먼지"
# weather = input("오늘 날씨는 어때요? ") -> 사용자의 응답을 받을 수 있다

if weather == "비" or weather =="눈" :
    print("우산을 챙기세요")
elif weather == "미세먼지" : 
    print("마스크를 챙기세요")
else: #else가 없고 조건이 if문에도 해당하지 않는다면 출력이 없다
    print("오늘의 날씨는 맑습니다")




temp = int(input("기온은 어때요? "))
#input은 값을 항상 문자열로 값을 받기 때문에 int로 감싸준다
if 30 <= temp:
    print("너무 더움. 나가지 말어")
elif 10 <= temp and temp <30:
    print("날씨가 조흠")
elif 0 <= temp <10:
    print("외투를 챙기시오")
else:
    print("JONNA 추운 날씨!")





# 5. for문 -> 문장이 중복될 때 사용
for waiting_no in [0, 1, 2, 3, 4]:  #순차적으로 커질경우는 range()사용
    print("대기번호 : {0}" .format(waiting_no))


for waiting_no in range(0,5):  #0부터 5미만까지
    print("대기번호 : {0}" .format(waiting_no))


starbucks = ["아이언맨", "토르", "아이엠 그루트"]
for custiomer in starbucks:
    print("{0}님, 커피가 준비되었습니다." .format(custiomer))




# 6. while문
customer = "토르"
index = 5
while index >=1:
    print("{0}님, 커피가 준비되었습니다. {1}번 남았어요.".format(customer, index))
    index -= 1
    if index == 0:
        print("커피가 폐기처분되었습니다.")

#while True라고 하면 계속 while문이 반복됨. ctrl+c누르면 종료됨


customer = "아이엠그루트"
person = "Unknown"

while person !=customer:
    print("{0}님, 커피가 준비 되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요? ")
    




# 7. continue와 break -> 반복문 내에서 쓸 수 있는 아이들
# continue쓰면 그 다음 순서의 반복문을 시작하게 됨
#break쓰면 바로 반복문을 끝냄
absent = [2, 5] #결석한 학생
no_book = [7] #책을 안 가져온 학생
for student in range(1, 11) :#1부터 11미만의 수
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
        break 
    print("{0}, 책을 읽어보렴".format(student))



