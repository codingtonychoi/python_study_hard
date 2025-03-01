'''
1. 예외 처리의 필요성
    1) 예외 vs. 오류
        예외(exception) : 개발자가 직접 처리할 수 있는 문제
        오류(error) : 개발자가 처리할 수 없는 문제

    2) 예외 처리의 목적 :
        어떤 문제가 발생했을 때 그 문제를 해결해 주는 것이 아니라,
        발생된 문제로 인해 프로그램이 비정상적으로 종료되는 것을 막고,
        사용자에게 발생한 문제에 대해 정보를 전달하기 위함.

'''
# 2 / 0
# 2를 0으로 나누는 것은 불가능.
# 오류 시 시뻘건게 뜨고 이때까지는 코드를 다시 읽고 바꿨다. 잘되면 땡큐, 안되면 망함.
'''
  2 / 0               
    ~~^~~
ZeroDivisionError: division by zero

와 같은 방식으로 프로그램이 정상적으로 종료되지 않으며(Process finished with exit code 1),
보기에 좋지도 않기 때문에, 예외를 처리하면 좋다.


2. 예외 처리
    1) 고전적인 예외 처리
        : 다음과 같이 했다.
'''
# a = int(input("나누는 수를 입력하세요. >>> "))
# b = int(input("나누어 지는 수를 입력하세요. >>> "))
# if a == 0:
#     print("0으로 나눌 수 없습니다.")
# else:
#     print(f"b/a = {b/a}")


# 알파테스트 : 개발자들끼리 하는 테스트
# 베타테스트 : 일반일들도 참여하는 테스트 -> 알파테스트 결과와 차이가 있다.(이런식으로 생각해보면 개발자들이 예외처리를 모두하기에는 한계가 있다.)

'''
어떤 값이든 0으로 나눌 수 없기 때문에 if a==0 을 통해 0으로 나누는 것을
아예 시도할 수 없도록 예외처리 함.

여기서 생각할 수 있는 잠재적인 문제는 :
    1) 어떤 문제가 발생할 지 예상할 수 있어야 미리 대비할 수 있다.
    2) 어떤 문제가 발생할 지 예상할 수 있더라도 대비할 수 없는 경우가 있다.


3. 예외의 종류
+------+---------------------+-------------------------------------------+
| 순번 |     예외 클래스     |                    의미                   |
+------+---------------------+-------------------------------------------+
|  1   |    BaseException    |             최상위 예외 클래스            |
|  2   |      Exception      |      대부분 예외 클래스의 슈퍼 클래스     |
|  3   |   ArithmeticError   |         산술연산에 문제가 있을 때         |
|  4   |    AttributeError   |          잘못된 속성을 참조할 때          |
|  5   |       EOFError      | 파일에서 더이상 읽어들일 데이터가 없을 때 |
|  6   | ModuleNotFoundError |          import할 모듈이 없을 때          |
|  7   |  FileNotFoundError  |          존재하지 않는 파일일 때          |
|  8   |      IndexError     |         잘못된 인덱스를 사용할 때         |
|  9   |      NameError      |       잘못된 이름(변수)를 사용할 때       |
|  10  |     SyntaxError     |              문법이 틀렸을 때             |
|  11  |      TypeError      |  계산하려는 데이터의 유형이 잘못되었을 때 |
|  12  |      ValueError     |   계산하려는 데이터의 값이 잘못되었을 때  |
+------+---------------------+-------------------------------------------+

'''

