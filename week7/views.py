import json

FILE_PATH = 'data.json'

def get_data(ge_price=None, le_price=None):
    with open(FILE_PATH) as file:
        data = json.load(file)
    if ge_price:
        new_data = [i for i in data if i['price'] >= ge_price]
        return new_data
    if le_price:
        new_data = [i for i in data if i['price'] <= le_price]
        return new_data
    return data

def get_one_data(id):
    data = get_data()
    one_data = [i for i in data if i['id'] == id]
    if one_data:
        return one_data[0]
    return 'Item not found'

def post_data():
    data = get_data()
    max_id = max([i['id'] for i in data])
    data.append({
        'id': max_id + 1,
        'name': input('Enter new item name: '),
        'price': float(input('Enter item price: '))
    })
    with open(FILE_PATH, 'w') as file:
        json.dump(data, file)
    return 'Item uploaded'    

def update_data(id):
    data = get_data()
    data_update = [i for i in data if i['id'] == id]
    if data_update:
        index_data = data.index(data_update[0])
        if input('Do you want to change product name? \n(yes/no) \n: ') == 'yes':
            data[index_data]['name'] = input('Enter new name: ')
        if input('Do you want to change product price? \n(yes/no) \n: ') == 'yes':
            data[index_data]['price'] = float(input('Enter new price: '))
            json.dump(data, open(FILE_PATH, 'w'))
        return 'Update succesful!'
    return 'Item not found'    

def delete_data(id):
    data = get_data()
    data_delete = [i for i in data if i['id'] == id]
    if data_delete:
        data.remove(data_delete[0])
        json.dump(data, open(FILE_PATH, 'w'))
        return 'Item succesfully deleted!'
    return 'Item not found'
