from views import *

def main():
    while True:
        method = input('Hello, here is the list of functions: \n1 - get all of the products \n2 - get specific item \n3 - create new product \n4 - delete item \n5 - update item \n6 - stop the program \nEnter the number: ')
        if method == '1':
            filter = input('Want to filter profucts by price? \nIf yes, type "more", "less" or "no": ')
            if filter == 'more' or filter =='less':
                filter_num = int(input('Enter the number to filter with: '))
                if filter == 'more':
                    print(get_data(ge_price=filter_num))
                if filter == 'less':
                    print(get_data(le_price=filter_num))
            else:
                print(get_data())    
        elif method == '2':
            id = int(input('Enter id of the item: '))
            print(get_one_data(id))
        elif method == '3':
            print(post_data())
        elif method == '4':
            id = int(input('Enter id of the item you want to delete: '))
            print(delete_data(id))
        elif method == '5':
            id = int(input('Enter id of the item you want to update: '))
            print(update_data(id))
        elif method == '6':
            print('Program stopped')
            break
        else:
            print('Function not found')

if __name__ == '__main__':
    main()