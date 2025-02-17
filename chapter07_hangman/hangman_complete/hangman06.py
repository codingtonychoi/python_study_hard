import random
import hangman_arts                 # 외부 파일을 가져온다.
import hangman_word_list

chosen_word = random.choice(hangman_word_list.word_list)     # 외부파일명.변수명 : 외부파일에 있는 변수를 가져오겠다.

length = int(len(chosen_word))
display = []
for i in range(length):             # for i in range(len(chosen_word) 로 해도 돌아간다.
    display.append("_")


end_of_game = False
lives = 6
print(hangman_arts.logo)

while not end_of_game:
    # while "_" in display:
    guess = input("알파벳을 하나 추측해서 입력하세요 >>> ").lower()

    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
                display[i] = guess
    if lives == 6:
            pass
    else:
        print(hangman_arts.stages[lives])
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
        print(hangman_arts.stages[lives])
        print(f"당신의 기회는 {lives}번 남았습니다.")
        if lives == 0:
            print(f"모든 기회를 잃었습니다. 정답은 {chosen_word} 입니다.")
            end_of_game = True


    if "_" not in display:
        print(" ".join(display))
        print("/".join(display))
        print("정답입니다!!")
        end_of_game = True

