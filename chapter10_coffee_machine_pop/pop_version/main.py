MENU = {
    "에스프레소" : {
        "재료" : {
            "물" : 50,
            "커피" : 18,
        },
        "가격" : 1.5,
    },
    "라떼" : {
        "재료" : {
            "물": 200,
            "우유":150,
            "커피": 24,
        },
        "가격" : 2.5,
        },
    "카푸치노" :{
        "재료": {
            "물": 250,
            "우유": 100,
            "커피": 24,
        },
        "가격" : 3.0,
    }
}

# print(MENU)
# print(MENU["라떼"])
# print(MENU["라떼"]["재료"])                      # 이까지는 자료형이 모두 dict
# print(MENU["라떼"]["재료"]["우유"])               # 자료형이 int. 연산이 가능해진다.

# 카푸치노의 가격을 콘솔에 출력하세요
# 에스프레소의 물의 양을 콘솔에 출력하세요

# print(MENU["카푸치노"]["가격"])
# print(MENU["에스프레소"]["재료"]["물"])

# profit = 0
# resources = {
#     "물" : 300,
#     "우유" : 200,
#     "커피" : 100,
# }



# resources 에서 에스프레소를 두잔 뽑았을 때, 남는 물, 우유, 커피량을 연산하고,
# 그 결과를 콘솔에 출력하시오.

# resources["물"] -= 2* MENU["에스프레소"]["재료"]["물"]
# resources["우유"] -= 0
# resources["커피"] -= 2* MENU["에스프레소"]["재료"]["커피"]
#
# print(resources)

# 이상을 진행했을 때 커피 두잔이 자판기에서 나왔기 때문에 자판기에는 돈이 들어가있겠죠.
# 자판기 profit 변수에 적절한 가격을 대입하시오.

# profit += MENU["에스프레소"]["가격"] *2
#
# print(profit)

'''
resources dict과 profit dict을 가져옴.

이전에는 main에 다 작성해서 했다면 이제는 함수를 만들어볼거다.
'''
#=============================== 나의 시도 -> 최종 파일은 main2 파일에 ============================
profit = 0

resources = {
        "물": 300,
        "우유": 200,
        "커피": 100,
    }


def print_resources():
    print(f"물: {resources["물"]}ml\n우유: {resources["우유"]}ml\n커피: {resources["커피"]}g\n돈: ${profit}")



# off라고 입력되면 종료될 것.
# report라고 입력되면 resources와 profit을 참조하여 manual과 같은 방식으로 console에 출력될 것.
# 잘 못 입력했을 경우 "잘 못 입력하셨습니다." 라는 안내문이 출력될 것.
# 이까지를 조건문으로 main에 작성.

class Drink :
    def __init__(self, price, water, milk, coffee):
        self.price = price
        self.water = water
        self.milk = milk
        self.coffee = coffee

    def set_price(self, price):
        self.price = price
    def set_water(self, water):
        self.water = water
    def set_milk(self, milk):
        self.milk = milk
    def set_coffee(self, coffee):
        self.coffee = coffee

    def get_price(self):
        return self.price
    def get_water(self):
        return self.water
    def get_milk(self):
        return self.milk
    def get_coffee(self):
        return self.coffee

    # def upgrade_profit(self, profit):
    #     profit += self.price()
    #
    # def upgrade_water(self, resources):
    #     if resources["물"] >= self.water():
    #         resources["물"] -= self.water()
    #     else:
    #         print("물 부족")
    #         return
    #
    # def upgrade_milk(self, resources):
    #     if resources["우유"] >= self.milk():
    #         resources["우유"] -= self.milk()
    #     else:
    #         print("우유 부족")
    #         return
    #
    # def upgrade_coffee(self, resources):
    #     if resources["커피"] >= self.coffee():
    #         resources["커피"] -= self.coffee()
    #     else:
    #         print("커피 부족")
    #         return

def print_resources():
    print(f"물: {resources["물"]}ml\n우유: {resources["우유"]}ml\n커피: {resources["커피"]}g\n돈: ${profit}")


espresso = Drink(1.5, 50, 0, 18)
latte = Drink(2.5, 200, 150, 24)
capuccino = Drink(3.0, 250, 100, 24)

