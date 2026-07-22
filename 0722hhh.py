#0722 복습

##num1 = int(input("첫 번째 숫자 입력: "))
##num2 = int(input("두 번째 숫자 입력: "))
##
##print(f"num1 + num2 = {num1 + num2}")
##print(f"num1 - num2 = {num1 - num2}")
##print(f"num1 * num2 = {num1 * num2}")
##print(f"num1 / num2 = {num1 / num2:.2f}")
##

##num1 = int(input("첫 번째 숫자 입력: "))
##num2 = int(input("두 번째 숫자 입력: "))
##
##print(f"num1 // num2 = {num1 // num2}")
##print(f"num1 % num2 = {num1 % num2}")
##print(f"num1 ** num2 = {num1 ** num2}")

##sec = int(input("초 입력: "))
##
##min = sec // 60
##
##sec = sec % 60
##
##hour = min // 60
##
##min = min % 60
##
##day = hour // 24
##
##hour = hour % 24
##
##print(f"{day}일 {hour}시간 {min}분 {sec}초")



##sec = int(input("초를 입력하시오: "))
##
##min = sec // 60
##sec = sec % 60
##
##hour = min // 60
##min = min % 60
##
##day = hour // 60
##hour = hour % 60
##
##print(f"{day}일 {hour}시간 {min}분 {sec}초")


##num = int(input("세 자리 숫자 입력: "))
##
##num1 = num % 10
##num = num // 10
##
##num10 = num % 10
##num = num // 10
##
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
##
##num100 = num // 100
##num = num % 100
##
##num50 = num // 50
##num = num % 50
##
##num10 = num // 10
##num = num % 10
##
##print(f"500원 {num500}개")
##print(f"100원{num100}개")
##print(f"50원 {num50}개")
##print(f"10원{num10}개")


num = int(input("다섯 자리 숫자를 입력합니다: "))

num1 = num % 10
num = num // 10

num10 = num % 10
num = num // 10

num100 = num % 10
num = num // 10

num1000 = num % 10
num = num // 10

num10000 = num % 10
num = num // 10
print(f"만의 자리: {num10000}")
print(f"천의 자리: {num1000}")
print(f"백의 자리: {num100}")
print(f"십의 자리: {num10}")
print(f"일의 자리: {num1}")










