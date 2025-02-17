'''
컬렉션(collection) : 여러 값을 하나의 이름으로 묶어서 관리하는 자료형

string의 경우 문자 하나하나를 줄(str)로 묶어서 문자열로 출력하는데,
예를 들어 '다수의 다른 string을 관리하는 방법은 무엇일까?'에 관한 대답

여러명의 프로필을 관리한다고 가정해보겠습니다.

'''

choijaehyuk = "이름: 최재혁\n나이: 10\n직업: 초등학생"
print(choijaehyuk)
shinminseung = "이름: 신민승\n나이: 30\n직업: 백수"
print(shinminseung)

'''
한 명 저장하는 데에는 문제가 없을 수 있지만 매번 변수 하나에 이름, 나이, 직업 등을 한 명 추가할 때마다
정리하는 것이 비효율적이고, 예를 들어 choijaehyuk 에서 직업만 조회하고 싶어도 전체 정보를 다 확인해야 함.

그리고 주소를 추가한다고 가정했을 때에도 각 변수들을 전부 다 참조해서 수정해줘야 할 필요성이 있다. 

이상의 문제들을 한꺼번에 관리하기 위해나 방식으로 모음(collection)을 사용합니다.

종류 :
    1. list 리스트 : 추가/수정/삭제가 언제나 가능 / a = [1,2,3] 대괄호 사용
    2. tuple 튜플 : 추가/수정/삭제가 불가능 / a = (1,2,3) 소괄호 사용
    3. set 세트 : 중복된 값의 저장이 불가능 / a = {1,2,3} 중괄호 사용
    4. dict 딕트(딕셔너리) : 키 + 값으로 관리 / a= {"name":최재혁, "age":10} 중괄호 사용
    
    

1. list
    여러 값을 저장할 때 가장 많이 사용. 자료형이 서로 다르더라도 하나의 리스트에 저장 가능.
    하나의 배열(python에서 리스트와 비슷한 개념)에 동일한 자료형만을 저장할 수 있는 C, Java에 비해
    python이 가지는 장점이라고 할 수 있음.

'''

'''
수학여행을 어디로 갈 지 결정하기 위해 학생들이 희망하는 모든 수학여행 장소를 조사하기로 했습니다.
학생들이 원하는 장소를 입력받아 동일한 입력을 무시하고 모든 입력을 저장하려고 합니다.
학생을 3명으로 가정하고 실행 예와 같이 동작하는 프로그램을 작성하시오.

실행 예
희망하는 수학여행지를 입력하세오 >>> 제주
희망하는 수학여행지를 입력하세오 >>> 제주
희망하는 수학여행지를 입력하세오 >>> 민속촌

조사된 수학여행지는 {'제주', '민속촌'} 입니다.
조사된 수학여행지는 ['제주', '민속촌'] 입니다.

'''
# 비어있는 list/set을 생성
# travel_list = []
# travel_set = {}
#
# for i in range(3) :
#     place = input("희망하는 수학여행지를 입력하세오 >>> ")
#     travel_list.append(place)
#
# travel_set = set(travel_list)
#
# #print(f"조사된 수학여행지는 {travel_set}입니다.")
# print(f"조사된 수학여행지는 {list(travel_set)}입니다.")
# print(f"조사된 수학여행지는 {travel_set}입니다.")


# ==== 다른 방법 ====
#
# for i in range(3) :
#     place = input("희망하는 수학여행지를 입력하세오 >>> ")
#     travel_list.append(place)
#     travel_set.add(place)                                   # 중복없는 set를 만들 수 있음



'''
짝수만 추출하기

사용자로부터 임의의 양의 정수를 입력받고, 그 정수만큼 숫자를 입력받아 list에 저장하세요.
이후 저장된 숫자 중 짝수만 새로운 list에 저장하여 출력하는 프로그램을 작성하세요.

실행 예
몇개의 숫자를 입력할까요? >>> 5
1번째 숫자를 입력하세요 >>> 10
...
5번째 숫자를 입력하세요 >>> 30
입력받은 숫자는 [10, 15, 20, 25, 30]입니다.
입력받은 숫자들 중 짝수는 [10,20,30]입니다.
'''

num_list = []
num_even_list = []

chance = int(input("몇개의 숫자를 입력할까요? >>> "))

