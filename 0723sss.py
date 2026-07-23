##num1 = int(input("첫 번째 숫자 입력: "))
##num2 = int(input("두 번째 숫자 입력: "))
##num3 = int(input("세 번째 숫자 입력: "))
##
##print(f"10000 += num1: {10000 + num1}")
##print(f"10000 -= num2: {10000 - num2}")
##print(f"10000 *= num3: {10000 * num3}")
##
##txt = input("문자열 입력: ")
##num = input("숫자 입력: ")
##
##txt2 = txt
##txt += num
##txt2 *= int(num)
##
##print(txt)
##print(txt2)

##num1 = input("숫자 세 개를 입력해주세요: ").split( )
##
##txt1 = num1
##
##a = 100
##a -= int(txt1[0])
##a -= int(txt1[1])
##a -= int(txt1[2])

##print(a)

#2)
##num = input("숫자를 입력해주세요: ")
##txt = "삐약"
##txt *= int(num)
##
##print(txt)

##egg = int(input("계란 개수 입력: "))
##tmp = egg
##tmp %= 30
##egg //= 30
##
##print("계란 {0}판, 나머지 {1}개".format(egg,tmp))

##first = int(input("피자를 몇 등분할까?: "))
##second = int(input("한 조각을 몇 등분할까?: "))
##pizza = 100
##pizza /= first
##pizza /= second
##
##print(f"이 조각은 피자 한 판의 {pizza:.2f}%")

#3)
##num_ori = 1357
##num = num_ori
##
##num %= 10
##num1 = num % 10
##
##
##num = num // 10
##num10 = num % 10
##
##num = num // 10
##num100 = num % 10
##
##num = num // 10
##num1000 = num % 10
##
##print(num1)
##print(num10)
##print(num100)
##print(num1000)

############num_ori = 1357
############num = num_ori
############
############num %= 10
############print(num)
############
############num = num_ori
############num //= 10
############
############num %= 10
############print(num)
############
############num = num_ori
############num //= 10
############num //= 10
############
############num %= 10
############print(num)
############
############num = num_ori
############num //= 10
############num //= 10
############num //= 10
############
############num %= 10
############print(num)



#4)
##num = input("숫자 5개를 입력해주세요: ").split( )
##a = int(num[0])
##b = int(num[1])
##c = int(num[2])
##d = int(num[3])
##e = int(num[4])
##
##print(f"{(a+b+c+d+e) / 5:.3f}")


#5)
##fullstr = input("문자열을 입력해주세요: ").split( )
##txt1 = fullstr[0]
##txt2 = fullstr[1]
##
##dummy1 = txt1[0].upper()
##dummy2 = txt2[0].upper()
##
##print(dummy1+txt1[1:5], end = " ")
##print(dummy2+txt2[1:6])
