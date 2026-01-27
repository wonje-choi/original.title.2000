
# print('안녕하세요.') #인사 코드

# print('A')

# '''
# 여러줄의
# 주석을
# 처리하는
# 방법입니다.
# '''
# print('B')
# print('C')

# print('hi~ Python')


# a = 10
# b = 5 

# print(a)
# print(b)
# b = 7
# print(a + b)


# print('hi', 'hello')

# name = input('이름을 입력해주세요')


# type()
# int()
# float()
# complex()

# a=10 
# b=5 
# c=2.0
# d=0.5

# print(b+c)
# print(b-b)
# print(b*b)
# print(b/b)
# print(b//c)
# print(b%c)
# print(b**c)

# bool
# >
# <
# ==
# !=
# or and not

# a=5  int
# b='5' str
# c=5.0  float

# print(b+b)
# print(a*b)

# list
# tuple
# set
# dictionary

# a = int(input('숫자를 입력하세요'))

# print (a+a)

# num = 5.0

# range(int(num))

# a = input ('숫자 하나 입력')
# b = int (a)
# c = float (a)

# print (type(a))
# print (type(b))
# print (type(c))

# a, b, c = map (int, input ('a b c 값 입력').split())

# print ( a, b, c, a + b + c)

# a, b, c = map ( int, ['1', '2', '3'])

# print ( a, b, c, a + b + c)

# text = input ('a b c 값 입력')
# text = text.split()
# a, b, c, = map (int, text) 

# print (a, b, c, a + b + c)

# a, b, c = map (int, input ('a b c 값 입력'). split())

# x = 3
# y = 5

# print (x, y, x + y)
# print ('3과 8의 합은 8이다')

# print ('{}과 {}의 합은 {}이다.' .format (x, y, x+y))

# 2 * 5 > 2 + 5 and not 3 * 3 > 10

# print (round (3.33))
# print (round (3.66))
# print (round (3.66, 1))

# print ( abs (3))

# print (pow(3, 2))
# print (3**2)

# x, y = divmod (7, 2)
# print (x)
# print (y)

# print (max())
# print (min())

# print (sum([]))

# text = 'abc'

# print (text [0])
# print (text [1])
# print (text [2])
# #print (text [3])
# print (text [-3])
# print (text [-2])
# print (text [-1])
# #print (text [2.0])


# text = 'abcde fgh ijk'

# print (text [2 : 5])
# print (text [1 : 8])
# print (text [-5 : -1])

# print (text [5 : ])
# print (text [ : 5])
# print (text [ : ])
# print (text [0 : 8 : 2])
# print (text [1 : 8 : 2])
# print (text [8 : 0 : -1])
# print (text [8 : 5 : -1])
# print (text [ : : -1])


# text = 'abcde {} {}'
# print ( text. format ( 'ABC', 123))

# text = 'abcde ABC ABC'
# print (text. replace ( 'ABC', 'KKK'))

# text = 'abcde A/B/C A.B.C'
# a, b, c = text. split ( '/' )
# print (a)
# print (b)
# print (c)

# text = 'abcde'
# print ( '/'. join (text))


# text = 'abcde A/B/C A.B.C'

# print ( text. count ( 'a' ))
# print ( text. count ( 'A' ))


# text = '  abcde  '
# print ( text. strip ())
# print ( text. lstrip ())
# print ( text. rstrip ())


# text = 'ABC ABC'
# print ( text. find ( 'A' ))
# print ( text. rfind ( 'A' ))
# print ( text. index ( 'A' ))
# print ( text. rindex ( 'A' ))


# text1 = 'ABCabc123'
# text2 = '123'
# text3 = 'ABC'
# text4 = 'abc'

# print ( text1. isalpha ())
# print ( text1. isdigit ())
# print ( text1. isalnum ())
# print ( text1. isupper ())
# print ( text1. islower ())

# text = 'ABCabc'
# print ( text. upper ())
# print ( text. lower ())


# y = '2026'
# m = '1'
# d = '23'
# print ( y. zfill(4))
# print ( m. zfill(2))
# print ( d. zfill(2))


# num = int ( input ('숫자하나 입력 : ') )

# if num > 0 :
#     print ( '{}은(는) 양수입니다.' .format (num) )


# num = int ( input ('숫자하나 입력 : ') )

# if num % 2 == 0 :
#     print ( '{}은(는) 짝수입니다.' .format (num) )
# else :
#     print ( '{}은(는) 홀수입니다.' .format (num) )


# age = int ( input ('나이 입력 : ') )

# if age <= 7 :
#     print ( '유아입니다')
# elif age <= 19 :
#     print ( '청소년입니다')
# elif age >= 20 :
#     print ( '성인입니다')

# text = input ( '알파벳 입력 :' )

# if text.isupper () : 
#     print ( '대문자' )
# elif text.islower () : 
#     print ( '소문자' )
# else : 
#     print ( '대/소문자 구분 불가능' )

# print ( 'a가 0보다 같거나 크면 실행, 작으면 정지')

# a = int ( input ( 'a:' ))

# while a >= 0:
#     print ( '실행' )
#     a = int ( input ( 'a:' ))

# a = 10

# while a > 0:
#     print ( '실행' )

# n = int ( input ( 'n:') )

# while n:
#     print ( n )
#     n = n - 1

# n = 1
# while n <= 10:
#     print ( n )
#     n = n + 1

# text = 'yes'

# while text == 'yes':
#     text = input ( 'yes 입력 시 반복' )

# print ( '종료' )


# text = input ( 'e 또는 E 입력시 종료' )

# while text != 'e' and text != 'E':
#     text = input ('e 또는 E 입력 시 종료')

# print ( '종료' )


# print (list (range (0, 5)))

# print (list (range (1, 11)))

# print (list (range (3, 10, 3)))

# print (list (range (5, 0, -1)))

# print (list (range (10, -11, -5)))


# for i in range ( 10 ) :
#     print ( i )


# n = int ( input ( 'n' ) )

# for i in range ( 1, n + 1 ) :
#     print ( i )


# a, b = map(int, input ( 'a b:' ). split () )

# for i in range ( a, b ) :
#     print ( i )

# n = int ( input ( 'n:') )

# for i in range ( n, n - 1, - 1 ) :
#     print ( i )


# age = int (input ( '나이 입력:' ) )

# if age <= 7:
#     print ( '유아입니다.' )
# elif age <= 19:
#     print ( '청소년입니다.' )
#     if age <= 13:
#         print ( '초등학생' )
#     elif age <= 16:
#         print ( '중학생' )
#     else :
#         print ( '고등학생' )
# else :
#     print ( '성인입니다' )


# n = int (input ( 'n:' ))
# for i in range ( 1, n + 1 ) :
#     if i % 3 == 0 :
#         print ( 'x' )
#     else :
#         print (i)


# num1 = 0
# num2 = int (input ( 'n:' ) )

# while True :
#     num1 = num1 + 1
#     print ( num1 )
#     if num1 == num2:
#         break


for i in range (1, 7):
    for j in range (1, 7):
        print (i, j)