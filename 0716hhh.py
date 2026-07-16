#split, replace, upper, lower

##dessert = "초코케이크 녹차마카롱"
##cake, macaron, coffee = dessert.split(" ")
##
##print("[오늘 먹은 간식 목록]")
##print("케이크 : ", cake)
##print("마카롱 : ", macaron)
##print("커피 : ", coffee)

##a, b, c = input("셋 입력: ").split()
##print(c,b,a,sep = '<')

##r1, r2 = input("float 둘 입력: ").split()
##
##r1 = float(r1)
##r2 = float(r2)
##print(r1*r2)

##store1 = """ 이 자판기 안에는 포도맛 사이다, 포도맛 주스, 포도맛 슬러쉬가 있습니다"""
##taste = input("무슨 맛 자판기로 바꿀까요?")
##print(store1.replace("포도", taste))


##num1 = input("전화번호 입력: ").split('-')
##print(num1[0])
##print(num1[1])
##print(num1[2])


year = input("태어난 해를 입력해: ")
month = input("태어난 월을 입력해 : ")
day = input("태어난 일을 입력해 : ")
date = "{}년 {}월 {}일".format(year, month, day)

print("당신의 생일은 "+date+"입니다. 축하해요!")







