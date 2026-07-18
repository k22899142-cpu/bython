#1단원 전체 복습

##print("안녕","반갑습니다." , sep= " ")
###sep이 없으면 그냥 기본적으로 띄어쓰기가 들어가게 되는 거고,
###sep이 생기면 그 띄어쓰기( , 때문에 생기는) 자리에 sep 값이 들어가게 되는 것
##
##print("너는 참 ","이야!", sep = '좋은 사람')

##print('안녕하세요', end = ' ')
##print('안녕하세요', end = ' ')
##print('안녕하세요\n')
##print('do ye')

##print('\\n')
##print("\"", "\'는 따옴표임")


##print(1,2,3,'apple')

##print('이샘', end = "")
##print('코딩', end = "")
##print('학원', end = "!")

##print(1,2,3,sep = "+", end = "=6")


##print("48 > %d, %o" %(48,48))
##print("48 > %c, %x" %(48,48))

##print("%c, %c" %(65,45))
##
##print("%c" %(46))

##print("%.2f %e" %(0.132, 4.567))
##
##print("이샘%s학원" %('코딩'))

##num1 = 17
##print(num1)
##print("10진수 17 = %d" %(num1))
##print("10진수 17의 8진수 = %o" %(num1))
##print("10진수 17의 16진수 = %x" %(num1))
##

##num2 = 97
##print("%d %c" %(num2,num2))
##
##float1 = 1234.567
##print(float(float1))
##print("기본 출력: %f" %(float1))
##print("지수표기법: %e" %(float1))
##print("소수 둘째자리까지: %.2f" %(float1))


##txt1 = "Hello!"
##txt2 = "World!"
##
##print("기본 출력\n%s %s" %(txt1, txt2))
##
##print("기본 출력\n%10s %5s" %(txt1, txt2))


##print("%c"%(5))
##
##
##print("{0:x} {1:c}".format(48,48))

##print("48 > {0} {1:o}".format(48,48))
##print('이샘{0}학원'.format('코딩'))
##print(f'{48:c},r {49:x}')
##
##
##print("%c"%(50))
##print("{0:c}".format(50))
##print(f"{50:c}")


##num1 = 17
##print(num1)
##
##print("10진수 17 = {0:d}".format(num1))
##
##print("10진수 17의 8진수 = {0:o}".format(num1))
##
##print("10진수 17의 16진수 = {0:x}".format(num1))



##num2 = 33
##print("{0} {1:c}".format(num2, num2))
##
##
##float1 = 1234.56789877655433
##print(float1)
##
##print("기본 출력 {0:f}".format(float1))
##
##print("지수표기법 {0:e}".format(float1))
##
##print("소수 둘째자리까지 {0:.2f}".format(float1))


##txt1 = "Hello!"
##txt2 = "World!"
##
##print(f'기본 출력\n{txt1:s}{txt2:s}')
##
##print(f'10칸 출력\n{txt1:10s}{txt2:10s}')

#1)
r = 5
pi = 3.14

##print('넓이는 %.0f * %.0f * %.2f = 78.5' %(r,r,pi))
##
##print('넓이는 {0} * {1} * {2} = 78.5'.format(r,r,pi))
##
##print(f'넓이는 {r} * {r} * {pi} = 78.5')

##golden_ratio = 1.61804 
##print(f'소수 첫째 자리까지 출력: {golden_ratio:.1f}')
##print(f'소수 둘째 자리까지 출력: {golden_ratio:.2f}')
##print(f'소수 셋째 자리까지 출력: {golden_ratio:.3f}')
##print(f'소수 넷째 자리까지 출력: {golden_ratio:.4f}')


NA = float(input("실수를 입력하세요: "))

MA = f'{NA*10:.3f}'

print(MA)








