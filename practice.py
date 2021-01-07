#2021-01-05 (화)
''' <숫자형자료형> '''
print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(3*5)
print(4*(3+1))


''' <문자형 자료형> '''
print('풍선')
print('풍선'*3)

print('')


''' <boolean 자료형 : 참/ 거짓> '''
print(5 > 10)
print(5 < 10)
print(True)
print(False)
print(not True)
print(not (5>10))


print('')

''' <변수> '''
name="연탄이"
animal="강아지"
age=4
hobby="산책"
is_adult = age >= 3
# + 대신에 ,를 사용할 수도 있다 이 경우에는
# ,다음에 한칸이 띄어진 채로 출력이 되고
# 숫자나 불리언에 str을 씌어주지 않아도된다.
print("우리집 "+animal+"의 이름은 "+name+"예요")
hobby="공놀이"
print(name+"는 "+str(age)+"살이며, "+hobby+"을 아주 좋아합니다")
#숫자나 불리언 같은 경우는 str로 묶어주어야 사용가능하다
print(name+"는 어른일까요? "+str(is_adult))


print('') 
print('')




''' <주석 : 코드 내에 포함되어있지만 실제로 실행은 안되는 녀석> '''
# 도 주석
'''은 여러문장 주석'''
# ctrl+/ 는 한방에 다 주석처리


print('')





''' Quiz '''
station = "사당"
print(station+"행 열차가 들어오고 있습니다.")
station = "신도림"
print(station+"행 열차가 들어오고 있습니다.")
station = "인천공항"
print(station+"행 열차가 들어오고 있습니다.")


print('')
print('')



''' <연산자> '''
print(1+1)
print(3-1)
print(1*2)
print(2/1)
print(2**3) #2^3
print(5%3) #나머지구하기
print(5//3) #몫구하기

print('')
print('')
print('')
# >(~보다 크다)
# <(~보다 작다)
# >= (크거나 같다)
# <= (작거나 같다)
# == (~와 똑같다)
# != (~와 같지 않다)
# not은 반대값을 가지게 한다. (False <-> True)
# and : 앞 뒤 값이 다 True가 되어야 True
# or(바 모양도 같은 역할) : 앞 뒤 값 중 하나가 True가 되면 True
# 5 > 4 > 3 처럼 여러번 사용도 가능


'''<간단한 수식> '''
# 사칙연산 여러개 섞인 것
# 변수에도 사칙연산 넣을 수 있음
number = 2
number = number+2
number += 2
# 위아래가 같은 식임. -=, +=, *=, /=, % 다 가능
print('')


''' <숫자 처리 함수> '''
print(abs(-5)) #절댓값
print(pow(4,2)) #지수
print(max(1, 10)) #최댓값
print(min(1, 10)) #최솟값
print(round(3.14)) #반올림


print('')



''' <랜덤함수 : 난수를 만들어주는 함수> ''' 
from random import *
print(random()) # 0.0 ~ 0.1미만의 임의의 값 생성
print(random() * 10) # 0.0 ~ 10.0미만의 임의의 값 생성
print(int(random() * 10)) # 0 ~ 10미만의 임의의 값 생성
print(int(random() * 10) + 1) # 1 ~ 10미만의 임의의 값 생성

print('')

#로또 번호 추첨해보자
print(int(random() * 45 +1)) #1 ~45미만의 임의의 값
print(int(random() * 45 +1))
print(int(random() * 45 +1))
print(int(random() * 45 +1))
print(int(random() * 45 +1))
print(int(random() * 45 +1))
print('')

print(randrange(1, 46)) # 1 ~ 46미만의 임의의 값 생성
print(randint (1, 45)) #1 ~ 45이하의 임의의 값 생성
print('')


'''<quiz>'''
#랜덤으로 날짜, 28일 이하로, 매월 1~3일은 제외
#출력문은 "오프라인 스터디 모임 날짜는 매월 x일로 선정되었습니다."

from random import *
date = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월" 
+str(date)+ "일로 선정되었습니다.")
print('')



