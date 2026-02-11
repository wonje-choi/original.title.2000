
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


# for i in range (1, 11):
#     if i == 5:
#         continue
#     print (i)


# for i in range (1, 11):
#     if i == 5:
#         break
#     print (i)


# for i in range (1, 11):
#     if i == 5:
#         pass
#     print (i)

# n = int (input ('n:') )

# if n > 0:
#     pass
# else :
#     pass


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


# for i in range (1, 7):
#     for j in range (1, 7):
#         print (i, j)


# li = []
# li = list ()

# li = ['a', 'b', 'c']

# li[0]
# li[1]
# li[2]

# li[2] = 'd'

# li = ['a', 'b', 'c', 'd', 'e']

# li. index ('c')

# li. append ('f')
# li. insert (0, 'aa')

# li. remove ('aa')
# del li [2]

# 'b' in li

# len (li)

# li. count ('a')

# num = [1, 2, 3, 4, 5, 9, 7, 6, 8, 10]

# sum (num)
# min (num)
# max (num)

# num. reverse ()

# num. sort ()
# num. sort (reverse = True)


# tu = ()
# tu = tupie ()

# tu = ('a', 'b', 'c')
# tu [0]
# tu [1]
# tu [2]

# tu [2] = 'd'

# tu = ('a', 'b', 'c', 'a')

# tu. index ('c')

# 'b' in tu
# len (tu)
# tu. count ('a')

# num = (5, 7, 9)
# n1, n2, n3 = num

# a = 'hello'
# b = 'world'
# (a, b) = (b, a)

# li = ['a', 'b', 'c', 'd', 'e', 'f']
# tuple (li)

# tu = ('a', 'b', 'c')
# list (tu)


# se = set ()
# se = {}

# a = {2, 4, 6, 8}
# b = {2, 4, 2, 1, 2, 3}

# a = [0]

# a. add (5)
# a. remove (5)
# 1 in a
# len (a)
# sum (a)
# min (a)
# max (a)

# list (a)
# tuple (a)

# a = {1, 2, 3}
# b = {2, 3, 4}

# a & b
# a | b
# a - b
# a ^ b

# dic = {}
# dic = dict ()

# dic = {'kor':80, 'eng':90, 'mat':77}
# dic ['kor']
# dic ['kor'] = 85
# dic ['sci'] = 92

# dic [0]

# del dic ['mat']
# dic. clear ()
# 'eng' in dic
# len (dic)

# dic. keys ()
# dic. valuse ()
# dic. items ()

# tuple (dic)
# list (dic)
# set (dic)

# li = ['ab', 'cd', 'ef']
# dict (li)

# li = [['a', 1], ['b', 2], ['c', 3]]
# dict (li)


# li1 = input ('문자 입력'). split ()

# li2 = list (input ('문자 입력'))

# li3 = []
# li3. append (int (input ('숫자 입력')))
# li3. append (int (input ('숫자 입력')))
# li3. append (int (input ('숫자 입력')))

# li4 = list (map (int, input ('숫자 입력'). split ()))
# a = input ('숫자 입력'). split ()
# b = map (int, a)
# c = list (b)

# num = list (map (int, input ('숫자 입력'). split()))

# num. sort ()

# print ('합 :', sum (num))
# print ('평균 :', sum (num) / len (num))
# print ('최소값 :', num [0])
# print ('최대값 :', num [len (num) - 1])
# print ('중간값 :', num [len (num) // 2])

# def aa ():
#     print ('hi~')

# def bb (x):
#     for i in range (x):
#         print ('hello')

# def cc ():
#     n = int (input ('n'))
#     print (n * 2)
#     return n * 2


# def dd (x, y):
#     print (x * y)
#     return x * y

# re1 = aa ()
# re2 = bb (3)
# re3 = cc ()
# re4 = dd (3, 5)


# li = []

# for i in range (5):
#     li. append (int (input ('숫자 입력')))

# for i in range (len (li)):
#     print (li [i])

# for i in li:
#     print (i)

# for i in range (len (li)):
#     if i % 2 == 0:
#         print (li [i])

# up = []
# low = []

# for i in li:
#     if i. isupper():
#         up. append (i)
#     elif i. islower ():
#         low. append (i)
# print (up)
# print (low)


# import math
# math. ceil (2.1)
# math. floor (2.1)
# math. factorial (10)
# math. sqrt (4)
# math. pi

# import random
# random. randint (1, 5)
# random. random ()

# li = ['a', 'b', 'c', 'd', 'e']
# random. choice (li)
# random. sample (li, 3)
# random. shuffle (li)

