'''
1. 생성자(constructor)
'''

# 클래스 정의
class Candy :
    def set_info(self, shape, color):
        self.shape = shape
        self.color = color

    def display_info(self):
        print(f"사탕의 모양은 {self.shape}이고, 색깔은 {self.color}입니다.")


# 객체 생성
satang = Candy()
satang.set_info("구형", "갈색")
satang.display_info()

'''
    satang 이라는 인스턴스는 생성된 '이후'에 set_info() 메서드를 호출하여 "구형" 모양의,
    "갈색"이라는 속성(attribute)을 갖게 됩니다.
    
    satang 인스턴스의 생성과정
        1. 값이 없는(속성에 값이 대입되어 있지 않은) 인스턴스를 생성
        2. 값을 저장할 수 있는 메서드 호출
        
    그렇다면 처음부터 값이 있는 인스턴스를 생성하면 코드라인이 줄지 않을까?
    이에 대한 해답이 생성자라는 개념이고,
    C 나 JAVA의 경우 생성자는 클래스명과 동일한데, 또 python만 이상한 방식으로 만듭니다.
    -> __init__() 라는 메서드            (initialization: 초기화라는 뜻. 초기화란 객체의 속성값을 처음으로 대입하는 것.)
   
   
   __init__() : 메서드(생성자)는 인스턴스가 생성될 때 '자동으로 호출'되기 때문에 인스턴스 변수의
   '초기화' 용도로 사용, 즉 값이 있는 인스턴스를 생성할 수 있다는 의미입니다.
    '객체 생성과 동시에' 생성자가 호출됨 -> 초기값을 작성할 때  사요앟ㄴ다는 의미
    
    
    형식 :
    
class 클래스명:
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color 
'''

class Candy2():

    # 생성자의 정의
    def __init__(self, shape, color):           # set_info 대신에 __init__ 이 들어감.
        self.shape = shape
        self.color = color

    def display_info(self):
        print(f"사탕의 모양은 {self.shape}이고, 색깔은 {self.color}입니다.")

satang2 = Candy2("정육면체", "흰색")      # 이 부분이 달라짐. 한줄 줄었다. set_info()에 안 넣고, class괄호 안에 넣음.
satang2.display_info()

# 이상에서 주목해야할 점은 satang 인스턴스와 satang2 인스턴스의 생성 방식의 차이입니다.

# ======= 내 연습 ========
# class Pokemon:
#     def __init__(self, number, type):
#         self.number = number
#         self.type = type
#     def display_info(self):
#         print(f"이 포켓몬은 {self.number}번이고, {self.type}타입입니다.")
#
# 이상해씨 = Pokemon(1, "풀")
# 이상해씨.display_info()

'''
2. 소멸자(Destructor)

    인스턴스가 생성될 때 자동으로 생성자와 마찬가지로 인스턴스가 소멸될 때 호출되는 메서드
    이를 소멸자라고 하며, 소멸자를 정의하는 메서드는 __del__()
'''

class Sample:

    # 생성자 정의
    def __init__(self):
        print(f"인스턴스가 생성되었습니다.")            # 생성자 생성할 때 속성에 값만 대입하는 게 아니라 출력문을 삽입할 수도 있음.

    def __del__(self):
        print(f"인스턴스가 소멸되었습니다.")

# 객체생성
sample = Sample()

del sample      # del 객체명으로 소멸자를 원하는 시기에 호출할 수 있음 -> 예를 들어 일단 객체 소멸시키고

# 여기 부분에 추가적인 로직을 작성하여 더 프로그램이 진행된 후에 프로그램 전체 종료가 이루어질 수 있음.
print("프로그램이 종료되었습니다.")


'''
기본예제

생성자를 이용해서 용량을 가진 usb 인스턴스를 만드는 프로그램을 작성하시오.

지시사항
1. 클래스 USB를 정의할 것.
2. 생성자를 정의하여 매개변수로 capacity를 받을 것.
3. get_info() 메서드를 정의할 것

main 단계 코드
usb = USB(64)
usb.get_info()

실행 예
64GB USB
'''

# class USB :
#     def __init__(self, capacity):
#         self.capacity = capacity
#     def get_info(self):
#         print(f"{self.capacity}GB USB")
#
# # 객체 생성 및 get_info() 메서드 호출
# usb = USB(64)
# usb.get_info()

