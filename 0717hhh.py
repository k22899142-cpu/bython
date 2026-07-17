#챕터2 전체복습 0717hhh

##egg = input("계란은 몇 개?")
##print(egg,type(egg))

##egg = int(input("계란은 몇 개?"))
##print(egg,type(egg))

##attack = int(input("공격력은?"))
##scale = int(input("배율은?"))
##
##print(attack * scale)

##minute = input("분을 입력하세요: ")
##minute = int(minute)
##
##second = int(minute*60)
##
##text = (minute)+"분="+(second)+"초"
##print(text)

#1)
##name1 = input("닉네임을 입력하세요: ")
##print("환영합니다! "+name1+"님!")

#2)
##num1 = float(input("실수를 입력하세요: "))
##math1 = f"{num1*10:.3f}"
##print(math1)

#3)
##num1 = int(input("첫번째 숫자를 입력하세요: "))
##num2 = int(input("두번째 숫자를 입력하세요: "))
##num3 = int(input("세번째 숫자를 입력하세요: "))
##
##print("총합은 ", num1+num2+num3)

#4)
##rad1 = float(input("반지름을 입력하세요: "))
##area1 = float(rad1*rad1*3.14)
##length1 = f'{float(2*rad1*3.14):.1f}'
##
##res1 = "원의 넓이는 "+str(area1)+"원의 둘레는 "+str(length1)
##print(res1)

#5)
##upline = int(input("윗변을 입력하세요: "))
##lowline = int(input("밑변을 입력하세요: "))
##height = int(input("높이를 입력하세요: "))
##
##area = (upline+lowline)*height/2
##print(area)


##nut1 = '밤양갱'
##nut2 = '달디단 밤양갱'
##nut3 = """달디달고 달디달고,
##달디단 밤양갱 밤양갱
##내가 먹고 싶었던 건,
##달디단, 밤양갱, 밤양갱이야"""
##
##print(nut1, nut2, nut3)


##sweat = '달디'
##sweat2 = sweat * 10
##number = 255
##
##message = sweat2 + ' ' + '단 밤양갱' + int(number) + '개'
##print(message)

##line = "=" * 20
##header = "밤양갱 대박 세일!"
##footer = "놓치지 마세요!"
##message = line + "\n" + header + "\n" + line + "\n" + footer + "\n" + line
##print(message)
##
##ID = input("아이디: ")
##PW = input("비밀번호: ")
##print('당신의 아이디는 '+'"'+ID+'"'+'이며, 비밀번호는 '+'"'+PW+'"'+'입니다.')
##


##str1 = "파이썬 문자열을 골라보자"
##print(str1[0])
##print(str1[3])
##print(str1[5])
##print(str1[9])


##str2 = "이샘코딩학원"
##print(str2[1:3])
##print(str2[2:])
##print(str2[:2])
##print(str2[::2])
##print(str2[::-2])


##str3 = "스파이더맨친구"
##print(str3[1:6:2])


##word = "문자열과 인덱스"
##print(word[0])
##print(word[3])
##print(word[5])
##print(word[-1])

##snack = "떡볶이 순대 튀김"
##setmenu = snack[0] + snack[4] + snack[7]
##print(setmenu)
##
##word = "부분만 바꾸려고 하면 에러가 나요"
##print(word)
##
##
##word = "새로 만들어 덮어쓰기는 가능함"
##print(word)

##word = "슬라이싱으로 다양하게 문자를 잘라봅시다"
##
##print(word[1:4])
##print(word[::2])
##print(word[::-2])
##print(word[:12])
##print(word[1:5:2])
##print(word[10:])

##song = "록도닳 고르마 이산두백 과몰해동"
##reverse = song[::-1]
##print(reverse)
##
##song = "동해물과 백두산이 마르고 닳도록"
##part_song = song[:4]
##print(part_song)
##
##part_song = song[1:9:2]
##print(part_song)
##
##part_song = song[2::]
##print(part_song)


##str1 = input("문자열을 입력하시오: ")
##print(str1[1::2])

##########[1:6:2] -> 1부터 6바로 직전까지 2 간격으로
######[::2] -> 처음부터 2바로 직전까지
#########[2::] -> 2부터 끝까지
#######[0::2] -> 0부터 끝까지 2 간격으로

##pn = input("주민등록번호를 입력하세요: ")
##print(pn[2:6])

##code = "타파에벅서이썬스나짱만스"
##print(code[11],end = "")
##print(code[0],end = "")
##print(code[3],end = "")
##print(code[7],end = "")
##print(code[2],end = "")
##print(code[4],end = "")
##print(code[10],end = "")
##print(code[8])