from prettytable import PrettyTable
table = PrettyTable()                                # 객체 선언
table.field_names = ["순번", "예외 클래스", "의미"]
table.add_row(["1", "BaseException", "최상위 예외 클래스"])
table.add_row(["2", "Exception", "대부분 예외 클래스의 슈퍼 클래스"])
table.add_row(["3", "ArithmeticError", "산술연산에 문제가 있을 때"])
table.add_row(["4", "AttributeError", "잘못된 속성을 참조할 때"])
table.add_row(["5", "EOFError", "파일에서 더이상 읽어들일 데이터가 없을 때"])
table.add_row(["6", "ModuleNotFoundError", "import할 모듈이 없을 때"])
table.add_row(["7", "FileNotFoundError", "존재하지 않는 파일일 때"])
table.add_row(["8", "IndexError", "잘못된 인덱스를 사용할 때"])
table.add_row(["9", "NameError", "잘못된 이름(변수)를 사용할 때"])
table.add_row(["10", "SyntaxError", "문법이 틀렸을 때"])
table.add_row(["11", "TypeError", "계산하려는 데이터의 유형이 잘못되었을 때"])
table.add_row(["12", "ValueError", "계산하려는 데이터의 값이 잘못되었을 때"])

print(table)

'''
4. 예외 처리 방식
    1) 모든 예외를 처리하는 방식 -> try / except 문
    
    형식 :
try :
    코드 작성 영역
except :
    예외 발생 시 처리 영역
    
'''
# try :
#     a = int(input("나누는 수를 입력하세요 >>> "))
#     b = int(input("나누어지는 수를 입력하세요 >>> "))
#     print(f"b/a = {b/a}")
# except :
#     print("예외가 발생하였습니다.")

# a = 0 을 넣어 위 코드를 실행하면 Process finished with exit code 0 로 오류는 안 나지만,
# 왜 예외가 발생했는지 알려주진 않음.
# a = 이십칠 을 넣는다면 b 안받고 바로 예외가 발생했다고 나옴.

'''
기본 예제

다음은 사용자가 입력한 키를 정수로 반올림해서 다시 저장하는 프로그램입니다.
try/except 문을 사용하여 "예외가 발생하였습니다."를 출력할 수 있도록 작성하세요.
'''
# try :
#     height = input("키를 입력하세요 >>> ")             # 결과값이 str인데, str을 round 처리할 수가 없어서 예외 발생.
#     height = round(height)
#     print(f"입력하신 키는 {height}cm로 처리됩니다.")
# except:
#     print("예외가 발생하였습니다.")

'''
    2) 특정 예외만 처리하는 방식
        try/except문을 사용하면 기본적으로 예외의 종류에 상관없이 모든 예외가 처리됨.
        하지만 이상에서 본 것처럼 0으로 나누는 경우와, 정수가 아닌 값을 입력한 경우에
        서로 다른 메시지를 출력한다면, 개발자에게 예외를 처리할 수 있을만한 정보를
        제공할 수 있음(아까 전까지의 예시는 예외 발생 후에 개발자가 어떤 코드에 문제가 있었는지
        스스로 확인해야했다는 점에서 편의성 개선 측면으로 볼 수 있음).
        
        2-1) 0으로 나누려고 하는 경우 : 0으로 나눌 수 없습니다.
        2-2) 정수가 아닌 값을 입력하는 경우 : 정수만 입력할 수 있습니다.
        로 특정 예외에 따른 서로 다른 안내문을 제시한다고 할 때,
        except 문 뒤에 처리하고자 하는 예외를 모두 명시하면 됩니다.
'''

# a = int(input("나누는 수를 입력하세요 >>> "))
# b = int(input("나누어지는 수를 입력하세요 >>> "))
# print(f"b/a = {b/a}")

'''
위 코드에서는
ZeroDivisionError
ValueError
가 나온다는 걸 시험해보면 알 수 있다.
'''

# try :
#     a = int(input("나누는 수를 입력하세요 >>> "))
#     b = int(input("나누어지는 수를 입력하세요 >>> "))
#     print(f"b/a = {b/a}")
#
# except ZeroDivisionError:                       # 이렇게 error 종류를 복붙하면 됨.
#     print("0으로 나눌 수 없습니다.")
# except ValueError:
#     print("정수만 입력할 수 있습니다.")

