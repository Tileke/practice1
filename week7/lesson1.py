# CRUD магазина на функциях 
    # C - CREATE
    # R - READ
    # U - UPDATE
    # D - DELETE


import datetime

data = [
    {
        'id': 1,
        'name': 'product1',
        'price': 100,
        'created_at': datetime.datetime(2022, 10, 4),
        'is_active': True
    }
]

def get_products():
    return data

def get_one_product(id):
    product = [i for i in data if i['id'] == id]
    if product:
        return product[0]
    return 'Item not found'

def post_product():
    max_id = max([i['id'] for i in data])
    new_data = {
        'id': max_id + 1,
        'name': input('Enter item name: '),
        'price': int(input('Enter item price: ')),
        'created_at': datetime.datetime.now(),
        'is_active': True
    }
    data.append(new_data)
    return f'Iitem succesfully published: \n{new_data}'
    
def delete_product(id):
    delete_product = [i for i in data if i['id'] == id]
    if delete_product:
        data.remove(delete_product[0])
        return 'Item succesfully deleted!'
    return 'Item not found'

def update_product(id):
    update_product = [i for i in data if i['id'] == id]
    if update_product:
        index_item = data.index(update_product[0])

        if input('Do you want to change product name? \n(yes/no) \n: ') == 'yes':
            data[index_item]['name'] = input('Enter new name: ')
        if input('Do you want to change product price? \n(yes/no) \n: ') == 'yes':
            data[index_item]['price'] = int(input('Enter new price: '))
        return 'Update succesful'
    return 'Item not found'


def main():
    while True:
        method = input('Hello, here is the list of functions: \n1 - get all of the products \n2 - get specific item \n3 - create new product \n4 - delete item \n5 - update item \n6 - stop the program \nEnter the number: ')
        if method == '1':
            print(get_products())
        elif method == '2':
            id = int(input('Enter id of the item: '))
            print(get_one_product(id))
        elif method == '3':
            print(post_product())
        elif method == '4':
            id = int(input('Enter id of the item you want to delete: '))
            print(delete_product(id))
        elif method == '5':
            id = int(input('Enter id of the item you want to update: '))
            print(update_product(id))
        elif method == '6':
            print('Program stopped')
            break
        else:
            print('Function not found')
if __name__ == '__main__':
    main()