str="we are\tlearning 12345 \tdata\tscience"
print("original string is \n:",str)
print(len(str))
print('=======================')
#expandtabs 1
str="we are\tlearning 12345 \tdata\tscience"
print("original string is \n:",str)
print('tabsize is nothing:',str.expandtabs())
print(len(str.expandtabs()))
print('=======================')
#rfind 2
str='tharuntharuntharun'
print(len(str))#count start with number 1,2,3,...18
print(str.rfind('t'))#count start with index number 0,1,2,...17
print(str.rfind('o'))#not there string letters means o/p comes -1
print('=======================')
#rindex 3
str='tharuntharuntharun'
print(len(str))#count start with number 1,2,3,...18
print(str.rindex('a'))#count start with index number 0,1,2,...17
# print(str.rindex())#takes at least 1 argument
print('=======================')
#isaplha 4
s=''#empty string
print(s.isalpha())
s='sample things'# not allow the cos of space
print(s.isalpha())
s='samplethings123'# not allow the num also only allow aplha
print(s.isalpha())
s='samplethings'
print(s.isalpha())#only allow the alpha in string fun
print('=======================')
#isaacii 5
str='@_Tth123'
print(str.isascii())
print('=======================')
#isdecimal
s='11.0'
print(s.isdecimal())
s='3¹'#base value not allow
print(s.isdecimal())
s='०३'
print(s.isdecimal())
print('=======================')
#isdigit
s='1.'
print(s.isdigit())
s='3¹'#power value allow
print(s.isdigit())
s='¹'#base value allow
print(s.isdigit())
print('=======================')

s='1.'
print(s.isnumeric())
s='3¹'#power value allow
print(s.isnumeric())
s='¹'#base value allow
print(s.isnumeric())