for i in range(chance) :
    num = int(input(f"{i+1}번째 숫자를 입력하세요 >>> "))
    num_list.append(num)
    if num % 2 == 0:                                        # 꼭 else 안 써도 됨.
        num_even_list.append(num)

print(f"입력받은 숫자는 {num_list}입니다.")
print(f"입력받은 숫자들 중 짝수는 {num_even_list}입니다.")


'''
딕셔너리 기반의 연락처 관리

사용자로부터 3명의 이름과 전화번호를 입력받아 딕셔너리에 저장한 뒤, 입력한 정보를 추출하는
프로그램을 작성하시오.

실행 예
1번째 사람의 이름을 입력하세요 >>> 최재혁
1번째 사람의 연락처를 입력하세요 >>> 010-1111-1111
2번째 사람의 이름을 입력하세요 >>> 신민숭
2번째 사람의 연락처를 입력하세요 >>> 010-2222-2222
3번째 사람의 이름을 입력하세요 >>> 장재만
3번째 사람의 연락처를 입력하세요 >>> 010-3333-3333

입력받은 연락처는 {'최재혁':'010-1111-1111, '신민승':'010-2222-2222', '장재만':'010-3333-3333} 입니다.
'''
friend_dict = {}                    # 비어있는 딕셔너리를 선언하는 방식

for i in range(3):
    key = input(f"{i+1}번째 사람의 이름을 입력하세요 >>> ")
    value = input(f"{i+1}번째 사람의 연락처를 입력하세요 >>> ")

    # 딕셔너리에 element를 추가하는 방법
    friend_dict[key] = value
    # friend_dict.append{name:address} >>>> 이게 아니다.

print(f"입력받은 연락처는 {friend_dict} 입니다. ")


'''
숫자를 입력한 횟수만큼 비어있는 list에 숫자를 추가하기
문제: 비어있는 list01을 선언하고 그 안에 입력받은 횟수만큼 숫자를 추가하시오.

함수정의 : add_numbers()
매개변수 : 정수 n

함수호출
add_numbers(last_num)

실행 예
숫자 몇까지 입력하시겠습니까? >>> 10
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

'''
n = int(input("숫자 몇까지 입력하시겠습니까? >>> "))

list01 = []
def add_numbers(n):                                                 # call2 유형의 함수 정의
    for i in range(n):
        list01.append(i+1)

add_numbers(n)                                                      # 함수 호출
print(list01)


list02 =[]
def add_numbers2(n):                                                # call4 유형의 함수 정의
    for i in range(n):
        list02.append(i+1)
    return list02

print(add_numbers2(n))                                              # 함수 return 값을 출력


# add_numbers 와 add_numbers2 의 차이점
# for number in add_numbers2(n):
#     print(number+1)                                     # add_numbers2(n)는 return값으로 list형태를 변환하기 때문에
                                                        # element에 대한 연산이 가능. eg) +1을 하건, 짝수만 걸러내건...

# for number in add_numbers(n):
#     print(number+1)                                     # add_numbers(n)은 print실행문으로 마무리되기 떄문에 추가 연산 불가능.


'''
짝수와 홀수의 개수 세기
list를 입력받아 짝수와 홀수의 개수를 세는 함수를 작성하시오.

함수 정의
함수이름 : count_even_odd
매개변수 : numbers(요소는 모두 정수일 것)

함수 호출
count_even_odd([1,2,3,4,5,6,7,8,9,10])

실행 예
짝수의 개수 : 5개
홀수의 개수 : 5개
'''
# 먼저 실행단계가 작동하는지 확인하고 함수화해도 됨.



#예시 numbers = [1,2,3,4,5,6,7,8,9,10]

def count_even_odd(numbers):
    even_count = 0
    odd_count = 0
    for number in numbers:
        if number % 2 == 0:
            even_count +=1
        else:
            odd_count +=1

    print(f"짝수의 개수 : {even_count}개\n홀수의 개수 : {odd_count}개")

count_even_odd([1,2,3,4,5,6,7,8,9,10])

'''

1. list
    여러 값을 저장할 때 가장 많이 사용. 자료형이 서로 다르더라도 하나의 리스트에 저장가능.
    하나의 배열(python에서 리스트와 비슷한 개념)에 동일한 자료형만을 저장할 수 있는 c, java에 비해
    python이 가지는 장점이라고 할 수 있음.
'''

li = [1, 2, 3, "최재혁"]
print(li)

