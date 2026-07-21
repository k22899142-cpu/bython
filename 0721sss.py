##a = "{:+d}".format(3)
##print(a)
##
##
##a = "{:-d}".format(+3)
##print(a)
##
##a = "{: d}".format(n)
##print(a)
##
##
##
##
##
##
##a = "{:5d}".format(-3)
##print(a)
##
##a = "{:05d}".format(-3)
##print(a)
##
##
##num1 = int(input("첫 번째 숫자 입력: "))
##num2 = int(input("두 번째 숫자 입력: "))
##
##print(f"num1+num2 = {num1+num2}")
##print(f"num1-num2 = {num1-num2}")
##print(f"num1*num2 = {num1*num2}")
##print(f"num1/num2 = {num1/num2:.2f}")
##
##1)
##num1 = int(input("숫자를 입력해주세요: "))
##print(f"num1 + 50 = {num1 + 50}")
##print(f"num1 - 50 = {num1 - 50}")
##print(f"num1 * 50 = {num1 * 50}")
##print(f"num1 / 50 = {num1 / 50:.3f}")
##
##2)
##w1= 3
##w2 = 4
##h = 5
##
##print(f"사다리꼴의 넓이는 (3 + 4) * 5 / 2 = {(w1+w2)*h/2}")
##
##
##num1 = int(input("첫 번째 숫자 입력: "))
##num2 = int(input("두 번째 숫자 입력: "))
##
##print(f"num1 // num2 = {num1 // num2}")
##print(f"num1 % num2 = {num1 % num2}")
##print(f"num1 ** num2 = {num1 ** num2}")
##
##
##3)
##num1 = int(input("숫자를 입력해주세요: "))
##print(f"num1 // 4 = {num1 // 4}")
##print(f"num1 % 4 = {num1 % 4}")
##print(f"num1 ** 4 = {num1 ** 4}")
##
##
##4)
##num1 = int(input("몸무게(kg)를 입력하세요: "))
##num2 = float(input("키(m)를 입력하세요: "))
##
##print(f"BMI 지수는 {num1 / num2 ** 2:.2f}")
##


##sec = int(input("초 입력: "))
##
##min = sec // 60
##sec = sec % 60
##
##hour = min // 60
##min = min % 60
##
##day = hour // 24
##hour = hour % 24
##
##print(f"{day}일 {hour}시간 {min}분 {sec}초")

##num = int(input("세 자리 숫자 입력 : "))
##
##num1 = num % 10
##num = num // 10
##
##num10 = num % 10
##num = num // 10
##num100 = num % 10
##
##print(f"백의 자리: {num100}")
##print(f"십의 자리: {num10}")
##print(f"일의 자리: {num1}")


##num = int(input("물건의 가격을 입력합니다: "))
##
##num = 1000 - num
##
##num500 = num // 500
##num = num % 500
##print(f"500원 {num500}개")
##
##
##num100 = num // 100
##num = num % 100
##print(f"100원 {num100}개")
##
##
##num50 = num // 50
##num = num % 50
##print(f"50원 {num50}개")
##
##num10 = num // 10
##print(f"10원 {num10}개")


##num1 = (1000 - num)
##
##num2 = (f"500원 {num1 // 500}개")
##
##num3 = (790 % 500)
##
##num4 = (f"100원 {num3 // 100}개")
##
##num5 = (290 % 200)
##
##num6 = (f"50원 {num5 // 50}개")
##
##num7 = (90 % 50)
##
##num8 = (f"10원 {num7 // 10}개")
##
##print(num2)
##print(num4)
##print(num6)
##print(num8)


##num = int(input("다섯 자리 숫자를 입력합니다: "))
##
##num1 = num % 10
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
##num = num // 10
##num10000 = num % 10
##
##print(f"만의 자리: {num10000}")
##print(f"천의 자리: {num1000}")
##print(f"백의 자리: {num100}")
##print(f"십의 자리: {num10}")
##print(f"일의 자리: {num1}")

##num = int(input("세 자리 숫자 입력 : "))
##
##num1 = num % 10
##
##num = num // 10
##num10 = num % 10
##
##num = num // 10
##num100 = num % 10
##
##print(f"백의 자리: {num100}")
##print(f"십의 자리: {num10}")
##print(f"일의 자리: {num1}")

num1 = int(input("첫 번째 숫자 입력: "))
num2 = int(input("두 번째 숫자 입력: "))
num3 = int(input("세 번째 숫자 입력: "))

print(f"10000+= num1 --> {10000+num1}")
print(f"10000-= num1 --->{10000-num1}")
print(f"10000*=num1 --->{10000*num1}")




