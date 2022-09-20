def add_menu_item_return(menu):
    new_item = input('Введите название нового элемента: ')
    new_item_price = input('Введите его цену: ')
    # menu = menu + '\n' + new_item + ' ' + new_item_price
    menu += '\n' + new_item + ' ' + new_item_price
    # menu = menu + f'\n {new_item} {new_item_price}'
    return menu
print(add_menu_item_return())