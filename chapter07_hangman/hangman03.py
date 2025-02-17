import random                       # 특정 모듈을 사용하는 것을 맨 처음에 명시합니다.

'''
"".join(반복가능객체) method : . 앞에 있는 문자열을 기준으로 반복가능객체의 요소들을 합쳐서 str으로 반환함.

for 변수명 in 반복가능객체
'''
#
# temp = ["안", "녕", "하", "세", "요"]
# hello = "".join(temp)
# print(hello)
# print("/".join(temp))
# print(" ".join(temp))

word_list = ["apple", "banana", "camel"]
chosen_word = random.choice(word_list)

length = int(len(chosen_word))
display = []
for i in range(length):             # for i in range(len(chosen_word) 로 해도 돌아간다.
    display.append("_")
print("".join(display))

#todo -1 : "_"가 적용된 display를 구현하세요.
#todo -2 : 사용자가 추측을 반복할 수 있도록 while 반복문을 작성하세요.
# 즉, display에 더이상 "_"가 없을 때 반복문이 멈추도록 작성합니다.
# 반복문 종료 후 print("정답입니다!!")를 출력하도록 작성하시오.

for i in range(10):
    while "_" in display:
        guess = input("알파벳을 하나 추측해서 입력하세요 >>> ").lower()
        for i in range(len(chosen_word)):
            if guess == chosen_word[i]:
                display[i] = guess
                # else 는 안써도 됨. 틀렸을 때의 지시사항이 없기 때문.
        print("".join(display))

    if "_" not in display:
        print("정답입니다!!")
        break


#======== 선생님 답 =========


while "_" in display :
    guess = input("알파벳을 하나 추측해서 입력하세요 >>> ").lower()

    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = guess
    print(display)

print(" ".join(display))
print("정답입니다!!")