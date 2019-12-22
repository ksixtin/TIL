# 메뉴를 입력하면 기입력된 5개 메뉴중 한가지가 출력됨
import random

a = input()

menus = ["순대국밥", "김치찌개", "순두부찌개", "된장찌개", "자장면"]
choiceList = random.choice(menus)
restrt = ["학식", "GS타워", "맥도날드", "김밥천국", "홍콩반점"]
resList = random.choice(restrt)


if  a == "메뉴":
    print(choiceList)
elif a == "식당":
    print(resList)
else:
    print("원하는 요청사항을 입력하세요")
    input()

# 문제점 : 여기서 다시 인풋을 한 결괏값이 메뉴와 식당을 불러오게끔 하는 방법을 모름