'''
1-1. list의 index와 slice
    list는 str과 동일한 방식의 index와 slicing을 지원함.

    1) 인덱스와 마이너스 인덱스
'''

print(li[0])
print(li[1])
print(li[-1])
print(li[-2])

'''
    2) slice
        str의 슬라이싱과 같이 '시작인덱스:종료인덱스:증감값'으로 이루어져 있음.
'''

list_num1 = [100, 3.14, "hello"]  # list 생성방법 1
list_num2 = list([4, 5, 6, 7, 8, 9])  # list 생성방법 2
print(list_num1)
print(list_num2[0:4:2])
print(list_num2[0:5:2])

'''
    3) list 요소의 추가와 삭제
        list에 새로운 요소를 추가할 때는 .append()와 .insert() '메서드'를 사용할 수 있습니다.
        기존 요소를 삭제할 때는 .pop() 메서드를 사용합니다.

        .append() - 항상 마지막 인덱스에 요소를 추가하는 메서드
        .insert(위치, 값) - 정해진 위치(인덱스)에 해당 값을 추가하는 메서드

'''

scores = [30, 40, 50]  # scores라는 list 내에 있는 int 데이터인 30, 40, 50 을 요소(element)라고 함.
print(scores)  # 함수와 달리 list명.메서드명(데이터)의 형태로 사용했음. 호출 방식이 다르다.
scores.append(100)
print(scores)
scores.insert(3, 90)
print(scores)

'''
        .pop()의 경우 빈 괄호로 사용하게 되면 맨 마지막 요소가 삭제됨. .pop(인덱스넘버)로 작성하면 해당 인덱스의 요소를 삭제함.
'''

scores.pop()
print(scores)
scores.pop(0)  # 오버로딩의 기초 개념이 포함되어 있어서 동일한 메서드명인데도 argument가 있을 수도/없을 수도 있음.
print(scores)

'''
교재에 없는 삭제 메서드 : .remove(값)을 사용하면 list 내에 해당하는 값을 찾아 삭제함.
'''
scores.remove(40)
print(scores)

# 이상의 코드까지 실행시켰을 때, 인덱스가 두 개 밖에 없어 10개 정도의 element를 추가하는 반복문을 작성

for i in range(10):
    scores.append(i * 10)
print(scores)

# list 내의 요소들을 하나씩 뽑아내는 반복문 -  for문
# 위 코드 참조해서 전체 element를 뽑아내는 반복문 작성하세요.
# len() 함수도 이용할 것. (파일 전체 검색 : ctrl + shift+ f)

for i in range(len(scores)):
    print(scores[i])

# 이렇게 요소를 뽑아내면 각 요소에다가 추가적인 연산을 할 수 있다. list 형태로는 요소를 변경할 수 없다.


# 향상된 for문 사용
for score in scores:  # collections의 경우 복수로 이름 짓고
    print(score)  # 향상된 for 문에서 각 변수는 단수로 이름 짓는 경우가 많습니다.

'''
2. Tuple
    저장된 값을 변경할 수 없는 list라고 생각하면 됨. 인덱스와 슬라이스를 사용하지만 저장된 값 이외에는
    추가/수정/삭제가 불가능.

    튜플은 소괄호로 작성.

'''

tuple_num1 = (1, 2, 3)  # 튜플 생성 방법 1
tuple_num2 = tuple((4, 5, 6))  # 튜플 생성 방법 2
tuple_num3 = 7, 8, 9  # 튜플 생성 방법 3

print(tuple_num1)
print(tuple_num2)
print(tuple_num3)

# 복수의 변수 선언 및 초기화 방법 (첫시간에 함)
a, b, c = 7, 8, 9  # 이거랑 세번째 방법이 다른게 이거는 등호 앞에도 복수(3개)개가 있다.
print(a)
print(b)
print(c)

'''
    튜플 생성 방법 3을 이용하다고 가정했을 때, 값이 하나 밖에 없는 튜플을 생성한다면
    tuple_num4 = 0 이라고 입력할 경우, 생길 수 있는 문제는 무엇일까요? 
'''

tuple_num4 = 0
print(tuple_num4)
print(type(tuple_num4))
print(type(tuple_num2))

tuple_num5 = 0,
print(tuple_num5)
print(type(tuple_num5))