#================================= 1차 시도 ====================================
# end_of_coffee_machine = False
#
# while not end_of_coffee_machine:
#
#     choice = input("어떤 음료를 드시겠습니까? >>> (에스프레소/라떼/카푸치노)")
#
#     if choice == "off":
#         end_of_coffee_machine = True
#
#     elif choice == "report":
#         print_resources()
#
#     elif choice in ("에스프레소", "라떼", "카푸치노"):
#
#         if choice == "에스프레소":
#             if resources["물"] < espresso.get_water():
#                 print("물 부족")
#             if resources["우유"] < espresso.get_milk():
#                 print("우유 부족")
#             if resources["커피"] < espresso.get_coffee():
#                 print("커피 부족")
#             else:
#                 quarter = int(input("지닌 쿼터 개수를 입력하세요"))
#                 dime = int(input("지닌 다임 개수를 입력하세요"))
#                 nickel = int(input("지닌 니켈 개수를 입력하세요"))
#                 pennies = int(input("지닌 페니 개수를 입력하세요"))
#
#                 money = quarter * 0.25 + dime * 0.10 + nickel * 0.05 + pennies * 0.01
#
#                 if choice == "에스프레소":
#                     if money < 1.50:
#                         print("돈이 부족합니다. 돈을 반환합니다.")
#                     else:
#                         profit += espresso.get_price()
#                         resources["물"] -= espresso.get_water()
#                         resources["우유"] -= espresso.get_milk()
#                         resources["커피"] -= espresso.get_coffee()
#                         print(f"여기 ${round(money - 1.50, 2)}의 잔돈이 있습니다.")
#                         print("여기 에스프레소가 나왔습니다. 맛있게 드세요!")
#
#         elif choice == "라떼":
#             pass
#
#         elif choice == "카푸치노":
#             pass
#
#
#
#     else:
#         print("잘 못 입력하셨습니다.")



#================================= 2차 시도( = main2 파일) ====================================

# end_of_coffee_machine = False
#
# while not end_of_coffee_machine:
#
#     choice = input("어떤 음료를 드시겠습니까? >>> (에스프레소/라떼/카푸치노)")
#
#     if choice == "off":
#         end_of_coffee_machine = True
#
#     elif choice == "report":
#         print_resources()
#
#     elif choice in ("에스프레소", "라떼", "카푸치노"):
#
#         if choice == "에스프레소":
#             drink = espresso
#         if choice == "라떼":
#             drink = latte
#         if choice == "카푸치노":
#             drink = capuccino
#
#         if resources["물"] < drink.get_water():
#             print("물 부족")
#         if resources["우유"] < drink.get_milk():
#             print("우유 부족")
#         if resources["커피"] < drink.get_coffee():
#             print("커피 부족")
#
#         if resources["물"]>=drink.get_water() and resources["우유"]>=drink.get_milk() and resources["커피"]>=drink.get_coffee():
#             quarter = int(input("지닌 쿼터 개수를 입력하세요"))
#             dime = int(input("지닌 다임 개수를 입력하세요"))
#             nickel = int(input("지닌 니켈 개수를 입력하세요"))
#             pennies = int(input("지닌 페니 개수를 입력하세요"))
#
#             money = quarter * 0.25 + dime * 0.10 + nickel * 0.05 + pennies * 0.01
#
#             if money < drink.get_price():
#                 print("돈이 부족합니다. 돈을 반환합니다.")
#             else:
#                 profit += drink.get_price()
#                 resources["물"] -= drink.get_water()
#                 resources["우유"] -= drink.get_milk()
#                 resources["커피"] -= drink.get_coffee()
#                 print(f"여기 ${round(money - drink.get_price(), 2)}의 잔돈이 있습니다.")
#                 print(f"여기 {choice}가 나왔습니다. 맛있게 드세요!")
#
#     else:
#         print("잘 못 입력하셨습니다.")



#=============================== 강의 따라가기 (pop_version2 에 있음)=========================

# choice가 "라떼"라는 str 데이터일 때, "라떼"를 만드는데 필요한 재료를 조회하는 방법은?
#  print(MENU["라떼"]["재료"])
#  print(MENU[choice]["재료"])          # 이렇게 하면 된다.


# 함수들 정의

def is_resources_enough(order_ingredients):
    """DocString(쌍따옴표 3개) : 함수/클래스/메서드가 어떤 작동을 하는지 '사람들에게' 설명해주는 기능.
    함수를 쓰고 마우스 커서를 올려놓으면 DocString 내 설명이 뜬다.
    주문 받은 음료를 resources 에서 재료 차감을 하고난 후, 음료 만들기가 가능하면
    True 반환, 아니면 False 반환
    : parameter : order_ingredients (주문 받은 것을 만드는 데에 필요한 재료)
    : return : True/False """
# is_resources_enough()

    # list를 반복문 돌리면 요소들이 튀어나왔고, dict를 반복문 돌리면 key들이 튀어나온다.
    # 밑은 order_ingredients가 dict 인것.
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:    #물은 물끼리 비교하려면 order_ingredients는 choice["재료"]까지 있어야 됨.
            print(f"죄송합니다. {item}이(가) 부족합니다.")
            return False

        # 아래 문구 대신 수업에서는 make_coffee()라는 함수를 만듦.
        # else:
        #    resources[item] -= order_ingredients[item]
        #    print(f"{choice} ☕ 가 나왔습니다. 맛있게 드세요!")

        return True                     # else 안 쓴 이유 : if 문이 실행 안 되었다면 어차피 True라서

