
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








