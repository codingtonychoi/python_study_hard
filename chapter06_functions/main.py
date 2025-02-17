'''
1. 함수(function) : 특정 작업을 수행하는 코드 블록을 정의하는 방법

예를 '사진을 찍는다'라는 행위에 대해 생각해보면,
1) 주머니에서 폰을 꺼내고,
2) 잠금화면을 풀고,
3) 카메라를 켜고,
4) 사진을 찍고자하는 대상에 폰을 조준하고,
5) 셔터를 누른다.

라고 볼 수 있습니다. 그런데 컴퓨터는 시키는대로만 하기 때문에 사진을 찍기 위해서
1) - 5)의 명령어를 입력해줘야만 합니다.
하지만 '사진을 찍는다'라는 함수 내에 미리 입력해두고서 이 명령어를 실행시키기만 하면
이들을 순선대로 수행합니다.

함수 정의 형식:
def turn_right():
    turn_left()
    turn_left()
    turn_left()

함수 호출 형식 :
turn_right()


2. 함수의 종류
    1) 파이썬 내장함수

        우리가 예를 들어 input("이름을 입력하세요 >>>")을 이용해서 이것을 name이라는 변수에 담았다고 가정하면,
        name = input("이름을 입력하세요 >>>")라고 작성해왔습니다.
        즉, 여태 함수의 결과값을 변수에 담아오고 있었습니다.

        파이썬 내장함수는 이미 함수가 정의되어있고, 개발자들은 함수 호출만 잘하면 됩니다.
        사용자 함수는 개발자 자신이 함수를 정의하고, 그 후에 호출하는 것까지의 과정이라고 생각하시변 됩니다.

        내장함수 예시
        print(), type(), int(), flat(), input() ...


    2) 메서드(method)

        정의 : 특정 객체가 가지고 있는 함수를 의미. 특정 자료형에 포함돼있는 함수.
        사실 함수와 메서드는 동일한 개념이지만, 호출 방식에 있어서의 차이가 있음.
        함수는 독립적으로 사용가능/ 메서드는 특정 객체를 통해서만 호출 가능.

        call3(), call4() 유형에서 함수 내에 print()를 집어넣어두면 main 단계에서 (들여쓰기가 안된 단계)
        print() 함수를 입력할 필요가 없어 훨씬 편할 것 같은데
        왜 굳이 return 형태로 입력해서 main에서 일일이 print() 함수를 적용해야 하는가?

        함수형 프로그래밍(Functional Programming): 특정한 함수 1의 결과값이
        또 다른 함수 2의 argument로 사용되는 것을 의미.
        그리고 함수 2의 결과값이 함수 3의 argument로 사용되는 것이 반복된다면


    3) 사용자 정의 함수

3. 함수용어 정리(멘토 파이썬 교재에 있습니다)
    1) 함수정의 : 사용자 함수를 새로 만드는 것
    2) 인수(argument) : 함수에 전달할 입력값( input)
    3) 매개변수(parameter) : 인수를 받아서 저장하는 변수를 의미
    4) 반환값/결과값/리턴값(return) : 함수의 출력값(output)
    5) 함수호출(call) : 함수를 실제로 사용하는 것

4. (사용자)함수의 형식
def 함수_이름(매개변수):
    실행문

변수 = 함수_이름(argument)
'''

# 함수정의
def write_name(name):                            # 정의 시 소괄호 내에 있는 것을 parameter라고 함.
    print(f"당신의 이름은 {name}입니다.")


# 함수호출
# write_name("최재혁")                              # 호출 시 소괄호 내에 있는 것을 argument라고 함.
#
# def write_name_age(name, age):                   # parameter가 복수인 사례 및 함수 정의
#     print(f"당신의 이름은 {name}이고, 나이는 {age}살입니다.")
#
# write_name_age("최재혁", 10)           # 매개변수가 2개이기 때문에 argument도 2개인 상황
# write_name_age(age=10, name="최재혁")             # keyword argument라고 함. 파이썬 작성자들 사이에서는 이게 매너라고 함.
#
# '''
#
#
# '''
#
# eng_name = input("당신의 이름을 소문자로 입력해 >>>").upper()        # 좌측 코드에서 input()은 함수, .upper()는 메서드
# print(eng_name)
# eng_name2 = input("당신의 이름을 소문자로 입력해 >>>").title()
# print(eng_name2)


