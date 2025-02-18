
def play_hangman2():
    from random import choice
    from hangman_arts import logo, stages
    from hangman_word_list import word_list

    chosen_word = choice(word_list)  # 외부파일명.변수명 : 외부파일에 있는 변수를 가져오겠다.

    length = int(len(chosen_word))
    display = []
    for i in range(length):  # for i in range(len(chosen_word) 로 해도 돌아간다.
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

