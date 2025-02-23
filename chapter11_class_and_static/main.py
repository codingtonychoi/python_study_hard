'''
1. 클래스 변수
    인스턴스 변수 : 인스턴스마다 서로 다른 값을 지니는 변수
    클래스 변수 : 모든 인스턴스가 동일한 값을 지니는 변수

    인스턴스 변수 :
        목적 - 인스턴스마다 서로 다른 값을 저장
        접근방식 - 인스턴스 접근(o)
                - 클래스 접근 (x)

    클래스 변수 :
        목적 - 인스턴스가 공유하는 값을 저장
        접근 방식 - 인스턴스 접근(o)
                - 클래스 접근(o)
'''
from itertools import count


# 클래스 변수 예제
class Korean :
    country = "한국"
    # 인스턴스 변수의 경우 생성자 내부에 있었습니다. 클래스 변수의 경우에는 이상처럼
    # 클래스 내부에 그냥 선언하고 초기화하면 됩니다.

    def __init__(self, name, age, address):
        self.name = name                            # 인스턴스 변수 1
        self.age = age                              # 인스턴스 변수 2
        self.address = address                      # 인스턴스 변수 3

# 객체 생성
man = Korean(name = "최재혁", age = 10, address = "부산")  # keyword argument
print(man.name)                                     # 객체의 속성 확인 방법 (아래 셋다 인스턴스 변수 확인)
print(man.age)
print(man.address)

# 클래스 변스 확인 방법
print(man.country)                                  # 객체명.클래스변수명 을 통한 접근 : 가능
print(Korean.country)                               # 클래스명.클래스변수명 을 통한 접근 : 가능

# 객체명.클래스변수를 통해서 클래스변수에 접근이 가능하긴 하지만 클래스 내부 코드를 들여다보기 전까지는
# country라는 변수가 클래스 변수인지 인스턴스 변수인지 확인이 불가능하다는 문제가 있습니다.
# 이상을 이류로 클래스 변수를 확인하고자 할 때는 객체명.클래스변수명으로 참조하기보다는
# 클래스명.클래스변수명을 통해서 참조하는 것이 바람직합니다.


'''
클래스 메서드 : 클래스 변수를 사용하는 메서드
'''
class Korean2:
    country = "대한민국"            # 클래스 변수 선언 및 초기화

    # 클래스 메서드 정의 방법
    @classmethod                  # 이걸 명시하면 밑의 코드가 클래스 메서드로 작성됨.
    def trip(cls, travelling_site):     # 그 결과 첫번째 매개변수로 self가 아니라 cls가 자동완성
        if cls.country == travelling_site:
            print("국내 여행입니다.")
        else:
            print("해외 여행입니다.")

# 클래스 메서드의 호출
Korean2.trip("대한민국")
Korean2.trip("미국")
# 객체 생성의 과정이 빠져있다. 클래스명으로도 메서드를 생성하고 호출할 수 있다. 그것이 클래스 메서드.

# 객체를 여기서 생성
man2 = Korean2()
man2.trip("일본")
# 클래스 변수 때와 마찬가지로 객체명.클래스메서드명()으로 호출 가능.
# -> 하지만 마찬가지로 얘가 인스턴스 메서드인지 클래스 메서드인지 구분할 수 없기 때문에
# 권장되는 코드 작성 요령은 아닙니다.

