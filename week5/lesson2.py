# Области видимости и пространство имен 

# LEGB - Local, Enclose, Global, Built-in
# Области видимости определеят как переменные и имена ищутся в вашем коде. Область видимости имен или переменной зависти от того места в коде, где вы созвдете эту перменную.
# 


x = 'Global variable'

# def func1():
#     print(  )
#     # x = x + 2
#     # x = 'Enclosed variable'
#     # print(x)
#     def func2():
#         x = 'Local variable'
#         print(x)
#     func2()
# func1()


# x = 2 
# def f():
#     y = 2
#     print(locals())
#     def f2():
#         print(locals())
#     f2()
# f()
# print(locals())
# print(globals())

# x = 0
# def counter():
#     global x
#     x += 1
#     print(x)
# counter()
# counter()
# counter()

# x = 10
# def f():
#     x = 20
#     # global x
#     # x +=  12
#     print(x)
#     def f2():
#         # x = 40
#         nonlocal x
#         x += 1
#         print(x)
#     f2()
# print(x)
# f()

# print(dir(__builtins__))

def is_palindrome(x):
    x = x.lower()
    if x[::1] == x[::-1]:
        return(True)
    else:
        return(False)
print(is_palindrome('Mom'))

# def getSum(n):
    
#     sum = 0
#     for i in str(n): 
#       sum += int(i)      
#     return sum
   
# print(getSum(12345))