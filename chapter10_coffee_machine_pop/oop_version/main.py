from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
# from 파일명(소문자 시작) import 클래스명(대문자 시작)

# 외부 파일에서 import 해온 class 들의 객체 생성
menu = Menu()                       # menu 객체를 만들었더니 MenuItem에 해당하는 객체(latte, espresso, capuccino가 또 생성되었다.
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

# 반복
is_on = True
while is_on :
    choice = input(f"음료를 선택하세요. {menu.get_items()} >>> ").lower()
    # todo -1 : choice가 -> off / report / 오타났을 때 작성하는 부분을 완성하시오.
    if choice == "off":
        is_on = False
        print("자판기가 종료되었습니다.")
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else :
        #menu.find_drink(choice)
        drink = menu.find_drink(choice)     # 음료 객체를 변수명 drink에 저장
        if drink == None :                  # choice에 오타가 있을 경우 None이 반환되기 때문에 이렇게 작성.
            continue                        # continue가 실행되면 이 밑의 코드라인은 실행되지 않고,
                                            # while 반복문의 맨 앞으로 돌아감.
        else :
            # if choice == str(menu(name)):
            #     coffee_maker.is_resource_sufficient(menu(name))
            #     money_machine.make_payment(menu(cost))
            if coffee_maker.is_resource_sufficient(drink):
                #.is_resource_sufficient()의 return이 T/F니까 if문 써라는 거임.
                #.is_resource_sufficient() 메서드를 확인해보면,
                    # drink.ingredients를 반복문 돌린다는 것을 확인할 수 있습니다.
                    # 이제 여러분이 주의해서 봐야할 점은 미리 작성된 메서드가 어떤 자료형의 argument를 요구하고 있는지 입니다.
                    # 즉, pop version 에서처럼 동일하게 생각해서 drink.ingredients를 argument로 넣었다면
                    # 오류가 발생했을 겁니다. -> 미리 작성된 코드 부분을 확인해야겠죠. 그리고 return 타입도.
                if money_machine.make_payment(drink.cost):
                    # 이상의 조건식을 통과했다면 돈이 충분한 거니까, 커피를 만들면 되겠지요.
                    coffee_maker.make_coffee(drink)






