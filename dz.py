from inspect import signature

# 1 Напишите функцию для транспонирования матрицы

def trans(mat):
    mat = [*zip(*mat)]
    return mat

rix = [['a','b','c'],['d','e','f'],['g','h','i']]
print(f'1.\n{rix} \n{trans(rix)}')

# 2 Напишите функцию принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ- значение
# переданного аргумента, а значение - имя аргумента. 
# Если ключ не хешируем, используйте его строковое представление.

def a_gang(desc = None, **record):
    if desc == None:
        desc = dict()
    for i in record:
        desc[record[i]] = i
    return desc

print("\n2.", a_gang(leader='Hearr Icks', color='green', member= 144, allies= None, type='Anarchist raiders'))

# 3 Возьмите задачу о банкомате из семинара 2. 
# Разбейте её на отдельные операции - функции. 
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

def op1(sum, money, perc3, round, *percs12):
    sum -= perc3
    sum += abs(money)
    print("Вы пополнили ваш счёт на\n:", money, "кредитов.\nВаш счёт теперь составляет\n:", sum, "кредитов.")
    round += 1
    if round % 3 == 0:
        sum += sum * percs12[0]

def op2(sum, money, perc3, round, *percs12):
    sum -= perc3
    procent = abs(money) * percs12[0]
    sum -= abs(money) + procent
    print("Вы сняли со счёта сумму в размере\n:", money, "кредитов.\nВаш счёт теперь составляет\n:", sum, "кредитов.\nС учётом ставки в 1.5% процентов, с вашего счёта также было снято\n:", procent, "кредитов.")
    round += 1
    if round % 3 == 0:
        sum += sum * percs12[1]

print("\n3.")
sum = 0
compute = True
round = 0
while (compute):
    if sum > 5000000:
        perc3 = 10 / 100
        print("Учитывается налог на богатство в 10%.")
    else:
        perc3 = 0
    move = input("Выберите желаемое действие:\n(1) Пополнить баланс\n(2) Снять сумму\n(3) Показать счёт\n(q) Выйти\n: ")
    if move == "1":
        money = int(input("Введите желаемую сумму\n: "))
        if money % 50 == 0:
            print(op1(sum, money, round, perc2 = 3 / 100))
        else:
            sum -= perc3
            print("Операция не была проведена. Сумма должна быть кратна 50.\nВаш счёт составляет\n:", sum, "кредитов.")
    elif move == "2":
        money = int(input("Введите желаемую сумму\n: "))
        if money % 50 == 0 and money <= sum:
            print(op2(sum, money, round, perc1 = 1.5 / 100, perc2 = 3 / 100))
        else:
            sum -= perc3()
            print("Операция не была проведена. Сумма должна быть кратна 50.\nВаш счёт составляет\n:", sum, "кредитов.")
    elif move == "3":
        print("Ваш счёт составляет\n:", sum, "кредитов.")
    elif move == "q":
        print("\nДо свидания.")
        compute = False
