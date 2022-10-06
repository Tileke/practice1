# Декораторы в Python
# Декораторы - это функция которая в свою очередь принимает другую функцию. Декоратор позволяет обернуть другую функцию для расширения ее функйионала без изменения ее кода.

# def decorator_func(func):
#     def wrapper(some_data):
#         return f'Вы передали: {func(some_data)}'
#     return wrapper
# @decorator_func
# def get_name(name):
#     return name
# def get_last_name(last_name):
#     return last_name
# def get_age(age):
#     return age

# print(get_name('John'))
# print(get_name('John'))
# print(get_last_name('Snow'))
# print(get_age(22))
# a = (decorator_func(get_name))
# print(a('John'))



# def decorator_func(func):
#     print('Hello John')
#     return func

# @decorator_func
# def func():
#     print('Hello2')
#     return 'Hey'

# @decorator_func
# def f():
#     return 'f'

# res = decorator_func(func)
# print(func())
# print(f())



# def to_upper_dec(func):
#     def wrapper(): 
#         res = func()
#         return res.upper()
#     return wrapper
# @to_upper_dec
# def get_name():
#     return 'John'

# @to_upper_dec
# def get_last_name():
#     return 'Snow'

# print(get_name())
# print(get_last_name())


# def func_dec(f):
#     def wrapper():
#         print('Я код который отрабатывает до вызова func1')
#         f()
#         print('Я код который срабатывает после!')
#     return wrapper

# @func_dec
# def func1():
#     print('Я функция func1')


# func1()

# def decorator(func):
#     def wrapper(*args):
#         print('Hello')
#         func(*args)        
#         print('Goodbye')
#     return wrapper

# @decorator
# def func_without_paramms():
#     print('Func without params')
# @decorator
# def func_with_params(name, last_name):
#     print('Func with params')
#     print(name, last_name)

# func_without_paramms()
# func_with_params('John', 'Snow')


### Scopes. Таск 4
# balance = 0 
# def get_salary(amount):
#     global balance
#     balance = amount
# def pay_bills(amount, log_name):
#     global balance
#     balance = balance - amount
#     print (f'Вы заплатили {amount} сом за {log_name}')

# def get_balance():
#     print (f'У вас на счету {balance} сом')

# get_salary(1000)
# get_balance()
# pay_bills(400, 'кабельное тв')
# get_balance()

# def div_decor(func):
#     def wrapper(*args, **kwargs):
#         print(func.__name__)
#         return f'<div> {func(*args)} <div>'
#     return wrapper            

# @div_decor
# def get_info(name, last_name):
#     res = 2+2
#     return f'{name} {last_name} {res}'

# print(get_info('John', 'Snow'))


# def decorator_num(func):
#     def wrapper(*args):
#         res = func(*args)
#         return f'Результат сложения = {res}, и {res} это {"Even" if res % 2 == 0 else "Odd"}'
#     return wrapper
# @decorator_num
# def get_sum(list_):
#     res = 0
#     for i in list_:
#         res += i
#     return(res)    
# print(get_sum([1,2,3]))

