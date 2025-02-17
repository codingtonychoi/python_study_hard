'''
input() 함수의 결과값은 언제나 str 입니다. 즉 수학 연산을 위해서는 별도의 과정이
print(필요합니다)이때 필요한 함수가 '형변환 함수' 입니다. (conversion)
'''

# age1 = input("당신의 나이는 몇 살 입니까?")
# age1_int = int(age1)    # str인 age1을 int로 자료형 변환시켜서 age1_int라는 새로운 변수에 대입
#
# print(f"당신은 내년에 {age1_int+1}살이 됩니다.")


'''
자주 쓰이는 형변환 함수
1. int() : str 또는 float을 int로 변경
2. float() : str 또는  int를 float로 변경
3. round() : 
'''

# temp = int(3.8)     # 3이 됨. 소수점은 버림
# print(temp)
#
# temp2 = float(4)    # 4.0이 됨.
# print(temp2)
#
# temp3 = round(3.8)
# print(temp3)
#
# temp4 = round(5.3263, 2)    # 괄호 첫번째 수를 소수점 2째자리까지 표기. 반올림.
# print(temp4)

'''
BMI 계산기를 작성합니다.

1. 키(cm)을 입력받아 input() 변수 height에 저장.
2. 몸무게(kg)을 입력받아 변수 weight 에 저장.
3. 몸무게/키의제곱 을 계산하면 bmi 지수.
4. bmi 지수를 int로 출력하세요.
5. bmi 지수를 소수점 셋째자리에서 반올림하여 둘째자리까지 출력하세요.
'''
height = float(input("당신의 키는 몇 cm 입니까? >>> "))
weight = float(input("당신의 몸무게는 몇 kg 입니까? >>> "))

bmi = weight/(height/100)**2
bmi1 = int(bmi)
bmi2 = round(bmi, 2)

# print("당신의 bmi 지수는 " + str(bmi1) + "입니다.")
# print("당신의 bmi 지수는 " + str(bmi2) + "입니다.")

print(f"당신의 bmi 지수는 {bmi1}입니다.")
print(f"당신의 bmi 지수는 {bmi2}입니다.")


#####################선생님 답 1.##################################################################
# height = input("당신의 키는 몇 cm?")
# height = float(height)
# height = height/100                # 이미 flaot으로 바뀌었기 때문에 height로 입력해도 됨.
# weight = input("당신의 몸무게는 몇 kg?")
# weight = float(weight)
#
# bmi = weight/(height**2)
# print(bmi)
# bmi_int = int(bmi)              # 계산 후 결과값을 정수로 표현
# bmi_round = round(bmi,2)        # 계산 후 결과값을 소수점 셋째자리에서 반올림한 결과
# print(f"당신의 bmi 지수는 {bmi_int}입니다.")
# print(f"당신의 bmi 지수는 {bmi_round}입니다.")

#####################선생님 답 2.##################################################################
# height = float(input("당신의 키는 몇 cm 입니까?"))/100
# weight = float(input("당신의 몸무게는?"))
# print(f"당신의 bmi지수는 {int(weight/height**2)}입니다.")
# print(f"당신의 bmi지수는 {round((weight/height**2),2)}입니다.")


