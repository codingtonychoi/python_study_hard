import random

word_list =  ["apple", "banana", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)

#todo -1 : 비어있는 list인 display를 만드시오.
# chosen_word의 각 문자 개수마다 "_"을 추가하시오. 예를 들어 chosen_word == "apple"이라면,
# display = ["_","_","_","_","_"]이 되어야 합니다. 즉, chosen_word의 문자 개수만큼
# "_"가 생깁니다.

length = int(len(chosen_word))
display = []
for i in range(length):             # for i in range(len(chosen_word) 로 해도 돌아간다.
    display.append("_")
print(display)

# 향상된 for 문 사용
# for letter in chosen_word:
#     display.append("_")
# print(display)


#todo -2 : chosen_word의 각 문자들을 반복시키세요.
# 만약 그 위치의 문자가 guess와 일치하면, 해당 위치의 display에서 해당 문자를 공개하세요.
# ex) 사용자가 "p"를 입력했고, chosen_word가 "apple"이라면 display = ['_','p','p','_','_']로
# 바뀌어야 합니다.

# 힌트 :
# list의 각 요소를 재대입하는 방법
# numbers = [1,2,3,4,5]
# print(numbers)
# numbers[0] = 100
# print(numbers)

for i in range(5):
    guess = input("알파벳을 하나 추측해서 입력하세요 >>> ").lower()
    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = guess
                                                # else 는 안써도 됨. 틀렸을 때의 지시사항이 없기 때문.
    print(display)