'''
2. 클래스 메서드
    : 클래스 변수를 사용하는 메서드
    
    특징 :
        1) 인스턴스 또는 클래스로 호출 -> 하지만 클래스 변수와 마찬가지로 클래스로 호출하는 것이 권장됨
        2) 생성된 인스턴스가 없어도 호출 가능(클래스로 호출가능하니까)
        3) @classmethod 데코레이터(decorator)를 표시하고 작성
        4) 매개변수 self를 쓰지 않고 cls를 사용 -> self는 객체를 의미하기 때문에 인스턴스에 사용함
        
    호출 방식 :
        클래스명.메서드명() -> cls를 통해 클래스변수에만 접근 가능. self를 사용하지 않아 인스턴스 변수에 접근 불가능.
        
Korean2 클래스에서 정의된 trip() 메서드는 클래스 메서드임을 알리는 @classmethod로 시작,
첫번째 매개변수인 cls는 class의 축약어에 해당. 여기서는 클래스 Korean2를 의미함.
따라서 내부의 cls.country는 Korean2.country와 동일한 의미. 이를 클래스 내부에서는 cls.country로 표기.
클래스 메서드는 인스턴스를 생성하지 않아도 클래스만으로 호출 가능. 즉 Korean2.trip(argument)로 호출 가능.


3. 정적 메서드 (static method)
    :  정적 메서드 또한 self를 사용하지 않음. 즉, 인스턴스 변수에 접근하여 사용하는 것이 불가능함을 의미.
        - 클래스 메서드와의 공통점 #1
    인스턴스를 생성하지 않아도 사용할 수 있음.
        - 클래스 메서드와의 공통점 #2
        
    특징 :
        1) 인스턴스 또는 클래스로 호출 가능. -> 클래스 메서도와의 공통점
        2) 생성된 인스턴스가 없어도 호출 가능. -> 클래스 메서드와의 공통점
        3) @staticmethod 데코레이터를 표기하고 작성. -> 클래스 메서드와의 차이점 #1
        4) 반드시 작성해야 할 매개변수(self, cls)가 없음. -> 클래스 메서드와의 차이점 #2
        
정적 메서드는 self, cls를 다 사용하지 않기 때문에 인스턴스/클래스 변수를 모두 사용하지 않는 메서드를 정의하는 경우에 적절함.
정적 메서드는 클래스에 소속되어 있지만, 인스턴스에는 영향을 주지 않고, 또한 영향을 받지도 않음.
'''

class Korean3:
    country = "한국"      # 클래스 변수

    @staticmethod       # 정적 메서드 선언
    def slogan():       # self, cls가 자동 생성 되지 않습니다. -> 인스턴스/클래스 변수를 참조하지 않으니까
        print("Imagine Your Korea!")

    @staticmethod
    def slogan2(str_example):
        print("Imagine Your Korea!" + str_example)

Korean3.slogan()
Korean3.slogan2("근데 너무 춥다..")

'''
기본 예제

가방을 만들 때마다 현재 만들어진 가방이 몇 개인지 계산할 수 있는 Bag 클래스를 정의합니다.
'''

# 클래스 정의
class Bag:
    count = 0           # 클래스 변수 선언 및 초기화

    def __init__(self):             # 생성자/인스턴스 메서드에 해당함. 아무런 @(decorator)가 없으니까요.
        Bag.count += 1              # 객체 하나 생성할 때마다 클래스 변수인 count가 1씩 증가함.
                                    # 인스턴스 메서드가 클래스 변수를 참조할 때는 클래스명.클래스변수명 으로 접근함.
        print("가방이 생산되었습니다.")


    # 클래스 메서드 정의
    @classmethod
    def sell(cls):
        print("가방이 팔렸습니다.")
        cls.count -= 1              # 클래스 메서드가 클래스 변수에 접근하기 때문에 Bag.count가 아니라
                                    # cls.count 입니다.

    @classmethod
    def remain_bag(cls):            # 클래스 변수를 main 단계에서 직접 참조하는 것이 보안상 좋지 않기 때문에
        return cls.count            # 클래스 메서드를 생성(getter 형태로) 하여 참조하는 방식

print(f"현재 가방 재고 : {Bag.count}")                 # 클래스 변수를 직접 참조
print(f"현재 가방 재고 : {Bag.remain_bag()}")          # 클래스 변수를 getter를 통해 메서드를 경유하여 참조 -> 보안상 더 좋음


# 객체 생성
bag1 = Bag()                                    # 생성자 상기하셔야 하는데, 아무런 속성이 없기 때문에 안에 argument 채울 필요없습니다.
print(f"현재 가방 재고 : {Bag.remain_bag()}")      # 클래스 변수를 클래스 메서드를 통해 조작할 수 있습니다.

bag2 = Bag()
bag3 = Bag()
print(f"현재 가방 재고 : {Bag.remain_bag()}")

bag1.sell()                                     # 인스턴스명.클래스메서드명()으로 호출 -> 가능하지만 좀 애매한 방식.
print(f"현재 가방 재고 : {Bag.remain_bag()}")
Bag.sell()                                      # 클래스명.클래스메서드명()으로 호출 -> 더 권장되는 방식.
print(f"현재 가방 재고 : {Bag.remain_bag()}")

