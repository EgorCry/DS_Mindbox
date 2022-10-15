def count_c(number):
    """
    Функция подсчитывает сумму цифр в числе и возвращает целочисленное значение.
    """
    nswr = 0
    while number > 0:
        nswr += number % 10
        number //= 10
    return nswr


def zero_id(n_customers):
    """
    Функция получает на вход количество клиентов, на выход предоставляя словарь с ключами из номера группы и 
    значениями из количества людей в ней.
    """
    nswr = {}
    cust_id = 0
    for i in range(n_customers):
        number = count_c(cust_id)
        if number not in nswr:
            nswr[number] = 0
        nswr[number] += 1
        cust_id += 1
    return nswr


def custom_id(n_customers, n_first_id):
    """
    Функция получает на вход количество клиентов и id первого клиента, 
    на выход предоставляя словарь с ключами из номера группы и значениями из количества людей в ней.
    """
    nswr = {}
    cust_id = n_first_id
    for i in range(n_customers):
        number = count_c(cust_id)
        if number not in nswr:
            nswr[number] = 0
        nswr[number] += 1
        cust_id += 1
    return nswr


if __name__ == '__main__':
    n_customers = int(input('Введите количество клиентов для первой функции: '))
    nswr = zero_id(n_customers)
    print(nswr, '\n')

    n_customers = int(input('Введите количество клиентов для второй функции: '))
    n_first_id = int(input('Введите первый id клиента в последовательности: '))
    nswr = custom_id(n_customers, n_first_id)
    print(nswr, '\n')
