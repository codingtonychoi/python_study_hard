
def coffee_machine():

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

    profit = 0

    resources = {
            "물": 300,
            "우유": 200,
            "커피": 100,
        }
    espresso = Drink(1.5, 50, 0, 18)
    latte = Drink(2.5, 200, 150, 24)
    capuccino = Drink(3.0, 250, 100, 24)

    def print_resources():
        print(f"물: {resources["물"]}ml\n우유: {resources["우유"]}ml\n커피: {resources["커피"]}g\n돈: ${profit}")


    end_of_coffee_machine = False

    while not end_of_coffee_machine:

        choice = input("어떤 음료를 드시겠습니까? >>> (에스프레소/라떼/카푸치노)")

        if choice == "off":
            end_of_coffee_machine = True

        elif choice == "report":
            print_resources()

        elif choice in ("에스프레소", "라떼", "카푸치노"):

            if choice == "에스프레소":
                drink = espresso
            if choice == "라떼":
                drink = latte
            if choice == "카푸치노":
                drink = capuccino

            if resources["물"] < drink.get_water():
                print("물 부족")
            if resources["우유"] < drink.get_milk():
                print("우유 부족")
            if resources["커피"] < drink.get_coffee():
                print("커피 부족")

            if resources["물"]>=drink.get_water() and resources["우유"]>=drink.get_milk() and resources["커피"]>=drink.get_coffee():
                quarter = int(input("지닌 쿼터 개수를 입력하세요"))
                dime = int(input("지닌 다임 개수를 입력하세요"))
                nickel = int(input("지닌 니켈 개수를 입력하세요"))
                pennies = int(input("지닌 페니 개수를 입력하세요"))

                money = quarter * 0.25 + dime * 0.10 + nickel * 0.05 + pennies * 0.01

                if money < drink.get_price():
                    print("돈이 부족합니다. 돈을 반환합니다.")
                else:
                    profit += drink.get_price()
                    resources["물"] -= drink.get_water()
                    resources["우유"] -= drink.get_milk()
                    resources["커피"] -= drink.get_coffee()
                    print(f"여기 ${round(money - drink.get_price(), 2)}의 잔돈이 있습니다.")
                    print(f"여기 {choice}가 나왔습니다. 맛있게 드세요!")

        else:
            print("잘 못 입력하셨습니다.")


coffee_machine()