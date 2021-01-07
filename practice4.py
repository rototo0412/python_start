# 2021-01-07 (목)
# 강의 1시간 40분~2시간 47분


# 8. 한 줄 for +quiz

#출석번호가 1 2 3 4 앞에 100을 붙이기로 함 -> 101 102 103 104처럼
students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students]
print(students)



#학생 이름을 길이로 변환
students = ["Iron man", "Thor", "I am groot"]
print(students)
students = [len(i) for i in students]
print(students)


#학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "I am groot"]
print(students)
students = [i.upper() for i in students]
print(students)



'''Quiz
당신은 Cocoa 서비스를 이용하는 택시 기사이다.
50명의 승객과 매칭 기회가 있을 때,
총 탑승 승객 수를 구하는 프로그램을 작성하라.

조건)
1. 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정한다.
2. 당신은 소요시간 5분 ~ 15분 사이의 승객만 매칭해야한다.

출력문 예제)
[o] 1번째 손님 (소요시간 : 15분)
[ ] 2번째 손님 (소요시간 : 50분)
[o] 3번째 손님 (소요시간 : 5분)
'
'
''
[ ] 50번째 손님 (소요시간 : 16분)

총 탑승 승객 : 2 분
'''

# my solve
from random import *
real_cust = 0 #총 탑승 승객 수
for customer in range(1, 51): #50명의 승객
    time = randint(5, 50) #5 ~ 50분 이하의 임의의 값 생성
    if 5 <= time <= 15: #5 ~ 15분 이내의 손님, 탑승 승객 수 증가 처리
        print("[o] {0}번째 손님 (소요시간 : {1}분)".format(customer, time))
        real_cust += 1

    else : #탑승 매칭 실패한 경우
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(customer, time))

print("\n총 탑승 승객 : {0} 분".format(real_cust))




# 9.함수 -> 함수는 어떤 역할을 하는 박스로 이해하면 된다
def open_account(): #함수 정의할 때는 'def 함수이름():'꼴로 정의한다
    print("새로운 계좌가 생성되었습니다.")

def deposit(balance, money): #입금함수
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
    return balance + money #원하는 값 반환

balance = 0 #잔액
balance = deposit(balance, 1000)
print(balance)

def withdraw(balance, money): #출금함수
    if balance >= money: #잔액이 출금보다 많은 상황. 출금이 가능
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance-money))
        return balance - money
    else:
        print("잔액이 부족하여 출금할 수 없습니다. 잔액은 {0} 원입니다.".format(balance))
        return balance


def withdraw_night(balance, money): #저녁에 출금할 때
    commission = 100 #수수료 100원
    return commission, balance - money - commission


balance = 0 #잔액
balance = deposit(balance, 1000)
# balance = withdraw(balance, 1000)
commission, balance = withdraw_night(balance, 500)
print("수수료 {0} 원이며, 잔액은 {1}입니다." .format(commission, balance))



# 10. 기본값 -> 함수에서 기본값을 설정하는 방법
def profile(name, age, main_lang): #역슬래쉬 + enter를 하면 줄은 바뀌지만 한문장을 인정됨.
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}" \
        .format(name, age, main_lang))

profile("유재석", 20, "파이썬")
profile("수지", 25, "자바")

#같은 학교 같은 학년 같은 반 같은 수업인 경우
def profile(name, age=17, main_lang="파이썬"): #age에는 17, main_lang에는 파이썬이 기본값이 됨
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}" \
        .format(name, age, main_lang))

profile("공유")
profile("이동욱")


# 11.키워드값 -> 키워드 값을 이용한 함수 호출
def profile(name, age, main_lang):
    print(name, age, main_lang)

profile("유재석", main_lang="파이썬", age=25)

# 12. 가변인자 -> 가변인자를 통한 함수 호출
def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    '''print문에서 괄호 닫기 전에 , end=" "라고 하면
    줄 바꿈 대신 " "을 하겠다는 의미가 됨'''
    print(lang1, lang2, lang3, lang4, lang5)

profile("유재석", 20, "Python", "Java", "C", "C++", "C#")
profile("김태호", 25, "Kotlin", "Swift", "", "", "")
#만약 유재석이 언어를 한개 더 배운다면? -> 이럴 때 사용하는 게 가변인자

def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
profile("김태호", 25, "Kotlin", "Swift")