'''
생성자와 소멸자릉 이용하여 서비스 안내 메시지를 출력하는 프로그램을 작성하시오.

class Service를 정의하고, 생성자를 통해 매개변수를 service로 받고, print() 메서드를 생성자와 소멸자 내에 작성하시오.

main 단계에서의 작성
s = Service("길 안내")
del s

실행 예
길 안내 Service가 시작되었습니다.
길 안내 Service가 종료되었습니다.
'''

# class Service:
#     def __init__(self, service):
#         self.service = service
#
#         print(f"{self.service} Service가 시작되었습니다.")
#
#
#     def __del__(self):
#         print(f"{self.service} Service가 종료되었습니다.")
#
#
# s = Service("길 안내")
# # del s                             # 종료 전에 모든 객체가 소멸하기 때문에 이 코드 없어도 소멸 print가 작성됨.
#
# print("프로그램이 종료되는 시점")
# del s


'''
응용 예제

1. 다음 지시 사항을 읽고 이름을 저장하는 Person 클래스를 생성하시오.

지시사항

1. 다음과 같은 방법으로 man 과 woman 인스턴스를 생성하시오.
man = Person("james")
woman = Person("emily")

2. man 과 woman 인스턴스가 생성되면 다음과 같은 메시지를 출력할 수 있도록 작성하시오
james is born.
emily is born.

3. 다음과 같은 방법으로 man 인스턴스를 삭제하시오.
del man

4. 인스턴스가 삭제되면 다음과 같은 메시지를 출력할 수 있도록 작성하시오.
james is dead.

'''

# class Person:
#     def __init__(self, name):
#         self.name = name
#         print(f"{self.name} is born.")
#
#     def __del__(self):
#         print(f"{self.name} is dead.")
#
#
# man = Person("james")
# woman = Person("emily")
#
# del man
# print("프로그램이 종료되었습니다.")                 # emily 가 죽은건 프로그램이 종료되었기 때문임.




'''
예제 1
    학생들의 성적을 관리하는 Studnet 클래스를 작성하시오. 이 클래스는
    학생의 이름, 학번, 성적을 인스턴스 변수로 갖습니다.
    
    지시사항
        1) Student 클래스를 정의하고 생성자를 통해 name, student_id, grade을 초기화 하시오.
        2) 학생의 프로필을 출력하는 인스턴스 메서드 print_profile()를 작성하시오. (call1() 타입으로: 매개변수x, 리턴 x)
        3) 학생의 성적을 변경할 수 있는 인스턴스 메서드 set_grade()를 작성하시오
            -> 이 부분이 고민해볼만한 요소입니다. // set_info() 메서드를 검색해보세요 ctrl + shift + f 눌러서
        4) 세 명의 학생 인스턴스를 생성하고, 각 학생의 정보를 출력한 다음,
            성적을 변경하고 다시 출력하세요.
            
    student1 = Stuent("김철수", 20250001, "A")
    student2 = Stuent("이영희", 20250002, "B")
    student3 = Stuent("박민지", 20250003, "C")
    
    실행 예
    
    학생 이름 : 김철수
    학번 : 20250001
    성적 : A
    
    student2 / student3도 출력하시오.
    
    이후 student1 성적을  A+ / studnet2는 A / studnet3 는 B+로 성적을 변경하고
    다시 print_profile을 적용하여 출력하시오.
'''
# 클래스 정의
class Student :
    # 생성자
    def __init__(self, name, student_id, grade):
        self.name = name
        self.student_id = student_id
        self.grade = grade
    # 객체의 인스턴스 변수값을 출력해주는 메서드
    def print_profile(self):                                    # 이런 방식의 잠재적인 문제점
                                                                # 1) 모든 속성을 전부 확인해야 한다는 점.
                                                                # 2) 콘솔에 찍히는 call1() -> 수학적인 연산이 불가능하다는 점.
        print(f"학생 이름 : {self.name}\n학번 : {self.student_id}\n성적 : {self.grade}")

    # 이상의 코드는 콘솔에 찍히기만 할 뿐 연산이 불가능하기 때문에 getter는 call1()유형으로 작성하기 보다는
    # call3() 매개변수x / 리턴o 형태로 작성합니다.
    def get_grade(self):
        return self.grade


    # grade를 바꾸게 될 메서드 -> set_info() : Book 클래스의 set_info() 메서드를 참조하시면 됩니다.

    # setter의 정의
    def set_grade(self, grade):
        if grade not in ["A+", "A", "B+", "B", "C+", "C", "D+", "D", "F"]:
            print("불가능한 점수 입력입니다.")
            return
        self.grade = grade                      # Book클래스에서는 set_info(self, title, author): 로 입력했음.
                                                # 근데 여기처럼 하나씩 바꿀 수도 있다.