# 아래처럼 Error 하나 덜 뜨게 축약할 수도 있다.
# try :
#     a = int(float(input("나누는 수(정수만)를 입력하세요 >>> ")))
#     b = int(float(input("나누어지는 수(정수만)를 입력하세요 >>> ")))
#     print(f"b/a = {b/a}")
#
# except ZeroDivisionError:
#     print("0으로 나눌 수 없습니다.")


'''
        거의 모든 예외는 Exception  클래스의 서브 클래스입니다. 따라서 모든 예외는
        Exception의 인스턴스가 됩니다. 다음과 같이 마지막에 작성하는 except문 뒤에 Exception을 명시하면
        예상하지 못한 예외들도 모두 처리할 수 있게 됩니다.
        
형식 :

try :
    코드 작성 영역
except 예외 클래스 1:
    예외 메시지1
except 예외 클래스 2:
    예외 메시지2
    ...
    
except 예외 클래스 n-1:
    예외 메시지n-1
    
except Exception:                           # 이렇게 맨 마지막에는 위의 except들이 처리하지 못하는 예상못한 예외를 처리하기 위해
    예외 메시지n                              # Exception 으로 마무리
    
    
    
5. 예외 메시지 처리하기
    지금까지는 직접 예외 메시지를 만들어서 사용했지만 기본적으로 예외 메시지를 이미 가지고 있는 경우도 있습니다.
    디폴트 에러 메시지를 출력하는 방식에 대해서 학습합니다.
    
    형식 :
    
try :
    코드 작성 영역
except 예외클래스 as 예외메시지:
    예외 발생 시 처리 영역    
 
'''

# z = [10, 20, 30, 40, 50]
# #print(z[10])                # IndexError: list index out of range 뜬다.
#
# try:
#     print(z[10])
# except IndexError as e:
#     print(e)

'''
6. else / finally 문
    try / except 문에 추가로 else와 finally문을 사용할 수 있음.
    else : 예외가 발생하지 않으면 처리되는 구문
    finally : 예외 발생 여부와 관계없이 맨 마지막에 항상 처리되는 구문
    
    형식 :
try :
    코드 작성 영역
except :
    예외 발생 시 처리 영역
else :
    예외가 없을 시 처리 영역
finally :
    언제나 실행되는 영역
'''
# try :
#     a = int(input("나누는 수를 정수로 입력 >>> "))
#     b = int(input("나누어지는 수를 정수로 입력 >>> "))
#     result = b/a
# except ZeroDivisionError as e:          # division by zero
#     print(e)
# except ValueError as e:                 # invalid literal for int() with base 10: '3.2'
#     print(e)
# else :
#     print(f"b/a = {b/a}")
# finally :
#     print("프로그램이 종료되었습니다.")

'''
7. 강제로 예외 발생시키기
    어떤 사람이 나이를 정수로 입력받는 프로그램이 있다고 가정했을 때,
    컴퓨터 상으로는(그리고 파이썬 상으로는) -1000이 정수이기 때문에 예외가 발생하지 않습니다.
    하지만 -1000살이 될 수는 없기 때문에 직접 예외를 발생시켜서 처리해야만 합니다.
    
    -> raise문
    
    형식 :
raise 예외클래스()                   # 이건 사용자가 정의하는 겁니다.

또는 

raise 예외클래스(예외메시지)

raise는 강제로 예외를 발생시킨다는 점에서 주로 사용되는 예외 클래스는 Exception 입니다.
'''

# age = int(input("나이를 입력하세요 >>> "))              # -1000 입력 시 예외가 발생하지 않음.
# print(f"당신의 나이는 {age}살입니다.")                   # 파이썬 상에서는 문제가 없지만 현실 세계에서 생기는 예외.

#
# try :
#     age = int(input("나이를 입력하세요 >>> "))
#     raise Exception("강제로 발생시킨 예외입니다.")       # 이 경우는 멀쩡한 숫자를 입력해도 예외가 발생함.
#                                                     # 특정 조건일 때만 raise되게 하려면 8. 사용자 정의 예외 클래스 를 알아야함.
# except Exception as e:
#     print("발생한 예외 메시지는 다음과 같습니다.")
#     print(e)