def process_coins():
    """동전들을 입력받아 전체 금액을 반환하는 함수 call3() 유형"""
    # quarters = int(input("쿼터 동전을 몇개 넣을래? >>>")) * 0.25
    # dimes = int(input("다임 동전을 몇개 넣을래? >>>")) * 0.1
    # nickels = int(input("니켈 동전을 몇개 넣을래? >>>")) * 0.05
    # pennies = int(input("페니 동전을 몇개 넣을래? >>>")) * 0.01
    # return quarters + dimes + nickels + pennies

    # 이 안에서 위처럼 정의하면 지역변수임. 지역변수가 4개지요. 너무 많다면 축약버전으로 할 수 있다.
    # 아래는 축약버전

    total = 0.0
    total += int(input("쿼터 동전을 몇개 넣을래? >>>")) * 0.25
    total += int(input("다임 동전을 몇개 넣을래? >>>")) * 0.1
    total += int(input("니켈 동전을 몇개 넣을래? >>>")) * 0.05
    total += int(input("페니 동전을 몇개 넣을래? >>>")) * 0.01
    return total

# 그 다음은, 들어온 동전 금액과 가격을 비교하는 함수를 정의
def is_transaction_successful(money_received, drink_cost):
    """process_coins()의 결과값과 음료 가격을 매개변수로 받아
    동전이 가격보다 높으면 True / 아니면 False 반환
    그리고 True 면 profit에 음료 가격만큼 추가해줘야 함. """
    charge = money_received - drink_cost

    #if money_received > drink_cost:
    if charge >= 0:
        # resources["돈"] += drink_cost
        # profit이라는 전역변수가 따로 있었음.
        global profit
        profit += drink_cost

        print(f"${charge}가 반환되었습니다.")
        return True

    else:
        print(f"동전이 충분하지 않습니다. 금액 ${money_received}을 반환합니다.")
        return False

def make_coffee(drink_name, order_ingredients):
    """resources 에 있는 재료에서 MENU["음료이름"]["재료"]들을 차감함.
    -> 차감은 무조건 이루어집니다. 음료 나오는 안내 문구 작성 """
    for item in order_ingredients:          # for item in resources 가 아닌 이유는 에스프레소에서는 우유가 없어서 오류 발생하기 때문에
                                            # order_ingredients 를 기준으로 반복문을 돌림.
        resources[item] -= order_ingredients[item]
    print(f"{drink_name} ☕이 나왔습니다. 맛있게 드세요!")

logo = " << CAFE >> "

is_on = True
print(logo)
while is_on:
    choice = input("어떤 음료를 드시겠습니까? 에스프레소/라떼/카푸치노 >>>")
    # 만약에 choice가 off라면 반복문을 종료

    if choice == "off" :
        is_on = False
        print("자판기가 종료되었습니다.")

    elif choice == "report" :
        print(f"물 : {resources["물"]}ml")
        print(f"우유 : {resources["우유"]}ml")
        print(f"커피 : {resources["커피"]}g")
        print(f"돈 : ${profit}")

    # 에스프레소 / 라떼 / 카푸치노 중 하나를 입력했을 때 다음 단계로 넘어가는 부분
    elif choice in ["에스프레소", "라떼", "카푸치노"]:
        # print("정상 작동합니다.")
        # 자판기에 메뉴명을 정확히 입력했을 때의 처리과정
        # 1. 자원이 충분한지 확인해서 T/F
        # 2. T 라면 돈을 받아서 계산 -> 해당 금액의 가격보다 높은지 확인해서 T/F 반환
        # 3. T 라면 음료를 만들어주는데, resources dict에 있는 재료 수량을 감소시키고, profit을 음료 가격만큼 + 시키기
        drink = MENU[choice]
        if is_resources_enough(drink["재료"]):
            # 이상의 조건식이 T라면 2. 단계로 넘어가야 함.

            # 우선 돈을 받는다. process_coins()의 return 값을 새로운 변수에 저장시킴.
            money_paid = process_coins()

            # 받은 돈과 메뉴 가격을 비교해서 진행시키는 함수
            # if is_transaction_successful(money_paid, MENU[choice]["가격"])
            if is_transaction_successful(money_paid, drink["가격"]) :
            # print(is_transaction_successful(money_paid, drink["가격"]))         # True 값이 반환됨.
            # True 라는 말은 이 다음을 실행시키겠다는 말.

                # 이제 여기서 재료 차감하고 음료 만들어서 사용자에게 제공.
                make_coffee(choice, drink["재료"])


    else :
        print("잘 못 입력하셨습니다. 다시 입력하세요.")




