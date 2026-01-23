
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


text = '  abcde  '
print ( text. strip ())
print ( text. lstrip ())
print ( text. rstrip ())