'''
함수(메서드)의 유형
'''
#
# # 매개변수 x, 리턴 x
# def call1():
#     print("[x|x]")
#
# # 매개변수 o, 리턴 x
# def call2(str_type):
#     print("[o|x]")
#     print(f"{str_type}이라고 입력하셨나보네요.")
#
# # 매개변수 x,  리턴 o
# def call3():
#     print("[x|o]")
#     return 1
#
# # 매개변수 o, 리턴 o
# def call4(str_type):
#     print("[x|o]")
#     return f"제 이름은 {str_type}입니다."
#
#
# call1()
# call2("오늘 날씨 너무 추워요")
#
# call3()                         # 이렇게 하면 return이 출력되지 않음.
# print(call3())                  # 이렇게 해야 return이 출력됨. -> print만 쓰면 되지 왜 call3라는 걸 쓰나요?
# print(call3() +1)               # 이런 연산이 가능
# new_element = (call3() +3)*10   # 이런 연산도
# print(new_element)
#
# call4("최재혁")                  # 이렇게만 하면 안나옴.
# print(call4("최재혁"))


# 사용자 함수를 정의
def introduce(name, address):
    return f"제 이름은 {name}이고, {address}에 삽니다."

# 함수1의 사용 : input()
name = input("이름 : ")
address = input("주소 : ")

# 함수 1의 결과값을 함수 2인 사용자 함수의 argument로 사용 -> 그 결과값을 함수 3인 print()함수의 argument로 사용
print(introduce(name, address))

'''
700원짜리 음료수를 뽑을 수 있는 자판기 프로그램을 구현하시오. 돈을 넣으면 몇 잔의 음료수를
뽑을 수 있는지, 그리고 잔돈은 얼마인지 모든 경우의 수를 출력하도록 합니다.
함수 정의
- 반환값 : 없음(call 1-4 중 어떤 유형일지 고려하세요)
- 함수이름 : vending_machine()
- 매개변수 : 정수 money

코드 구성
def vneding_machine():
    # 함수 구현
    
vending_machine(3000)

실행 예
음료수 = 0개, 잔돈 = 3000원
음료수 = 1개, 잔돈 = 2300원
음료수 = 2개, 잔돈 = 1600원
음료수 = 3개, 잔돈 = 900원
음료수 = 4개, 잔돈 = 200원

'''
def vending_machine(money):
    #pass                                           # 이걸 입력하면 함수 구현이 되어있지 않더라도 일단 오류가 발생하지 않음.
    money = int(money)
    for i in range((money // 700)+1):               # range() 함수 내 들어있는 argument의 자료형은 int 여야함. float은 안됨.
        print( f"음료수 = {i}개, 잔돈 = {money - (700*i)}" )

# return 타입(반환값) 없으니깐 print()로 마무리 지음.  매개변수 명이 통제되어 있으므로 vending_machine(money) 형태로작성.
# call3() 타입이다.


# 함수호출
vending_machine(3000)                               # 매개변수만  바뀌어도 출력가능.


# =========== 내 답 ===================================================
#     money = int(money)
#     can = 0
#     while money > (700*can):
#
#         return f"음료수 = {can}개, 잔돈 = {money - (700*can)}"
#         can += 1
#
# # 함수 호출
# print(vending_machine(3000))

'''
예제 : 구구단 출력하기
함수 정의 : 
함수 이름 : multiply
매개변수 : 정수 n
리턴값 : 없음

함수 호출 :
multiply(dan)

실행 예
몇 단을 출력하시겠습니까? >>> 3
3 x 1 = 3
...
3 x 9 = 27

ctrl + shift + f 사용해서 구구단 출력 코드 찾아와서 작성해도 됨.
'''

dan = int(input("몇 단을 출력하시겠습니까? >>> "))

def multiply(dan):
    for i in range(9):
        print(f"{dan} x {i+1} = {dan * (i+1)}")

multiply(dan)

#======================= 선생님 답 =============================================

# call2 유형으로 작성(내꺼랑 비슷)
# for i in range(1,10, 1) :           #range(시작값, 종료값, 증감값)
# 대신 print에 i+1 대신 i 적용

# call1 유형으로 작성

def multiply2():
    dan = int(input("몇 단을 ? >>> "))                         # 매개변수가 없으므로 함수 안에서 dan이 정의되어야 함.
    for i in range(1,10,1):
        print(f"{dan} x {i} = {dan * (i)}")

multiply2()


# print(dan)          # 현재 상황에서 오류 발생 -> 함수를 정의하는 것은 사용한게 아니기 때문에 dan은 변수에 해당하지 않는다.
                    # structure 확인 시에도 multiply2 함수에서는 선언한 dan이 없음을 알 수 있다.













