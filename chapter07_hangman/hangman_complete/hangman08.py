
# 함수를 정의해보자
def play_hangman():

    # 사용되는 클래스/모듈을 명시
    import random

    # 해당 프로그램에서 사용될 변수들의 목록
    logo = '''
    ██   ██  █████  ███    ██  ██████  ███    ███  █████  ███    ██ 
    ██   ██ ██   ██ ████   ██ ██       ████  ████ ██   ██ ████   ██ 
    ███████ ███████ ██ ██  ██ ██   ███ ██ ████ ██ ███████ ██ ██  ██ 
    ██   ██ ██   ██ ██  ██ ██ ██    ██ ██  ██  ██ ██   ██ ██  ██ ██ 
    ██   ██ ██   ██ ██   ████  ██████  ██      ██ ██   ██ ██   ████                                                     
    '''

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


    word_list = [
    'abruptly',
    'absurd',
    'abyss',
    'affix',
    'askew',
    'avenue',
    'awkward',
    'axiom',
    'azure',
    'bagpipes',
    'bandwagon',
    'banjo',
    'bayou',
    'beekeeper',
    'bikini',
    'blitz',
    'blizzard',
    'boggle',
    'bookworm',
    'boxcar',
    'boxful',
    'buckaroo',
    'buffalo',
    'buffoon',
    'buxom',
    'buzzard',
    'buzzing',
    'buzzwords',
    'caliph',
    'cobweb',
    'cockiness',
    'croquet',
    'crypt',
    'curacao',
    'cycle',
    'daiquiri',
    'dirndl',
    'disavow',
    'dizzying',
    'duplex',
    'dwarves',
    'embezzle',
    'equip',
    'espionage',
    'euouae',
    'exodus',
    'faking',
    'fishhook',
    'fixable',
    'fjord',
    'flapjack',
    'flopping',
    'fluffiness',
    'flyby',
    'foxglove',
    'frazzled',
    'frizzled',
    'fuchsia',
    'funny',
    'gabby',
    'galaxy',
    'galvanize',
    'gazebo',
    'giaour',
    'gizmo',
    'glowworm',
    'glyph',
    'gnarly',
    'gnostic',
    'gossip',
    'grogginess',
    'haiku',
    'haphazard',
    'hyphen',
    'iatrogenic',
    'icebox',
    'injury',
    'ivory',
    'ivy',
    'jackpot',
    'jaundice',
    'jawbreaker',
    'jaywalk',
    'jazziest',
    'jazzy',
    'jelly',
    'jigsaw',
    'jinx',
    'jiujitsu',
    'jockey',
    'jogging',
    'joking',
    'jovial',
    'joyful',
    'juicy',
    'jukebox',
    'jumbo',
    'kayak',
    'kazoo',
    'keyhole',
    'khaki',
    'kilobyte',
    'kiosk',
    'kitsch',
    'kiwifruit',
    'klutz',
    'knapsack',
    'larynx',
    'lengths',
    'lucky',
    'luxury',
    'lymph',
    'marquis',
    'matrix',
    'megahertz',
    'microwave',
    'mnemonic',
    'mystify',
    'naphtha',
    'nightclub',
    'nowadays',
    'numbskull',
    'nymph',
    'onyx',
    'ovary',
    'oxidize',
    'oxygen',
    'pajama',
    'peekaboo',
    'phlegm',
    'pixel',
    'pizazz',
    'pneumonia',
    'polka',
    'pshaw',
    'psyche',
    'puppy',
    'puzzling',
    'quartz',
    'queue',
    'quips',
    'quixotic',
    'quiz',
    'quizzes',
    'quorum',
    'razzmatazz',
    'rhubarb',
    'rhythm',
    'rickshaw',
    'schnapps',
    'scratch',
    'shiv',
    'snazzy',
    'sphinx',
    'spritz',
    'squawk',
    'staff',
    'strength',
    'strengths',
    'stretch',
    'stronghold',
    'stymied',
    'subway',
    'swivel',
    'syndrome',
    'thriftless',
    'thumbscrew',
    'topaz',
    'transcript',
    'transgress',
    'transplant',
    'triphthong',
    'twelfth',
    'twelfths',
    'unknown',
    'unworthy',
    'unzip',
    'uptown',
    'vaporize',
    'vixen',
    'vodka',
    'voodoo',
    'vortex',
    'voyeurism',
    'walkway',
    'waltz',
    'wave',
    'wavy',
    'waxy',
    'wellspring',
    'wheezy',
    'whiskey',
    'whizzing',
    'whomever',
    'wimpy',
    'witchcraft',
    'wizard',
    'woozy',
    'wristwatch',
    'wyvern',
    'xylophone',
    'yachtsman',
    'yippee',
    'yoked',
    'youthful',
    'yummy',
    'zephyr',
    'zigzag',
    'zigzagging',
    'zilch',
    'zipper',
    'zodiac',
    'zombie',
    ]

    chosen_word = random.choice(word_list)

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