'''
이상의 코드에서 보면 예시이기 때문에 적합하다고 보기가 힘든데,
인스턴스명.sell()로 작성한다면 특정한 가방 인스턴스가 팔렸다고 보여질 수 있기 때문에 가독성이 더 높은 반면,
Bag.sell()로 작성하게 된다면 어떤 가방이 팔렸는지는 모르고 그냥 가방 count 변수만 하나 줄었습니다.

따라서 저희는 코딩할 때 변수나 메서드를 인스턴스 수준으로 작성할지 혹은 클래스 수준으로 작성할지에 대한
고민이 선행되어야만 할 겁니다.


응용 예제

1. 다음 지시 사항을 읽고 이름과 전체 인구 수를 저장할 수 있는 Person 클래스를 작성하시오.

지시 사항
1. 다음과 같은 방법으로 man과 woman인스턴스를 생성하시오.
man = Person("안근수")
woman = Person("안근순")

2. man과 woman 인스턴스가 생성되면 다음과 같은 메시지를 출력할 수 있도록 작성하시오.
안근수(이)가 태어났습니다.
안근순(이)가 태어났습니다.

3. 다음 코드를 통해서 전체 인구수를 조회할 수 있도록 작성하시오.
print(f"전체 인구수 : {Person.get_population()}")

4. 다음과 같은 방법으로 man 인스턴스를 삭제하시오.
del man

5. man 인스턴스가 삭제되면 다음과 같은 메시지를 출력할 수 있도록 소멸자를 정의하시오.
RIP 안근수

'''
class Person:
    count = 0
    def __init__(self, name):
        self.name = name
        print(f"{name}(이)가 태어났습니다.")
        Person.count += 1

    def __del__(self):                       # 여기는 인자를 self로만 받아야 함. name이 없어야 함.
        print(f"RIP {self.name}")
        Person.count -= 1

    @classmethod
    def get_population(cls):
        return Person.count

man = Person("재돌")
woman = Person("재순")

#print("프로그램 종료")                           # 프로그램 종료 시 객체가 자동 del 되어 RIP가 뜨므로 구분을 위해 표시
print(f"전체 인구수 : {Person.get_population()}")

del man
del woman

#print("프로그램 종료")
print(f"전체 인구수 : {Person.get_population()}")

'''
클래스 변수 / 클래스 메서드 활용 예제

다음 지시 사항을 읽고 가게의 매출을 구할 수 있는 Shop 클래스를 작성하시오.

지시사항
1. Shop 클래스는 다음과 같은 변수를 갖고 있다.
    total : 가게 전체 매출액
    menu_list : {메뉴명:가격}으로 이루어진 딕셔너리 요소를 가지는 리스트
    menu_list = [{"떡볶이":3000}, {"순대":4000}, {"튀김":500}, {"김밥":2000}]
    
2. 매출이 생기면 다음과 같은 방식으로 판매량을 작성합니다.
Shop.sales("떡볶이", 1)            # 떡볶이를 1개 판매
Shop.sales("김밥", 2)            
Shop.sales("튀김", 5)           

3. 모든 매출을 작성한 뒤, 다음과 같은 방식으로 전체 매출액을 확인합니다.
print(f"매출 : {Shop.get_total()} 원")
'''

class Shop:
    total = 0
    menu_list = [{"떡볶이":3000}, {"순대":4000}, {"튀김":500}, {"김밥":2000}]


    # 객체 생성 안해도 되나봄

    @classmethod
    def sales(cls, menu_name, quantitiy):
        for menu_dict in cls.menu_list:
            # print(item)
            # for key in item:
            #     print(key)
            #     print(item[key])
        # 이상의 부분은 collection의 요소들을 가져오는 반복문에 해당하는데
        # argument로 menu_name을 받은 뒤에 그게 일치하는 key를 찾아내고, 그것의 value*num을 해준 값을 total에 더해주자.

            if menu_name in menu_dict:          # menu_dict의 key 중 menu_name에 해당하는 것이 있다면, 에 해당하는 조건문.
                #print(menu_dict[menu_name])    # 이렇게 하면 dict의 value값이 나옴.
                cls.total += menu_dict[menu_name]*quantitiy
                print(f"{menu_name}을 {quantitiy}개 판매")

    @classmethod
    def get_total(cls):
        return cls.total

    menus = {
        "떡볶이": 3000,
        "순대": 4000,
        "튀김": 500,
        "김밥": 2000,
    }

    @classmethod
    def sales2(cls, menu_key, account):
        # for key in cls.menus:
        #     if key == menu_key:
        if menu_key in cls.menus:
            cls.total += cls.menus[menu_key] * account  # menus(dict)를 정의하면 if문 하나로 처리할 수 있다.
            print(f"{menu_key}을 {account}개 판매")


Shop.sales("떡볶이", 1)
print(f"매출 : {Shop.get_total()} 원")

Shop.sales2("튀김", 6)
print(f"매출 : {Shop.get_total()} 원")
















