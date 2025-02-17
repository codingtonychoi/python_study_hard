height = float(input("당신의 키는 몇 cm 입니까? >>> "))
weight = float(input("당신의 몸무게는 몇 kg 입니까? >>> "))

bmi = weight/(height/100)**2                # 반복적으로 나오게 되는 연산의 경우, 간단한 변수명에 대입하는 것이
bmi1 = int(bmi)                             # 가독성 높은 코드를 작성하는 방식에 해당함.
bmi2 = round(bmi, 2)

# print("당신의 bmi 지수는 " + str(bmi1) + "입니다.")
# print("당신의 bmi 지수는 " + str(bmi2) + "입니다.")

#print(f"당신의 bmi 지수는 {bmi1}입니다.")
print(f"당신의 bmi 지수는 {bmi2}입니다.")

'''
업그레이드 관련 지시 사항

1. chrome에서 사이트를 확인하신 후 bmi가 특정 구간일 때마다
당신의 bmi 지수는 xx.xx이고, 저체중/정상/과체중/비만입니다. 가 출력될 수 있도록
조건문을 작성하여 반영하시오.

'''

if bmi2 < 18.50:
    print("당신은 저체중.")
elif bmi2 < 23.00:
    print("당신은 정상!")
elif bmi2 < 25.00:
    print("당신은 과체중.")
elif bmi2 < 30.00:
    print("당신은 비만!")
else:
    print("당신은 고도비만!!!")
