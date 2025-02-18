import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

#todo -1 : 남은 목숨 수를 추적하기 위한 'lives'라는 변수를 선언하고 6으로 초기화하세요.
#todo -2 : 추측한 알파벳이 chosen_word에 없으면 lives를 1 감소시키세요.
# lives가 0이 되면 "모든 기회를 잃었습니다."를 출력하고 게임을 끝내세요.

#todo -3 : display list의 모든 요소를 결합하여 문자열로 변환하세요.
#todo -4 : 사용자가 모든 문자를 맞췄는지 확인하세요 -> 정답을 맞췄다면 "정답입니다!!"를 출력하세요.

word_list = ["apple", "banana", "camel"]
chosen_word = random.choice(word_list)

length = int(len(chosen_word))
display = []
for i in range(length):             # for i in range(len(chosen_word) 로 해도 돌아간다.
    display.append("_")


end_of_game = False
lives = 6

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
            # else:                         # 여기에 넣으면 안되는게 for문은 단어 내 문자하나하나 비교하는데 else는 단어전체에 없을 때 실행되어야 하는 실행문.
            #     lives -= 1
            #     print(f"당신의 기회는 {lives}번 남았습니다.")
            #     if lives == 0:
            #         print("모든 기회를 잃었습니다.")
            #         end_of_game = True
            #         print(f"정답은 {chose_word} 입니다.")
    if guess not in chosen_word:                         # 여기에 넣으면 안되는게 for문은 단어 내 문자하나하나 비교하는데 else는 단어전체에 없을 때 실행되어야 하는 실행문.
        lives -= 1
        print(stages[lives])
        print(f"당신의 기회는 {lives}번 남았습니다.")
        if lives == 0:
            print(f"모든 기회를 잃었습니다. 정답은 {chosen_word} 입니다.")
            end_of_game = True


    if "_" not in display:
        print(" ".join(display))
        print("정답입니다!!")
        end_of_game = True


# 여기까지 작성했을 때 비어있는 점.
# 1. 로고
# 2. word_list가 부족하다.
# 3. 혹시 테스트 해보고 유지보수 및 리팩토링 지점이 있는지 확인할 필요가 있음.(함수화)



