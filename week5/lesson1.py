# set1 = set([i for i in range(1, 11])
# set2 = set([i for i in range(11, 21)])
# full_set = set1|set2
# length = len(full_set)
# if len(full_set) < 20:
#     result = 

# Введение в функции. Позиционные и именованные, args, kwargs аргументы параметры /по default 

# Встроенные функции - len, print, sum, max, min, dir, int, list и т.д.

# def get_sum(x,y): # Параметры
#     s = x + y
#     return(s)
#     print('fdfdsf') # не сработает
# print(get_sum(2,3)) # Аргументы


# def get_mult(x,y,z):
#     return x * y * z
# print(get_mult(2,3,4))

# Аннотации функции
# def funct1(x: int, y: int) -> int:
#     return(x * y)
# print(funct1(2,4))


# def func2(x='Tolik'):
#     return x + 'John'
# print(func2())

# def func3(x: int ,y: int ,z: int=2) -> int:
#     return(x + y + z)
# print(func3(3,1,1)) # 5
# print(func3(3,1)) # 6

# list_ = [1, 2, 5, 6]
# sum = 0
# for i in list_:
#     sum += i
# print(sum)

def my_sum(l):
    sum = 0
    for i in l:
        sum += i
    return sum
# print(my_sum(list_))

# Позиционные и именованные аргументы 
# def func4(x, y, z):
#     print(x,y,z)
# func4(2, 3, 5) # передали как позиционные аргументы
# func4(y=5, z=2, x=3) # передали аргументы как именованные 
# func4(y=5, 4, 3) # SyntaxError (после именованных аргументов не могут идти позиционные)
# func4(2, 3, z=5)

# *args & **kwargs - позиционные аргументы и именнованные аргументы

# def func5(x, y, *args, **kwargs):
#     print(args) #tuple
#     print(kwargs) #dict
#     return x + y + my_sum(args) + sum(kwargs.values())
# print(func5(5, 4, 5, 2, 1, c=7))


# def func6(x: int, y):
#     l = []
#     for i in range(x, y+1):
#         l.append(i)
#     return(l)
# print(func6(1, 5))

# def func6(x, y):
#     l = list(range(x, y+1))
#     return(l)
# print(func6(1, 5))

# def f():
#     if False:
#         pass
#         return 'f'
#     else:
#         pass
#         return 't'


# inp1 = int(input(': '))
# inp2 = int(input(': '))
# if TypeError:
#     print(inp1,inp2)
# else:
#     print(inp1 + inp2)

# inp1 = int(input(': '))
# inp2 = int(input(': '))
# if inp1.isalpha or inp2.isalpha:
#     print(inp1,inp2)
# else:
#     print(inp1 + inp2)

def func8(x, *args):
    print(x, args)

func8([1, 23], 'john', 'tolik', 8, {'a': 5})