'''
1. 클래스 도입의 필요성
'''

# 매개 변수가 6개인 함수를 하나 정의합니다.
def student_info(name, department, professor, phone, address, grade):
    print(name)
    print(department)
    print(professor)
    print(phone)
    print(address)
    print(grade)

name1 = "최재혁"
department1 = "ENT"
professor1 = "Mun"
phone1 = "010-1111-1111"
address1 = "양산"
grade1 = "A"

# 함수호출
student_info(name1, department1, professor1, phone1, address1, grade1)

'''
지금까지 배운 함수와 매개변수, 그리고 argument를 통해 6개의 변수를 처리했습니다.
하지만 만들어야 할 변수의 개수가 많고, 학생 한명당 매개변수가 6개라면, 학생이 100명일 경우 600개의
변수를 처리할 필요가 있습니다.
'''

# keyword argument 사용해서 함수호출
student_info(grade="B", address="부산", phone="010-2222-2222", professor="Cho",
             department="ENT", name="이민수")

# name2, ..., grade2라는 변수를 선언하고, 거기에 여러분의 정보를 입력한 뒤
# keyword argument를 통해서 student_info() 함수를 호출하시오.
name2 = "신민숭"
department2 = "RAD"
professor2 = "Kim"
phone2 = "010-3333-3333"
address2 = "장전"
grade2 = "C"

student_info(name2, department2, professor2, phone2, address2, grade2)
student_info(name=name2, department=department2, professor=professor2, phone=phone2, address=address2, grade=grade2)

'''
이상의 상황들(변수에 각각 데이터를 대입한 후에 함수의 argument로 사용하거나, 혹은 데이터를 직접 argument에 등록)을
벗어나기 위해 클래스와 객체 개념을 도입합니다.

class 란? : 객체를 만드는 도구 (설계도/틀 등)

    자동차 설계도 -> 클래스
    설계도를 통해 생성된 자동차들 -> 객체
    
    같은 설계도로 만든 자동차라 하더라도 서로 다른 옵션을 가질 수 있습니다.
    마찬가지로 같은 클래스로 만든 객체라 하더라도 서로 다른 값을 가질 수 있습니다.
    
    인스턴스(instance) 역시 클래스를 이용해서 생성한 객체를 가리키는 용어입니다.
    객체와 인스턴스는 그 둘을 바라보는 관점의 차이로 볼 수 있습니다.
    
    1) '자동차 설계도'로 만든 자동차 하나하나는 객체(object)입니다.
    2) '자동차'라는 생산품은 자동차 설계도의 인스턴스(instance)입니다.
    
1. 클래스 정의
    클래스를 작성하는 것을 클래스 정의라고 합니다. -> 함수 정의와 비슷
    
    1) 형식 :

class 클래스명(대문자로 시작):
    본문
-------------------------
    2) 객체생성형식 :

객체이름 = 클래스명()
    
'''

# 클래스 정의 형식 예시
class WaffleMachine :                   # 클래스명은 대문자로 작성. Pascal Case로 표기함. python에서 변수는 snake_case 로 표기.
    pass

# 객체 생성 예시
waffle = WaffleMachine()
print(waffle)
'''
실행 시 <__main__.WaffleMachine object at 0x100c735c0> 라고 표기된 점을 미루어 보아
waffle은 WaffleMachine의 객체임을 확인할 수 있음.

클래스의 구성

1. 클래스의 기본 구성
    객체를 만들어내는 클래스는 객체가 가져야할 구성요소를 지닙니다.
    객체를 생성하기 위해서는 클래스는 객체가 가져야 할 '값'과 '기능'을 지녀야 합니다.
    
    값 = 속성(attribute)
    기능 = 메서드(method)
    
    클래스를 구성하는 변수는 두 가지로 구분됩니다.
        1) 클래스 변수 : 클래스를 기반으로 생성된 모든 인스턴스들이 공유하는 변수
        2) 인스턴스 변수 : 인스턴스들이 개별적으로 가지는 변수
        
    메서드는 특징에 따라서
        1) 클래스 메서드
        2) 정적 메서드
        3) 인스턴스 메서드
        
    인스턴스 변수 : 클래스를 기반으로 만들어지는 모든 인스턴스들이 각각 따로 저장하는 변수를 의미
        모든 인스턴스 변수는 self라는 키워드를 앞에 붙여준다.
    인스턴스 메서드 : 인스턴스 변수를 사용하는 메서드
        인스턴스 변수값에 따라서 각 인스턴스마다 다르게 동작됩니다.
        인스턴스 메서드는 첫번째 매개변수로 self를 추가해야 합니다.
        
'''