'''
8. 사용자 정의 예외 클래스

    음수를 입력받을 때 강제로 예외를 발생시키는 예외 클래스 정의
'''
class NegativeAgeError(Exception):                  # 클래스명(부모클래스) -> 상속 개념
#     """사용자 정의 예외 클래스 : 나이가 음수일 때 발생"""
    pass                                            # 예외를 발생시키기만 하면 되기 때문에 따로 코드 작성 필요 없음.
#                                                     # -> Exception 클래스를 상속받았기 때문에 메서드 사용 가능.
# try:
#     age = int(input("나이를 입력하세요 >>> "))
#     if age < 0:
#         raise NegativeAgeError("나이는 음수일 수 없습니다.")
# except NegativeAgeError as e:
#     print("발생한 예외 메시지는 다음과 같습니다.")
#     print(e)


'''
나이를 200 초과 입력했을 때 '강제로 TooManyAgeError를 발생시키고' '불가능한 나이 입력입니다'를
출력하는 예외 클래스를 정의하고 이상의 코드에 추가하시오.
나이를 실수로 입력했을 때 나타나는 예외를 처리하고 default 에러 메시지를 출력하시오.
예상할 수 없는 예외가 발생했을 때 처리하는 예외 구문을 작성하시오.
else 문을 통해 정상적으로 처리되었을 때 당신의 나이는 __살입니다.  가 출력되도록 작성하시오.
finally 구문을 통해 프로그램이 종료되었습니다. 가 출력되도록 작성하시오.
'''

# class TooManyAgeError(Exception):              # class 정의 꼭 해주고, try에 if - raise 써야, except 문에 쓸 수 있다.
#     pass
#
# try:
#     age = int(input("나이를 입력하세요 >>> "))
#     if age < 0:
#         raise NegativeAgeError("나이는 음수일 수 없습니다.")
#     if age > 200:
#         raise TooManyAgeError("불가능한 나이 입력입니다.")
#
# except NegativeAgeError as e:
#     print("발생한 예외 메시지는 다음과 같습니다.")
#     print(e)
# except TooManyAgeError as e:
#     print("발생한 예외 메시지는 다음과 같습니다.")
#     print(e)
#
# except ValueError as e:                     # default 에러 메시지 출력하라고 했으니까 굳이 메시지 안써도됨.
#     print(e)
#
# except Exception as e:
#     print(e)
# else:
#     print(f"당신의 나이는 {age}살입니다.")
# finally:
#     print("프로그램이 종료되었습니다.")

'''
과제

사용자의 점수를 0 이상 100이하로 입력받아서 점수가 80점 이상이면 합격, 아니면 불합격을 출력하는
프로그램을 작성하는데, 0이상 100이하의 유효한 값이 아니라면 예외를 발생시키고
'점수는 0이상 100이하입니다'라는 예외 메시지를 출력하시오. -> 사용자 정의 예외 클래스를 정의해야겠죠.
ScoreOutOfRangeError 클래스를 정의해서 사용하겠습니다.

입력 받는데 예를 들어 백점이라고 입력하면 '점수는 숫자로 입력해야합니다.'라는 메시지를 출력하세요.
실수로 입력하면 '정수로 입력해야 합니다.'라는 메시지를 출력하세요.

예상할 수 없는 예외가 발생 시 Exception을 적용하여 디폴트 에러 메시지를 출력하세요.

프로그램이 종료되었다는 메시지를 맨 마지막에 작성하세요.

'''
class ScoreOutOfRangeError(Exception):
    pass
try :
    score = int(input("점수를 입력하세요 >>> "))
    if score < 0 or score >100:
        raise ScoreOutOfRangeError("점수는 0이상 100이하입니다.")

except ScoreOutOfRangeError as e :
    print(e)

except ValueError:
    print("정수로 입력해야 합니다.")

