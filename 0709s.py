##name1  = str(input("이름을 입력하세요: "))
##print(name1+"님 환영합니다!")

##str1 = 'Helllo string!'
##str2 = "안녕 문자열!"
##str3 = """안녕 변수!
##안녕 문자열!
##안녕 파이썬!"""


##str1 = 'Hello string!'
##str1[0] = 'D'

##str1 = '안녕 문자열'

##str1 = "파이썬"
##str2 = "참 쉽다"
##str3 = str1 + ", " + str2 + "!!"
##print(str3)

##str1 = "강해린! "
##str2 = str1 * 123
##
##print(str2)

##str1 = """안녕하세요
##제 이름은 김범서이고
##저는 유니스트 경영과학부 26학번 입니다
##그렇습니다"""
##
##print(str1)

##sweet = '달디'
##sweet2 = sweet * 10
##number = 225
##message = sweet2 + ' ' + '단 밤양갱 '+  str(number) + '개'
##print(message)

##
##sweet = '달디'
##sweet2 = sweet * 10
##number = 225
##message = sweet2 + ' ' + '단 밤양갱 '+  'number' + '개'
##print(message)

##line = "=" * 20
##header = "밤양갱 대박 세일!"
##footer = "놓치지 마세요!"
##message = line + "\n" + header + "\n" + line + "\n" + footer + "\n" + line
##
##print(message)


##문제1

##ID = input('아이디: ')
##PW = input('비밀번호: ')
##
####print("당신의 아이디는", "'"+ ID +"'" , "이며, 비밀번호는",PW, "입니다.")
####print("당신의 아이디는 '", ID, "' 이며, 비밀번호는",PW, "입니다.", sep="")
##
##print('당신의 아이디는', '"'+ID+'"'+ '이며, 비밀번호는', '"'+PW+'"'+ '입니다.')
##



##str1 = "파이썬 문자열을 골라보자"
##
##print(str1[0])
##print(str1[4])
##print(str1[9])
##print(str1[2])
##print(str1[6])
##print(str1[12])

##str2 = "이샘코딩학원"
##print(str2[1:3])
##print(str2[2:])
##print(str2[:2])
##print(str2[::2])
##print(str2[::-2])


##str2 = "아버지가방에들어가신다"
##print(str2[1:3])
##print(str2[2:])
##print(str2[:2])
##print(str2[::2])
##print(str2[::-2])

##word = "문자열과 인덱스"
##print(word[0])
##print(word[3])
##print(word[5])
##print(word[-1])

##snack = "떡볶이 순대 튀김"
##
##setmenu = snack[0] + snack[4] + snack[7]
##print(setmenu)


##word = "부분만 바꾸려고 하면 에러가 나요"
##print(word)

##word[0] = "수" #에러나면 주석 처리해서 다시
##word = "새로 만들어 덮어쓰기는 가능"
##print(word)
####
##word = "슬라이싱으로 다양하게 문자를 잘라봅시다"
##print(word[0:4])
##print(word[7:9])
##print(word[5:])
##print(word[:12])
##print(word[::3])
##print(word[::-3])


##song = "록도닳 고루마 이산두백 과물해동"
##reverse = song[::-1]
##print(reverse)


##song = "동해물과 백두산이 마르고 닳도록"
##part_song = song[:4]
##print(part_song)
##
##part_song = song[5:13]
##print(part_song)
##
##part_song = song[14:]
##print(part_song)


###문제1
##
##str1 = input("문자열을 입력하세요 : ")
##even = str1[1::2]
##
##print(even)
##
##
###문제2
##numb1 = input("주민번호를 입력하세요: ")
##birth = numb1[2:6]
##print(birth)
##
##
###문제3
##code1 = "타파에벅서이썬스나짱만스"
##print(code1[11], end = "")
##print(code1[0],end = "")
##print(code1[3],end = "")
##print(code1[7],end = "")
##print(code1[2],end = "")
##print(code1[4],end = "")
##print(code1[10],end = "")
##print(code1[8])
##
##
##
###문제4-1
##lovecountrysong = """동해물과 백두산이 마르고
##닳도록
##하느님이 보우하사 우리 나라만세.
##무궁화 삼천리 화려 강산
##대한 사람, 대한으로
##길이 보전하세."""
##
##
##print(lovecountrysong[33:35])
##print(lovecountrysong[68:])


####문제4-1
##lovecountrysong = """동해물과 백두산이 마르고
##닳도록
##하느님이 보우하사 우리 나라만세.
##무궁화 삼천리 화려 강산
##대한 사람, 대한으로
##길이 보전하세."""
##
##강산 = lovecountrysong[48:50]
##print(lovecountrysong[0:48]+'강세'+lovecountrysong[50:])
##


##str1 = "파이썬, C언어, HTML/CSS, JAVA"
##logic1 = "파이썬" in str1
##
##print(logic1)
##
##logic2 = "C#" in str1
##print(logic2)

##poison = "이 파이썬 문장에는 독이 있어!"
##print("독" in poison)
##print("약" not in poison)

##number = '12345678'
##print('1' in number)


##
##message = "다른 연산자들끼리 섞어쓰는 것도 가능해."
##print("연산자" in message[2:10])
##print("연산자" not in "정말 다양한 방법으로" + "연산자를 쓸 수 있어")
##print("연산자" in "정말 다양한 방법으로" + "연산자를 쓸 수 있어")
