# def get_sum(a, b):
#     return a + b

# a = lambda a, b: a + b
# print(a)

# a = lambda str1, str2: str1 + str2
# print(a('hello','world'))

# f = lambda x: print(x)

# a = lambda a, b, c: (a + b) * c
# print(a(1,2,3))

# split and join 
# s = 'hello john snow'
# l = s.split('l')
# print(l)

# l = ['hello', 'john', 'snow']
# s = ' '.join(l)
# print(s)


# sort() vs sorted()
# print(dir(list)) # sort
# l = ['aaaa', 'aa', 'b', 'ffff', 'A']
# l.sort(reverse = True)
# l.sort(key=len)
# print(l)

# l = ['a', 2, 3]
# l.sort()

# s = 'asdfsdfsda'
# s2 = sorted(s)
# s3 = ''.join(s2)
# print(s2)
# print(s3)

# Константа 
# AGE = 18

# import random 
# l = ['John', 'Snow', 'Tolik']
# answer = random.choice(l)
# print(answer)
# print(dir(random))

# print(random.randint(0, 100))

# def f():
#     global x
#     x = 100
# f()
# print(x)

# x = 100
# def f():
#     x = 30
#     print(id(x))
# print(id(x))
# f()

# x = 10
# def f1():
#     # global x
#     x = 20
#     print(x)
#     def f2():
#         nonlocal x
#         print(x)
#         x = 30
#         print(x)
#     f2()
# f1()
# print(x)

# print(globals())

''' Рекурсия learn '''

# l = [ord(str(i)) for i in range(10)]
# print(l)

# import time
# import datetime
# print(datetime.datetime.now())
# for i in range(10):
#     print(i)
#     time.sleep(1)

# def sum_num(x):
#     # r = 0
#     # for i in str(x):
#     #     r += int(i)
#     # return(r)
#     return sum([int(i) for i in str(x)])
# print(sum_num(985)) 




# Перед новым годом магазин решил оповестить всех покупателей, которые есть в базе данных о том, что 
# сейчас дейстыует скидка на алкоголь, необходимо на основе данных разослать всем клиентам оповещение о 
# скидке, и нужно игнорировать тех, кому нет 18 лет, данные представлены 
# в след. виде: [('Jack', 25), ('Helen', 18), ('Mike', 15), ('Jessica', 32), ('Jack', 25), ('Alice', 28), ('Mike', 15)]
# в данном списке встречаются повторяющиеся данные, необходимо избавиться от дубликатов и 
# отправить приглашение клиенту только один раз

# a = dict([('Jack', 25), ('Helen', 18), ('Mike', 15), ('Jessica', 32), ('Jack', 25), ('Alice', 28), ('Mike', 15)])
# for k, v in a.items():
#     if v >= 18:
#         print(f'{k}, we got discounts for alchohol')

# a = [('Jack', 25), ('Helen', 18), ('Mike', 15), ('Jessica', 32), ('Jack', 25), ('Alice', 28), ('Mike', 15)]
# for i in {name for name, age in a if age >= 18}:
#     print(f'{i}, we got discounts for alchohol')




# в новый год вы решили сделать друзьям подарки, список друзей выглядит след. 
# образом: ['Tom', 'Jessica', 'Helen', 'Jim', 'Bob', 'Alice'], у вас есть определенное количество подарков 
# различных категорий, представлено в след виде: [['Harry Potter', 'It', 'Rich&Poor Dad'], 
# ['Samsung Phone', 'Xiaomi Phone', 'iPhone'], ['20% Gucci discount', '10% LV discount', '15% Apple discount']], 
# использую встроенный модуль рандом, необходимо каждому другу выбрать подарок и результат 
# в следующем виде вывести в терминал:
# 'Tom' --> 'Xiaomi Phone'
# 'Jessica' --> '20% Gucci discount'
# 'Helen' --> 'Rich&Poor Dad'
# и тд.
# для каждого друга рандомно должна выбираться категория подарков и рандомный подарок из этой категории соответственно.
# Требования: использовать рандом, каждому другу должен достаться уникальный 
# подарок(т.е. нельзя дарить один подарок нескольким)

import random
a = ['Tom', 'Jessica', 'Helen', 'Jim', 'Bob', 'Alice']
gifts = [['Harry Potter', 'It', 'Rich&Poor Dad'], ['Samsung Phone', 'Xiaomi Phone', 'iPhone'], ['20% Gucci dicount', '10% LV discount', '15% Apple discount']]

# gift_type = []
# for i in a:
#     while gift_type == []:
#         gift_type = random.choice(gifts)
#     gift = random.choice(gift_type)
#     print(f'{i} --> {gift}')
#     gift_type.remove(gift)


for friend in a:
    present = random.choice(gifts)
    present1 = random.choice(present)
    print(f'{friend} ---> {present1}')
    present.remove(present1)
    if len(present) == 0:
        gifts.remove(present)