#4)
##str1 = """동해물과 백두산이 마르고
##닳도록
##하느님이 보우하사
##우리나라 만세.
##무궁화 삼천리 화려 강산
##대한 사람, 대한으로
##길이 보전하세."""
##
####print(str1[33:35])
####print(str1[68:70])
##
##print(str1[0:48]+"강세"+str1[50::])
##


##poison = "이 문장에는 독이 있어!"
##print("독" in poison)

##number = '123478'
##print('1' in number)

##string = "문자열 함수 & 문자열 함수"
##print(string.find("자열"))
##print(string.find("함수"))
##print(string.rfind("자열"))
##print(string.rfind("함수"))

      
##string = "HelloPython"
##number = '123456'
##
##print(string.isalpha())
##print(string.isnumeric())
##print(number.isalpha())
##print(number.isnumeric())
##
##
##bab = "국밥 컵밥 초밥 김밥 비빔밥"
##print("가장 앞에 있는 밥은 "+(bab.find("밥"))+"번째!")      
##print("가장 뒤에 있는 밥은 "+(bab.rfind("밥"))+"번째!")

##eng = "FunnyPython"
##kor = "신나는파이썬"
##blank = 'B L A N K'
##
##print(eng.isalpha())
##print(kor.isalpha())
##print(blank.isalpha())


##num = '20240717'
##date = '2024.07.17'
##print(num.isnumeric())
##print(date.isnumeric())

#1)
##word = """강낭콩 옆 빈 콩깍지는 완두콩 깐 빈 콩깍지고 완두콩 옆 빈 콩깍지는 강낭콩 깐 빈 콩깍지다."""
##
##text1 = "첫번째 완두콩은 "+str(word.find("완두콩"))+"번째에 있습니다."
##text2 = "두번째 완두콩은 "+str(word.rfind("완두콩"))+"번째에 있습니다."
##print(text1)
##print(text2)
##
##
##str1 = "강낭콩 옆 빈 콩깍지는 완두콩 깐 빈 콩깍지고 완두콩 옆 빈 콩깍지는 강낭콩 깐 빈 콩각지다."
##
##print("첫번째 완두콩은 "+str(str1.find("완두콩"))+"번째에 있습니다.")
##print("두번째 완두콩은 "+str(str1.rfind("완두콩"))+"번째에 있습니다.")


#3)
##em = input("이메일을 입력해주세요: ")
##ID = em[0:6]
##print("이 이메일의 아이디는 "+ID+"입니다.")

####################str1 = "강낭콩 옆 빈 콩깍지는 완두콩 깐 빈 콩깍지고 완두콩 옆 빈 콩깍지는 강낭콩 깐 빈 콩각지다."
####################index1 = str1.find("완두콩")
####################str2 = str1[index1:index1+len("완두콩 깐 빈 콩깍지")]
####################print(str2)
####################
####################
####################index2 = (str1.rfind("강낭콩"))
####################str3 = str1[index2:index2+len("강낭콩 깐 빈 콩깍지")]
####################print(str3)


#split = 분열해주는 놈   replace= 바꿔주는 놈

##string = "문자열 함수는 참 다양해요"
##print(string.split("-"))
##
##print(string.replace("다양해요", "멋져요"))


##str1 = "Hello World!"
##print(str1.upper())
##print(str1.lower())

##dessert = "초코케이크 녹차마카롱 모카라떼"
##
##cake, macaron, coffee = dessert.split("")
##
##print(cake)
##print(macaron)
##print(coffee)


##n1,n2 = input("int 둘 입력: ").split()
##print(n1)
##print(n2)
##
##print(n1+n2)
##print(int(n1)+int(n2))

##a,b,c = input("알파벳 셋 입력 : ").split()
##print(c,b,a,sep = ">")

##r1,r2 = input("float 둘 입력: ").split()
##r1 = float(r1)
##r2 = float(r2)
##
##print(r1*r2)

##message = "abc 1234 ..$%%#%#!!!"
##trans = message.upper()
##
##print(trans)


##str1 = "이 문장안에 있는 글자수는 몇개일까요?"
##print(len(str1))

##
##str1 = "파이썬 {0}번 복습하기".format(10)
##print(str1)
##
##str2 = f"문자열도 {10:8.2f}번 복습하기"
##print(str2)

##num = 345345
##print(len(num))

##year = input("태어난 해: ")
##month = input("태어난 월: ")
##day = input("태어난 일: ")
##date = "{}년 {}월 {}일".format(year,month,day)
##print("당신의 생일은 "+date+"입니다!")
##

num1 = f"{10}/{20}"
num2 = f"[{10.10}/{20.20}]"
print(num1)
print(num2)

pi = 3.14
num3 = f'[{pi:4.1f}/{pi:010.0f}]'
print(num3)

str1 = 'python'
str2 = f'[{str1:10s}/{str1:010s}]'
print(str2)

