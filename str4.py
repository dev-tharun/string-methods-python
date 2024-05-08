#ISUPPER
s= "python1@"
print(s.isupper())
s= "PYTHON12@"
print(s.isupper())
print("============================================================")
#UPPER and lower
s= " I am learning python"
print(s.upper())
s=" I am learning PYTHON"
print(s.lower())
print("============================================================")
#partition
S="I am learning for python for every day"
print(S.partition("for"))
print("============================================================")
#right partition
S="I am learning for python for every day"
print(S.rpartition("for"))
print("============================================================")
#replace
s="1. I am learning java java java java for every day"
print(s.replace("java","python"))
s = "2. I am learning java java java java for every day"
print(s.replace("java","python",2))
s = "3. I am learning java java java java for every day"
print(s.replace("java","# ",3))
print("============================================================")
#split
s="I am learning python for every day"
print(s.split())
s="I am learning python for every da y"
print(s.split())
s="I am learning python for every day"
print(s.split("python"))
s="I ::am learning python for every day"
print(s.split(":"))
print("============================================================")
#right split
s="I am learning python for every day"
print(s.rsplit())
s="I am learning python for every da y"
print(s.rsplit())
s="I am learning python for every ::day"
print(s.rsplit(":"))
print("============================================================")
#splitlines \n
s="I am learning \npython for every day"
print(s.splitlines())
s="I am learning \n python for\n every day"
print(s.splitlines(True))
print("============================================================")
#startswith
s="I am learning  python for every day"
print(s.startswith("p"))
s="I am learning  python for every day"
print(s.startswith("i"))
s="I am learning  python for every day"
print(s.startswith("I"))
s="'I am learning  python for every day'"
print(s.startswith("I"))
s="'I am learning  python for every day'"
print(s.startswith("'"))
print("============================================================")
#strip
s="@@@@@@@@@@@@............,,,pythonttttttttttttttttttt"
print(s.strip("@.,t"))
s="python"
print("I am learning",s.strip(),"for every day")
print("============================================================")
#swapcase
s="i am learning  python for every day"
print(s.swapcase())
s="i aM learNing  pythOn fOr evEry dAy"
print(s.swapcase())
print("============================================================")
#casefold
s="mel@gmail.COM"
a=(s.casefold())
print(a)
s1="mel@gmail.com"
b=(s.casefold())
print(b)
print(s==s1)
print(a==b)
print("============================================================")
#ENCODE
S="MONTY 123 PYTHON"
print(S.encode())
print(type(S.encode()))
print("============================================================")
# martrans & Translate
str1='python'
str2='@12645'
martran=str.maketrans(str1,str2)
print(martran)
str3="I am learning python"
print(str3.translate(martran))









