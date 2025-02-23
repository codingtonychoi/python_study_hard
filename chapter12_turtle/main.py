
# turtle 이라는 모듈을 사용할 건데, Turtle, Screen 클래스를 import 할 겁니다.

from turtle import Turtle, Screen

t = Turtle()        # Turtle 클래스의 객체 생성, 이름은 t
screen = Screen()   # Screen 클래스의 객체 생성

t.shape("turtle")
t.color("white")
screen.bgcolor("black")

# t.penup()             # pen을 들고 있어서 trace가 안 남음.
# t.forward(100)
# t.pendown()
# t.forward(200)

# for _ in range(10):       # 변수 사용하지 않고 반복만 하기 때문에 _ 사용.
#     t.penup()
#     t.forward(20)
#     t.pendown()
#     t.forward(20)

# t.left(90)
# t.forward(100)

# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)

# for _ in range(4):
#     t.forward(100)
#     t.left(90)

# 정삼각형
# for _ in range(3):
#     t.forward(100)
#     t.left(120)

# 정오각형
# for _ in range(5):
#     t.forward(100)
#     t.left(72)

# 정n각형
# n=8
# for _ in range(n):
#     t.forward(100)
#     t.left(360/n)

# 함수화
def regular_shape(n):
    for _ in range(n):
        t.forward(100)
        t.left(360/n)
#
# regular_shape(6)

#==============선생님=================
def dotted_line():
    for _ in range(10):
        t.forward(5)
        t.penup()
        t.forward(5)
        t.pendown()

# 이상의 함수를 사용하여 사각형을 그린다고 하였을 때

# for _ in range(4):
#     dotted_line()
#     t.left(90)

def draw_dotted_shape(n):
    for _ in range(n):
        dotted_line()
        t.left(360/n)

# n=3
# while n <11:
#     draw_shape()
#     n +=1

#=== 선생님 답===
# for i in range (3,11,1):
#     draw_dotted_shape(i)


# 색 바꾸기
import random
# random = random.Random()
# 구글에 "trinket colors" 검색해서 색의 이름 붙여넣기

colors = ["lawn green", "dodger blue", "gold", "hot pink", "medium purple", "red", "mint cream", "cornflower blue",
          "orange","medium blue", "burlywood", "orange red", "sienna", "medium sea green", "dark grey"]
#chosen_color = random.choice(colors)           # 이렇게 하면 색이 여기서 미리 정해져 버리기 때문에 반복문 내에서는 한 색만 나옴.
                                                # 반복문 내에 random이 들어가야 random이 반복됨.
# for i in range (3,11,1):
#     t.color(random.choice(colors))
#     #draw_dotted_shape(i)
#     regular_shape(i)


def draw_figures(n,m):
    if n >=3 and m >=3 and n < m :
        for i in range (n,m,1):
            t.color(random.choice(colors))
            #draw_dotted_shape(i)
            regular_shape(i)
    else:
        print("도형을 그릴 수 없습니다.")

# draw_figures(4, 4)



#========================== 선생님 답 ===========================

def draw_figures2(n):
    if n < 3:
        print("도형을 그릴 수 없습니다.")
        return                              # 함수에서 return 다음 아무것도 입력하지 않으면 함수 종료
    t.color(random.choice(colors))
    for _ in range(n):
        t.forward(100)
        t.left(360/n)


# draw_figures2(3)
# draw_figures2(4)
# draw_figures2(5)

# for i in range(11):
#     draw_figures2(i)

'''
.heading() 메서드 :
    거북이가 바라보는 방향을 나타내는 속성으로 도(degree) 단위로 나타남.
    
    해당 메서드는 콘솔창에 float 형태로 출력됩니다.
    0도 : 동
    90도 : 북
    180도 : 서
    270도 : 남
    
.setheading() 메서드 :
    특정 각도로 거북이를 회전시키는 메서드.

.circle() 메서드 :
    거북이가 원을 그리는 메서드
'''
# t.forward(100)
# print(t.heading())
# t.right(90)
# print(t.heading())                              # float 값이기 때문에 연산이 가능함.

# t.circle(100)
#
# t.color(random.choice(colors))
# t.setheading(10)
# t.circle(100)
#
# t.color(random.choice(colors))                  # 얘는 제자리에서 돈다. 각도가 계속 10이기 때문인듯.
# t.setheading(10)
# t.circle(100)
#
# t.color(random.choice(colors))                  # 그래서 t.heading() +10 을 넣어준다.
# t.setheading(t.heading() +10)
# t.circle(100)

# spirograph 10도 간격으로
# for _ in range(36):
#     t.circle(100)
#     t.color(random.choice(colors))
#     t.setheading(t.heading()+10)


# 범용성 : 360이 딱 나누어 떨어지는 각도가 아니라면 오류가 남. 이를 해결해보자.
def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):                       # 선생님 : for _ in range(360//size_of_gap)
        t.circle(100)
        t.color(random.choice(colors))
        t.setheading(t.heading()+ size_of_gap)

t.speed(0)
draw_spirograph(5)

# print(300/7)
# print(int(300/7))
# print(300//7)



screen.exitonclick()