'''
        1) 튜플에서의 인덱스/ 마이너스 인덱스
'''
tuple_num6 = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
print(tuple_num6[2])
print(type(tuple_num6[2]))  # collections의 element에 type() 함수를 적용하면,
# element의 자료형이 반환됨. (int)

tuple_num7 = "hello.", "nice to meet you.", "my name is", "choijaehyuk.", "I am", "10", "years old."

for str in tuple_num7:
    print(str.title(), end=" ")  # 튜플의 정의를 생각해보았을 때 왜 결과값이 이렇게 될까요?
print()
for str in tuple_num7:
    print(str, end=" ")  # str.title()을 적용시켰다고 해서 tuple 내의 element들 값이 바뀐 상태로
print()  # 유지되는 것이 아니라, 출력문에만 메서드가 적용된 상태이기 때문에
# 실제 element가 바뀐 것이 아니며 튜플의 정의에서도 벗어난 것이 아니다.

'''
3. set
    수학의 집합 개념을 구현한 자료형.
    list 와의 차이점은 순서가 없기 때문에(비시퀀스) 인덱스 및 슬라이싱 사용이 불가능.
    중복된 값의 저장도 불가능.

    이를 활용하여 중복 제거용으로 사용하는 경우와, 교집합, 합집합, 차집합과 같은 집합 개념이 필요한 경우 사용.

    set를 사용하기 위해서는 중괄호{}를 사용한다.
'''

set_num1 = {1, 2, 3}  # 세트 생성 방법 1
set_num2 = set({4, 5, 6})  # 세트 생성 방법 2
print(set_num1)
print(set_num2)

# 비어 있는 list, tuple, set 생성 방법
li = []
tu = ()
se = {}

print(type(li))  # list
print(type(tu))  # tuple
print(type(se))  # dict

'''
se = {} 형태로 비어있는 set를 생성했을 경우 se는 사실 class 'dict' 이기 때문에
비어있는 set를 만들기 위해서는 세트 생성 방법 2를 사용해야만 함.
'''

se2 = set({})
print(type(se2))  # set

'''
    특징 :
        1) 저장되는 순서가 없다. -> 인덱싱/슬라이싱 불가
        2) 중복되는 값 저장 불가.
        3) 특히 2)의 특징으로 인해 set는 단독으로 쓰이기 보다는 list와 연계해서 많이 쓰임.
'''

list_num5 = [1, 1, 2, 2, 3, 3, 3]
print(list_num5)

set_num5 = set(list_num5)  # 형변환 함수인 set()을 사용하고, 그 안에 list_num5를 argument로 넣어 바꿔줌.
print(set_num5)

list_num6 = list(set_num5)
print(list_num6)  # 다시 list로 바뀌어서 슬라이싱/인덱싱 사용 가능. 중복되는 값은 사라졌다.

'''
    set에는 인덱싱/마이너스 인덱싱/슬라이싱을 지원하지 않기 때문에 특정 요소만 추출하기 위해서는
    형변환 과정( 주로 list() )이 필요함.

    요소 관련 메서드
        .add() : set 에 새로운 요소 추가
        .remove() : 기존 요소를 삭제
        .discard() : 기존 요소를 삭제
'''

set_num6 = {10, 20, 30}
set_num6.add(50)
print(set_num6)  # {10,20,30,50} : 순서가 없어서 다르게 나올 수도 있음.

set_num6.remove(50)
print(set_num6)

# .remove() v/s .discard()

# set_num6.remove(70)                     # 안에 값이 set 내에 없다면 오류가 남.
set_num6.discard(70)  # 안에 값이 set 내에 없더라도 오류가 발생하지 않음.

'''
4. dictionary
    사전을 찾으면 'flower: 꽃', 'dictionary: 사전' 등으로 기재되어 있다.
    즉 ":"을 기준으로 좌측과 우측이 나누어진 형태.
    dictionary는 list, tuple, set와 달리 'key:value' 의 구성으로 이루어져 있음.
'''

dict_num1 = {
    "이름": "최재혁",
    "나이": 10,
    "주소": "부산광역시",
}
print(dict_num1)

# 맨 마지막에 있는 ,의 이미는 혹시 후에 key-value를 추가할 때 이전 라인에서 콤마 입력하고 엔터치고
# 또 key: value 형태로 작성하기 귀찮으니까 미리 쉼표를 찍어놔서 쉽게 추가할 수 있도록 하는 것이
# 개발자들끼리의 매너라고 함.


