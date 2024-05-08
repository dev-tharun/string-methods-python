#isidentifier
s='123'
print(s.isidentifier())
str="My folder"
print(str.isidentifier())
str_1="myName"
print(str_1.isidentifier())
str_2="MyName"
print(str_2.isidentifier())
str_3="1MyName"
print(str_3.isidentifier())
str="My_1Name"
print(str.isidentifier())
print("==============================================")
#isprintable
s="tharun\n"
print(s.isprintable())
s="tharun\n\t"
print(s.isprintable())
# print(repr(s))
s="tharun12321@!"
print(s.isprintable())
s="tharun"
print(s.isprintable())
print("==============================================")
#join
str_1=(["AA","BB","CC","@@@","ddd","22","ssss"])
str2="k:"
print(str2.join(str_1))
print("==============================================")
#ljust left just
s="monty 123 python"
# print(len(s))
print(s.ljust(30,"^"))
print("==============================================")
#rjust right just
s="monty 123 python"
# print(len(s))
print(s.rjust(30,"^"))


