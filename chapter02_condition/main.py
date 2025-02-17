'''
1. if문
    if 문은 조건이 참(True)일 때만 해당 블록의 코드를 실행.
    if 문에서 주의할 점
        1) if 와 같은 줄에 작성된 코드는 true/false 로 구분할 수 있어야 함.
        2) if 와 같은 줄에 있는 조건문이 끝났을 때 콜론(:)으로 마무리
        3) python 에서는 타 언어들과 달리 들여쓰기(indented writing)가 '매우' 중요. (pycharm에서는 4번 들여쓰기가 기본.)

2. if else문
    if 문 다음에 else를 사용할 수 있는데, if가 참일 때 실행된다면, else는 거짓일 때 실행됨.

3. if elif else문
    타 언어에서는 else if를 쓰는데 파이썬은 elif라고 씀.
    여러 조건을 동시에 검사하기 위해 사용하는 구조.

    if 조건문의 전체 형식
        if 조건식 1:
            실행문1
        (elif 조건식 2:)
            (실행문2)
            ...

        (else:)
            (실행문n)

4. 중첩 if문(Nested if)
    조건문 내부에 또 다른 조건문을 사용할 수 있음. 다만 가독성이 떨어져
    추후에 배우는 논리연산자와 함께 사용하는 편.

5. 조건문에서 자주 쓰이는 연산자
    비교 연산자 :
        1) == : 같다
        2) != : 같지 않다
        3) > : 초과
        4) < : 미만
        5) >= : 이상
        6) <= : 이하
    논리 연산자 :
        1) and : A and B        # 둘 모두가 참일 때 실행문 실행
        2) or : A or B          # 둘 중 하나가 참일 때 실행문 실행
        3) not : if not A       # A가 false일 때 실행문 실행

'''

# age = int(input("당신의 나이는?"))
# if age >= 19 :
#     print("성인입니다.")         # if 와 함께 있는 조건문이 True 일 때만 실행됩니다. False 시 실행 안됨.
# # else:
# #     print("미성년자입니다.")       # 이 print 함수는 else절에 종속되어 있음을 들여쓰기를 통해 알 수 있음.
# #                                 # if-else는 서로 반대이기 때문에 else 절에서는 굳이 조건식을 명시하지 않음.
#
# elif age >= 8 :
#     print("학생입니다.")
#
# else:
#     print("미취학 아동입니다.")

'''
age 14라면
1) 첫 번째 조건은 false
2) 두 번째 조건은 true 이므로 두번째 라인이 실행됨.
3) 이후 조건은 확인하지 않고 조건문 전체가 종료됨.
'''

age = 5
has_ticket = False

if age >= 19:
    if has_ticket:                              # 중첩 if문
        print("영화관 입장이 가능합니다.")
    else:
        print("티켓을 구매하세요.")

else:
    print("미성년자는 출입할 수 없습니다.")


age = 5
has_ticket = False

if age >= 19 and has_ticket:                # 논리연산자를 적용한 중첩 if문의 축약.
    print("영화관 입장이 가능합니다.")          # 하지만 티켓구매 문구는 출력 못하므로 완전 대체는 할 수 없다.

else:
    print("입장할 수 없습니다.")