'''
    dictionary는 인덱스는 존재하지 않지만 위와 같이 key를 인덱스와 유사하게 사용함.
    즉, key 값을 알면 저장된 값(value)를 확인할 수 있는 구조.
'''

# list의 각 요소를 추출하기 위한 반복문

li2 = [10, 20, 30, 40]
for num in li2:
    print(num)

# dictionary에서 같은 방식의 반복문을 활용하게 될 때,
# for i in range(len(dict_num1)) :
#     print(dict_num1[i])                             # 인덱스가 없기 때문에 오류 발생

for k in dict_num1:
    print(k)  # 그냥 print 하게 되면 dict_num1의 key 만 추출됨.
    print(dict_num1[k])  # value도 추출하려면 이렇게 작성해야함.
    print()

# key 목록을 추출하는 메서드
print(dict_num1.keys())
print(dict_num1.values())

print(type(dict_num1.keys()))  # class : dict_keys : list가 아니라서 인덱스가 없음.
print(type(dict_num1.values()))  # class : dict_values

keys = list(dict_num1.keys())  # 인덱스를 활용하기 위해 list로 형변환을 할 필요가 있다.
values = list(dict_num1.values())

print(keys[1])
print(values[2])

'''
        1) 딕셔너리 요소의 추가와 삭제
'''

dict_num1["직업"] = "코리아 IT 아카데미 파이썬 강사"  # 기존에 없는 key를 입력하고, = value 지정하면 됨.
print(dict_num1)
dict_num1["직업"] = "코리아 IT 아카데미 자바 강사"  # 하나의 key에 서로 다른 value를 저장할 수 없음. 즉 key 하나당 value는 하나.
print(dict_num1)  # 이전 value가 날아감.

# 삭제 방법
dict_num1.pop("직업")  # key를 정확하게 입력해야 삭제 가능.
print(dict_num1)  # key를 삭제하면  value도 같이 날아감.

'''
응용 예제

list [10, 20, 30, 40 ~ , 100]의 3번재 요소부터 7번재 요소만 추출한 결과, 그리고
list에서 2번째 요소를 출력하는 프로그램은 작성하시오.

실행 예
3번재 요소로부터 7번째 요소 = [30, 40, 50, 60 , 70]
3번째 요소로부터 7번재 요소 중 2번재 요소 = 40
'''
# 처음거 슬라이싱 사용하고
# 슬라이싱 된 list에서 인덱싱 사용

list_origin = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(list_origin)

list_sliced = list_origin[2:7:1]
print(f"3번재 요소로부터 7번째 요소 = {list_sliced}")
print(f"3번째 요소로부터 7번째 요소 중 2번째 요소 = {list_sliced[1]}")  # 현재 줄 복사는 ctrl + d

# 선생님 답
# print(f"3번째 요소로부터 7번째 요소 중 2번째 요소 = {list_origin[2:7:1][1]}")
# list_origin[2:7:1]  <-- 이거 자체도 리스트니깐 여기서 인덱싱을 바로 적용할 수 있다.
# 결과값의 데이터 타입이 뭔지 아는 것이 중요하다는 말.

# 내가 한 코드가 대부분의 인강에서 사용하는 방법이긴 함.
# 근데 한번만 사용할 거라면 굳이 변수 선언 안해도 된다. 이렇게 쓰는거에 익숙해져 보자.

'''
사용자로부터 1에서 12사이의 월을 입력받아, 해당 월이 몇일까지 있는지 출력하시오.
(윤년은 고려x)

실행 예)
1~12 사이의 월을 입력하세요 >>> 2
2월은 28일 까지입니다.
'''

month = int(input("1~12 사이의 월을 입력하세요 >>>"))

# list의 사용
last_dates = [31, 28, 31, 30, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# print(f"{month}월은 {last_dates[month-1]}일까지 있습니다.")

# dictionary의 사용
last_dates_dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
# print(f"{month}월은 {last_dates_dict[month]}까지 있습니다.")

last_dates_short = [28, 30, 31]
if month == 2:
    last_date = last_dates_short[0]
elif month in (4, 6, 9, 11):
    last_date = last_dates_short[1]
elif month in (1, 3, 5, 7, 8, 10, 12):
    last_date = last_dates_short[2]
else:
    print("잘 못 입력하셨습니다.")
    last_date = "x"

print(f"{month}월은 {last_date}일까지 있습니다.")





















