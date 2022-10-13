import json
from uuid import uuid4


def display_stock(d: dict) -> str:
    """
    Комфортно відображає інформацію про товар
    :param d: повні данні про товар
    :return: повні данні про товар
    """
    return f'{d["EAN"]}; Категорія - {d["category"]}; Назва - {d["name"]}; Колір - {d["color"]}; Розмір - {d["size"]} - {d["qty"]}шт.'


def view_index(index_name: str, index_to_view: dict, source_uid_data: dict):
    """
    Виводить на екран інформацію в зручному вигляді
    :param index_name: назва індексу
    :param index_to_view: сам індекс.
    :param source_uid_data: повні данні товару за категоріями
    :return: нічого
    """
    print(f'Відображення товару за {index_name}')
    for key, values in index_to_view.items():
        print(key)
        for uid in values:
            print(f'  {display_stock(source_uid_data[uid])}')


stock = json.load(open('stock.json', mode='r'))
uid_index = dict()
name_index = dict()
category_index = dict()
color_index = dict()
size_index = dict()


for stock_info in stock['stock']:
    stock_info['uid'] = str(uuid4())
    stock_info['EAN'] = f"{stock_info['article']}"
    uid_index[stock_info['uid']] = stock_info
    if stock_info['name'] in name_index:
        name_index[stock_info['name']].append(stock_info['uid'])
    else:
        name_index[stock_info['name']] = list()
        name_index[stock_info['name']].append(stock_info['uid'])

    if stock_info['category'] in category_index:
        category_index[stock_info['category']].append(stock_info['uid'])
    else:
        category_index[stock_info['category']] = list()
        category_index[stock_info['category']].append(stock_info['uid'])

    if stock_info['color'] in color_index:
        color_index[stock_info['color']].append(stock_info['uid'])
    else:
        color_index[stock_info['color']] = list()
        color_index[stock_info['color']].append(stock_info['uid'])

    if stock_info['size'] in size_index:
        size_index[stock_info['size']].append(stock_info['uid'])
    else:
        size_index[stock_info['size']] = list()
        size_index[stock_info['size']].append(stock_info['uid'])


while True:
    choice = input('\nВиберіть одне з 4 значень, за яким хочете відсортувати залишок товару \n1 - Назва\n2 - Категорія\n3 - Колір\n4 - Розмір\n5 - Вийти\n>>> ')
    if choice == '1':
        view_index('назвою', name_index, uid_index)
    elif choice == '2':
        view_index('категорією', category_index, uid_index)
    elif choice == '3':
        view_index('кольором', color_index, uid_index)
    elif choice == '4':
        view_index('розміром', size_index, uid_index)
    elif choice == '5':
        break
    else:
        print('Виберіть цифру від 1 до 5')






