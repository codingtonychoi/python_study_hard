'''
외부 패키지의 설치

좌측 상단 메뉴버튼(햄버거) -> file -> settings(설정: ctrl + alt + s)
좌측 리스트에서 project : 프로젝트명으로 되어있는 부분 클릭
-> python interpreter
-> 좌측 상단에 + 눌러서 필요한 패키지 검색 및 설치
-> prettytable 검색 해서 Luke 꺼 install
'''

from prettytable import PrettyTable
from pokemon_data import pokemon_data

# print(pokemon_data[0])
# print(pokemon_data[0][1])

table = PrettyTable()
table.field_names = ["번호", "이름", "타입"]
for i in range(len(pokemon_data)):
    #table.add_row([pokemon_data[i][0], pokemon_data[i][1], pokemon_data[i][2]])
    table.add_row(pokemon_data[i])                      # pokemon_data의 0번지가 tuple이라서 이렇게 넣어도 다 나온다.
                                                        # 외부 데이터의 자료형이 너무나도 중요하다.
print(table)






