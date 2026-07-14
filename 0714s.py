##print("김범서0714")
##str1 = "파이썬, C언어, HTML/CSS, JAVA"
##logic1 = "파이썬" in str1
##print(logic1)
##
##logic2 = "C#" in str1
##print(logic2)

##poison = "이 파이썬 문장에는 독이 있어!"
##print("독" in poison)
##print("약" not in poison)

##number = 12345678
##print(1 in number)
#이러면 안돼요 12345678이 숫자지만 문자취급됩니다 따옴표 붙여야해요 + print안에도 숫자지만 따옴표 붙여야 함

##number = '12345678'
##print('1' in number)

##message = '다른 연산자끼리 섞어쓰는 것도 가능해.'
##print("연산자" in message[2:10])
##print("연산자" not in "정말 다양한 방법으로" + "연산자를 쓸 수 있어")
##print("연산자" not in "정말 다양한 방법으로")
##print("연산자" in "정말 다양한 방법으로")

##print("\\\\\\\\")

##string = "문자열 함수 & 문열 함수"
##print(string.find("자열"))
##print(string.find("함수"))
##print(string.find("자열"))
##print(string.find("함수"))

####string = "HelloPython"
####number = "123456"
####print(string.isalpha())
####print(string.isnumeric())
####print(string.isalpha())
####print(string.isnumeric())


##bab = "국밥 컵밥 초밥 김밥 비빔밥"
##print("가장 앞에 있는 밥은 "+str(bab.find("밥"))+"번째!")
##
##print("가장 앞에 있는 밥은 "+str(bab.rfind("밥"))+"번째!")
##
##
##eng = "FFFFFunnyPython"
##
##kor = "파이썬크림치즈빵"
##
##blank = "B L A N K"
##
##blank1 = "BLANK"
##
##print(eng.isalpha())
##print(kor.isalpha())
##print(blank.isalpha())
##print(blank1.isalpha())

##num = "20240505"
##data = "2024.05.05"
##
##print(num.isnumeric())
##print(data.isnumeric())

#문제1

##str1 = "강낭콩 옆 빈 콩깍지는 완두콩 깐 빈 콩깍지고 완두콩 옆 빈 콩깍지는 강낭콩 깐 빈 콩각지다."
##
##print("첫번째 완두콩은 "+str(str1.find("완두콩"))+"번째에 있습니다.")
##print("두번째 완두콩은 "+str(str1.rfind("완두콩"))+"번째에 있습니다.")



#문제2

####str_ori = "강낭콩 옆 빈 콩깍지는 완두콩 깐 빈 콩깍지고 완두콩 옆 빈 콩깍지는 강낭콩 깐 빈 콩각지다."
####index1 = str_ori.find("완두콩")
####string1 = str_ori[index1:index1+len("완두콩 깐 빈 콩깍지")]
####print(string1)

##str_ori = "강낭콩 옆 빈 콩깍지는 완두콩 깐 빈 콩깍지고 완두콩 옆 빈 콩깍지는 강낭콩 깐 빈 콩각지다."
##index1 = str_ori.find("완두콩")
##string1 = str_ori[index1:index1+11]
##print(string1)
##
##
##index2 = (str_ori.rfind("강낭콩"))
##string2 = str_ori[index2:index2+len("강낭콩 깐 빈 콩깍지")]
##print(string2)

#문제3
##mail1 = input("이메일을 입력해주세요: ")
##
##name1 = (mail1[0:6])
##
##print("이 이메일의 아이디는", name1+"입니다.")


##string = "문자열_함수는_참_다양해요"
##split_string = string.split("_")
##print(split_string)
##
##
##string = string.replace("다양해", "멋져")
##print(string)
##
##
##string = "인간은_누구나_죽는다."
##split_string = string.split("_")
##print(split_string)
##
##
##string = string.replace("죽는", "살아간")
##print(string)

##word1 = "You've got a friend in me, you've got a freind in me."
##print(word1.upper())
##
##word2 = "YOU'VE GOT A FRIEND IN ME, YOU'VE GOT A FREIND IN ME."
##print(word2.lower())
##

##dessert = "초코케이크 녹차마카롱 모카라떼"
##
##cake, macaron, coffee = dessert.split(" ")
##print("[ 오늘 먹을 간식 목록 ]")
##print("케이크 :", cake)
##print("마카롱 :", macaron)
##print("커피 :", coffee)


##n1,n2 = input("int 둘 입력 : ").split()
##print(n1)
##print(n2)
##
##print(n1+n2)
##print(int(n1)+int(n2))
##
##a, b, c = input("알파벳 셋 입력 : ").split()
##print(c,b,a,sep=">")


r1,r2 = input("float 둘 입력 : ")
r1 = float(r1)
r2 = float(r2)
print(r1*r2)