# n = int(input ('n:'))
# s = 0

# for i in range (1, n + 1):
#     s = s + i
# print (s)

# n = int(input ('n:'))
# s = 1

# for i in range (1, n + 1):
#     s = s * i
# print (s)


# n = int(input ('n:'))
# s = 0

# while n != 0:
#     s = s + n
#     n = int(input ('n:'))

# print (s)


# a = int(input ('a:'))
# b = int(input ('b:'))

# if a % b == 0:
#     print ('약수입니다.')
# else :
#     print ('약수가 아닙니다')


# a = int(input ('a:'))
# b = int(input ('b:'))

# if b % a == 0:
#     print ('배수입니다.')
# else :
#     print ('배수가 아닙니다.')


# n = int(input ('n:'))

# for i in range (1, n + 1):
#     if n % i == 0:
#         print (i)


# n = int(input ('n:'))

# for i in range (1, 101):
#     if i % n == 0:
#         print (i)


# text = input ('text:')
# t = input ('t:')

# print (t in text)

# check = False
# for i in text:
#     if i == t:
#         check = True

# print (check)


# li = list (map (int, input ('li:'). split ()))
# n = int (input ('n:'))

# check = False
# for i in li:
#     if i == n:
#         check = True

# print (check)

# print (n in li)


# n = int (input ('n:'))

# check = 0

# for i in range (1, n + 1):
#     if n % i ==0:
#         check = check + 1

# print (check)

# n = int (input ('n:'))

# li = []

# for i in range (1, n + 1):
#     if n % i ==0:
#         li. append (i)
        
# print (len (li))

# text = list(input ('text'))

# print (text. count ('o'))
# print (text. count ('x'))

# o_count = 0
# x_count = 0

# for i in text:
#     if i == 'o':
#         o_count = o_count + 1
#     elif i == 'x':
#         x_count = x_count + 1

# print (o_count)
# print (x_count)


# num = list (map (int, input ('num:'). split()))

# avg = sum (num) / len (num)
# check = 0
# for i in num:
#     if i >= avg:
#         check = check + 1
    
# print (avg)
# print (check)


# n = int (input ('n:'))

# check = 0
# for i in range (n, n + 1):
#     if n % i == 0:
#         check = check + 1

# if check == 2:
#     print (True)
# else :
#     print (False)

# n = int (input ('n:'))
# check = True
# for i in range (2, n):
#     if n % i == 0:
#         check = False
# print (check)


# a = int (input ('a:'))

# li = []

# for n in range (2, a + 1):
#     check = True
#     for i in range (2, n):
#         if n % i == 0:
#             check = False
#     if check :
#         li .append (n)


# n = int(input ('n:'))

# a = 3

# for i in range (n-1):
#     a = a + 5

# print (a)


# n = int(input ('n:'))
# a = int(input ('a:'))
# r = int(input ('r:'))

# for i in range (n-1):
#     a = a * r

# print (a)


# n = int(input ('n:'))

# a = 1
# b = 1

# for i in range (n - 2):
#     c = a + b
#     a = b
#     b = c

# print (b)


# n = int(input ('n:'))

# for i in range (n):
#     print (' ' * i, end = '')
#     print ('*' * n)


# n = int(input ('n:'))

# for i in range (1, n + 1):
#     print ('*' * i)


# n = int(input ('n:'))

# for i in range (1, n + 1):
#     print (' ' * (n - i), end = '')
#     print ('*' * i)

# n = int(input ('n:'))

# for i in range (n):
#     print ('*' * (n - i))

# n = int(input ('n:'))

# for i in range (n):
#     print (' ' * i, end = '')
#     print ('*' * (n - i))


# n = int(input ('n:'))

# for i in range (n):
#     print (' ' * (n - i - 1), end = '')
#     print ('*' * (i * 2 +1))


# a = int(input ('a:'))
# b = int(input ('b:'))
# n = int(input ('n:'))

# for i in range (1, a + 1):
#     for j in range (1, b + 1):
#         if i + j == n:
#               print (i , j)


# for i in range (2, 10):
#     for j in range (1, 10):
#         print ('{} * {} = {}'. format (i, j, i * j))
#     print ()


# li = [[1, 2, 3, 4], [5, 6, 7, 8]]

# for i in range (len (li)):
#     for j in range (len(li [i])):
#         print (li [i] [j], end = '')
#     print ()


text = input ('text')

for i in text:
    if i != ' ':
        print (i, end = '')
        

