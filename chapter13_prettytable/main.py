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
for i in range(len(pokemon_data)):                      # len는 26, 0~25번지까지 있다.
    #table.add_row([pokemon_data[i][0], pokemon_data[i][1], pokemon_data[i][2]])
    table.add_row(pokemon_data[i])                      # pokemon_data의 0번지가 tuple이라서 이렇게 넣어도 다 나온다.
                                                        # 외부 데이터의 자료형이 너무나도 중요하다.
#print(table)

# 데이터를 그대로 집어넣는 것을 하드코딩이라고 함.
# 하드코딩을 하는 것이 더 범용성 있는 코드를 짜는 방법.


# 향상된 for문
#for table in tables:
for pokemon in pokemon_data:                            # 변수명은 아무거나 해도 되는듯.
    table.add_row(pokemon)
print(table)




