# 변수명이 너무 긴 것들을 좀 줄여보자.

#import random
from random import choice

#import hangman_arts                 # 외부 파일을 가져온다.
#import hangman_word_list
from hangman_arts import logo, stages
from hangman_word_list import word_list

'''
import 문 학습:
    import문을 단독으로만 쓸 경우에는 모듈명.변수명 혹은 모듈명.메서드명()을 명시해야함.
    모듈명.변수명의 예시 : hangman_arts.logo
    모듈명.메서드명()의 예시 : random.choice()

import문의 응용
    from - import 문을 쓰게 될 경우에 모듈명을 생략할 수 있음
    from - import의 경우
    from a import *로 작성할 경우 : a 모듈 내에 있는 모든 변수를 참조하겠다는 의미
    
    *(asterisk) : all의 의미.
    다만, 너무 많은 부분을 from - import 구문으로 작성했을 때 
    특정변수가 해당 파일에서 자체적으로 생성됐는지,
    혹은 다른 어떤 파일들에서 참조되었는지를 가시적으로 확인할 수 없다는 점 때문에
    제한적으로 사용됨.
    
    from a import a, b, c 의 경우는 그나마 낫지만
    * 개념과 합쳐졌을 때는 가독성이 매우 떨어진다는 단점.
    
    마찬가지로, from random import choice의 경우에도 해당 메서드 하나만 참조했기 때문에
    별 문제 없지만
    from random import * 로 작성했을 경우
    choice 가 자체적으로 정의된 메서드인지 혹은 다른데서 가지고 온 변수인지 메서드인지
    기타 등등의 가독성 문제가 야기될 수 있음.
    
'''


chosen_word = choice(word_list)     # 외부파일명.변수명 : 외부파일에 있는 변수를 가져오겠다.

length = int(len(chosen_word))
display = []
for i in range(length):             # for i in range(len(chosen_word) 로 해도 돌아간다.
    display.append("_")


end_of_game = False
lives = 6
print(logo)

while not end_of_game:
    # while "_" in display:
    guess = input("알파벳을 하나 추측해서 입력하세요 >>> ").lower()

    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
                display[i] = guess
    if lives == 6:
            pass
    else:
        print(stages[lives])
    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(stages[lives])
        print(f"당신의 기회는 {lives}번 남았습니다.")
        if lives == 0:
            print(f"모든 기회를 잃었습니다. 정답은 {chosen_word} 입니다.")
            end_of_game = True


    if "_" not in display:
        print(" ".join(display))
        print("/".join(display))
        print("정답입니다!!")
        end_of_game = True