# class Person:
#     def display_info(self, name, age, tel, address):
#         self. tel = tel
#         self.address = address

# class Person:
#     # call1() /  매개변수 없음. return 없음.
#     def display_info(self):
#         print(f"이름 : {self.name}")
#         print(f"나이 : {self.age}")
#         print(f"연락처 : {self.tel}")
#         print(f"주소 : {self.address}")
#
#     # call3() / 매개변수 없음. return 있음
#     def display_info2(self):
#         return f"제 이름은 {self.name}이고, {self.age}살입니다.\n연락처는 {self.tel}이며, 주소는 {self.address}입니다."

# 객체 생성
# person01 = Person()
# print(person01)         # 객체명으로 그대로 출력할 수 없음 (주소값만 출력)
# person01.set_info("최재혁", 10, "010-0000-0000", "부산시")
# print(person01.display_info())          # 클래스에서 정의한 method 사용 -> 메서드 호출 방식 객체명.메서드명()

# person02 객체를 생성하시고, person02.set_info()를 활용하여 여러분 이름 나이 연락처 주소를 입력하고
# display_info2() (call 3() 유형으로 작성) 를 정의하여 다음 실행 예와 같이 출력되도록 작성하시오.
# 제 이름은 ___이고, ___살입니다.
# 연락처는 ___인데, ___에 살고 있습니다.
# 코드 실행
# print(person02.display_info2())


# person02 = Person()         # 객체 생성은 완료
# person02.set_info("최재", 20, "010-0000-0101", "부산시")

# method의 정의는 class 내부에서 이루어져야 함.
#
# person02.display_info()
# print(person02.display_info2())

'''
응용 예제

다음 지시사항을 읽고 책 제목과 저자정보를 저장할 수 있는 Book 클래스를 생성하세요 -> 객체도 생성하고, 실행 예를 구현하세요.
1. 다음과 같은 방법으로 book1과 book2 인스턴스를 생성하세요.

book1 = Book()
book2 = Book()

2. set_info(self, title, author)를 통해 책 제목을 입력하세요.

3. display_info()를 통해 실행 예와 같이 출력되도록 작성하세요.

실행 예
책 제목 : 파이썬
책 저자 : 민경태
책 제목 : 어린왕자
책 저자 : 생택쥐페리
'''

class Book:
    def set_info(self, title, author, stock):
        self.title = title
        self.author = author
        self.stock = stock

    def display_info(self):
        print(f"책 제목 : {self.title}\n책 저자 : {self.author}")

# 클래스 내부에 method들을 정의해야함

book1 = Book()
book2 = Book()

# 어떤 method 를 사용해서 속성에 값을 대입하고, 어떤 method를 사용하여 정보를 출력할지 코드를 작성해야함.

book1.set_info("파이썬", "민경태", stock = 3)
book2.set_info(author = "생택쥐페리", title = "어린왕자", stock = 10)            # keyword argument  형식으로 작성함.

book1.display_info()
book2.display_info()


# 특정 객체의 속성값을 확인하는 방법            -> (객체명.속성명) 의 형식
print(book1.title)
# 그러면 특정 속성값만 꺼내는 이유             -> 연산을 할 수 있다.
print(book1.stock +2)








