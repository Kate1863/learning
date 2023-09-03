login=input("Введите Ваш логин: ")
def wrapper_decorator(login):
        # Do something before
    if login=='Vasia':
            print('На вашем счёте: 10$')
        # Do something after
    if login!='Vasia':
            print('Доступ запрещён')
    return wrapper_decorator
wrapper_decorator(login)