# except TypeError:                                     # 이것도 ValueError 안에 속해서 구분하고 싶다면 class 정의해야 함.
#     print("점수는 숫자로 입력해야합니다.")

# except ValueError:
#     if type(score) ==  float:                         # 이렇게 나눌 수가 없는게 받은게 이미 int가 아닌거에서 error가 난거임.
#         print("점수는 숫자로 입력해야합니다.")
#     if type(score) == str:
#         print("정수로 입력해야 합니다.")

except Exception as e:
    print(e)

else:
    if score >= 80 :
        print(f"합격입니다.")
    else:
        print(f"불합격입니다.")
finally:
    print("프로그램이 종료되었습니다.")

# print(type(3.3))

'''
사용자로부터 숫자를 입력받아 해당 숫자로 100을 나누는 값을 출력하는 프로그램을 작성하시오.
만약 사용자가 0을 입력하거나 숫자가 아닌 값을 입력하면 적절한 예외 메시지를 출력하시오.

지시사항
1. 사용자로부터 숫자를 입력받는다.
2. 입력 받은 숫자로 100을 나누어 결과를 출력한다.
3. 입력값이 0일 경우 적절한 예외를 처리하여 '0으로 나눌 수 없습니다'라는 메시지를 출력한다.
4. 입력값이 숫자가 아닌 경우 적절한 예외를 처리하여 '숫자만 입력할 수 있습니다'라는 메시지를 출력한다.
5. 예외가 발생하지 않는 경우 '정상적으로 처리되었습니다.'라는 메시지를 출력하고, 결과도 출력한다.
6. 프로그램 종료 메시지를 출력한다.
'''
try :
    num = float(input("100을 무슨 숫자로 나눌까요? >>> "))
    result = 100/num                            # 굳이 result를 쓰는 이유가 아래에 있다.

except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")

except ValueError:
    print("숫자만 입력할 수 있습니다.")

except Exception as e:
    print(e)

else:
    print(f"정상적으로 처리되었습니다.")
    #print(f"{100/num}.")                       # 위에서는 except ZeroDivisionError 때문에 오류 안나는데
    print(f"{result}")                          # else로 넘어와서 이 줄에서 100/num에 오류가 난다.
                                                # 이상을 이유로 result라는 중간단계를 거쳐서 작성함.

finally:
    print("프로그램이 종료되었습니다.")


'''
사용자로부터 리스트의 인덱스를 입력받아 해당 인덱스의 값을 출력하는 프로그램을 작성하시오.
만약 잘못된 인덱스를 입력하면 적절한 예외 메시지를 출력하시오.

지시사항
1. 미리 정의된 리스트가 있다.
2. 사용자로부터 리스트의 인덱스를 입력받는다.
3. 입력받은 인덱스를 사용하여 리스트의 값을 출력한다.
4. 인덱스가 리스트의 범위를 벗어나면 적절한 메시지를 출력한다.
5. 사람을 의심하고 예상되는 예외를 적용한다.
6. 예외가 발생하지 않는 경우 "정상적으로 처리되었습니다" 라는 메시지와 함께 해당 인덱스의 값을 출력한다.
7. 프로그램 종료 메새지를 출력한다.
8. 마이너스 인덱스는 적용시키지 않는다. -> 사용자 정의 예외 클래스를 통해서 적용합니다.
-> NegativeNumIndexError 라고 이름 짓고 처리하겠습니다.
'''
# 예외 목록 : IndexError / ValueError / TypeError / NegativeNumIndexError / Exception
class NegativeNumIndexError(Exception):
    pass
my_list = [10, 20, 30, 40, 50]
try:
    index_num = int(input("인덱스 넘버를 입력하세요 >>> "))
    chosen_element = my_list[index_num]                  # 이전 문제처럼 원하는 출력값을 여기서 정의해야 생기는 오류들을 미리 확인가능.
                                                         # else에 처음 넣으면 위에 오류들은 다 안생기는 걸로 됨.
    if index_num < 0:
        raise NegativeNumIndexError("마이너스 인덱스는 적용하지 않습니다.")