student1 = Student("김철수", 20250001, "A")
student2 = Student("이영희", 20250002, "B")
student3 = Student("박민지", 20250003, "C")

student1.print_profile()
student2.print_profile()
student3.print_profile()

#== setter, getter를 사용하는 방법 ==
print("========== 바뀐 성적은 =============")
#student1.set_grade("바보바보야")                 # 직접 입력했기 때문에 결과값이 "불가능한 점수 입력입니다."로 나왔음.
student1.set_grade("A+")
student2.set_grade("A")
student3.set_grade("B+")

student1.print_profile()
student2.print_profile()
student3.print_profile()

print("========== 바뀐 성적만 출력 시 =============")
print(student1.get_grade())
print(student2.get_grade())
print(student3.get_grade())


# 속성값을 직접 참조해서 바꾸는 방법
# student1.grade = "A+"               # 근데 문제점은 A+ 대신 말도 안되는 값을 넣더라도 일단 가능.
# student1.print_profile()

# 이상을 이유로 인스턴스 변수에 값을 대입할 때 제약을 걸기 위해 method를 경유하여 값을 대입하도록 권장함.
# -> 여기서 나온 개념이 setter(call2() 유형)와 getter(call3()유형). 지금은 setter에 해당.
# -> 클래스로 돌아가서 해당 메서드를 추가하겠음.

'''
1. Setter/Getter란?
    1) Setter: 객체의 속성 값(인스턴스 변수)을 변경하는 메서드
    2) Getter : 객체의 속성 값(인스턴스 변수)을 조회하는 메서드
    3) 왜 Setter/Getter를 사용하는가?
        (1) 데이터 보호 및 무결성 유지
            : 속성 값을 직접 변경하는 경우, 잘못된 값이 입력될 가능성이 높음.
            : Setter를 사용하면 특정 조건을 만족하는 값만 속성에 대입가능.
        (2) 객체의 캡슐화(Encapsulation) 실현
            : 객체의 내부 데이터를 외부에서 직접 수정하는 것을 방지
            : 대신 메서드를 통해서만 접근하도록 제한하여 보안성을 높임
        (3) 추후 유지 보수 및 확장성 용이
            : Setter/Getter 를 사용하면 특정 속성에 대한 로직을 쉽게 변경 가능(if 절 바꾸는거 생각하시면 됩니다)
            : 예를 들어, 특정 속성을 설정할 때 추가적인 검증이 필요하면 Setter에서 처리 가능.

2. 이제 클래스를 정의할 때 기본적으로 Setter/Getter를 타이핑하면서 형태를 배울 예정입니다.
    1) Setter : call2()유형 -> 매개변수 o /리턴 x
    2) Getter : call3()유형 -> 매개변수 x /리턴 o
        
'''
# Setter/Getter 적용된 클래스 정의 예시
class Person:
    # 생성자 정의
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    # setter 정의
    def set_name(self, name):
        self.name = name

    # getter 정의
    def get_name(self):
        return self.name


    # set_age /set_address를 정의하는데, set_age의 경우 0미만 및 200 초과는 입력 불가능하게
    # 로직을 작성하시오.

    # get_age/get_address

    def set_age(self, age):
        if age < 0:
            print("0이상 200이하의 나이를 입력하세요. 이전 나이가 유지됩니다.")
            return
        elif age > 200:
            print("0이상 200이하의 나이를 입력하세요. 이전 나이가 유지됩니다.")
            return

        # if age <0 or age>100:                 # 이렇게 해도 된다.
        else:
            self.age = age

    def set_address(self, address):
        self.address = address

    def get_age(self):
        return self.age
    def get_address(self):
        return self.address


# 객체 생성
person = Person("최재혁", 10, "부산")

print(f"제 이름은 {person.get_name()}입니다.")
print(f"제 나이는 {person.get_age()}인데, 만으로는 {person.get_age()-2}살입니다.")            # 이런 이유로 getter 사용됨.
print(f"현재 {person.get_address()}에 살고 있습니다.")

# 불가능한 나이 입력
person.set_age(230)