except NegativeNumIndexError as e:
    print(e)
except ValueError as e:
    print("정수만 입력할 수 있습니다.")
    print(e)

except IndexError as e:
    print("list의 범위를 벗어났습니다.")
    print(e)

except TypeError as e:                          # 사실 try에서 이까지는 넘어가지 못하게 코딩되어 있음.
    print("자료형이 잘못 입력되었습니다.")
    print(e)
except Exception as e:
    print("예측할 수 없는 예외가 발생하였습니다.")
    print(e)
else :
    print("정상적으로 처리되었습니다.")
    print(f"{index_num} 위치에 있는 값은 {chosen_element}입니다.")
finally:
    print("프로그램이 종료되었습니다.")

'''
사용자로부터 속성명을 입력받아 객체의 해당 속성을 출력하는 프로그램을 작성하시오.
만약 사용자가 잘못된 속성을 입력하면 적절한 예외처리 메시지를 출력하시오.

지시사항
1. 미리 정의된 클래스와 객체가 있다.
2. 사용자로부터 속성명을 입력받는다.
3. 입력받은 '속성명'을 사용하여 객체의 '속성값'을 출력한다.
4. 잘못된 속성명을 입력하면 '존재하지 않는 속성입니다.'라는 메시지를 출력한다.
5. 예외가 발생하지 않는 경우 '정상적으로 처리되었습니다'라는 메시지와 속성값을 출력한다.
6. 프로그램 종료 메시지를 출력한다.
'''

# 클래스 정의
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 객체 생성
person1 = Person(name="John", age=10)       # keyword argument로 객체 생성
# attribute = input("출력할 속성명을 입력하세요. >>> ")

# #name을 보고싶으면
# print(person1.name)
# #근데 아래같이 쓸수는 없다.
# print(person1.attribute)
# #그래서 배워야하는게 있음.

'''
getattr(객체명, 속성명-> 대입된 애가 들어가야함) 함수 :
이상의 코드를 예시로 생각했을 때,
Person 클래스 내부에 있는 인스턴스 변수명을 그대로 집어넣는 것은 불가능하고
input을 통해서 받은 str 데이터를 대입했을 때 가능.

vars() : 객체의 속성명 - 값 을 dictionary의 키 - 값 의 쌍으로 바꿔주는 함수
'''

#======================== 풀이 1. getattr() 을 사용 ===========================
# print(getattr(person1, name))         # 이렇게 하면 안나옴.
# print(getattr(person1, attribute))      # 이런 식으로 사용해야함.

try:
    attribute = input("출력할 속성명을 입력하세요. >>> ")
    again = getattr(person1, attribute)
except AttributeError as e:
    print("존재하지 않는 속성명입니다.")
    print(e)

except Exception as e:
    print("예측할 수 없는 예외가 발생했습니다.")
    print(e)

else :
    print("정상적으로 처리되었습니다.")
    print(again)

finally:
    print('프로그램이 종료되었습니다.')

#========================= 풀이 2. vars() 을 사용 ===========================
# 객체를 dictionary 로 변환
profile = vars(person1)
attribute2 = input("출력할 속성명을 입력하세요. >>> ")
# for key in profile:                     # dictionary에서 반복문 돌리면 key만 튀어나옵니다.
#     print(key)                          # value를 조회하기 위해서는 추가적으로 작성해야만 했습니다.
#     print(profile[key])
try :

    if attribute2 in profile:                   # profile의 key 중에 attribute2와 일치하는 것이 있는지 묻는 조건문
        print("정상 출력이 가능합니다.")
    else:
        raise KeyError

except KeyError as e:
    print(e)
    print("존재하지 않는 속성입니다.")

except Exception as e:
    print(e)
    print("예측할 수 없는 예외가 발생했습니다.")
else:
    print(f"{attribute2}의 속성값은 {profile[attribute2]}입니다.")
finally:
    print("프로그램이 종료되었습니다.")












