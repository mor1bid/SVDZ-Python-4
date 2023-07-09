import random

# 1
def newstr(text, nid):
    for l in text.split():
        nid += 1
        print(f'{nid}. {l}')

nid = 0
text = input("1. Здравствуйте. Введите желаемый текст\n: ")
print("\nРезультат:")
newstr(text, nid)

# 2
def codunic(text, data = None):
    if data == None:
        data = list()
    for l in text:
        data.append(ord(l))
    return data

text = list(input("\n2. Введите желаемый текст\n: "))
res = sorted(codunic(text), reverse=True)
print(res)

# 3
def unidi(unter, uber, data = None):
    if data == None:
        data = dict()
    for i in range(unter, uber + 1):
        data[chr(i)] = i
    return data

digs = input("\n3. Введите два числа через пробел\n: ").split()
digs = sorted(digs)
res = unidi(int(digs[0]), int(digs[len(digs) - 1]))
print(res)

# 4
def digsort(digs):
    for i in range(len(digs)):
        for j in range(len(digs)):
            if digs[i] > digs[j]:
                temp = digs[j]
                digs[j] = digs[i]
                digs[i] = temp
    return digs

digs = [4, 8, 15, 16, 23, 42]
digs = input("\n4. Введите два числа через пробел\n: ").split()
res = digsort(digs)
print(res)

# 5
print("\n5. ")
def worldparty(n, p, l, fin = None):
    l = [l.replace('%', '') for l in levelup]
    print(l)
    if fin == None:
        fin = dict()
    for i in range(len(payday)):
        fin[n[i]] = p[i] * (float(l[i]) / 100)
    return fin

names = ["Agent Dennis", "Killing Spree", "Hearr Icks", "Puppet Master", "Jake El"]
payday = [500, 1000, 200, 360, 800]
levelup = ["10.17%", "17.03%", "100.0%", "6.66%", "13.07%"]
res = worldparty(names, payday, levelup)
print(res)

# 6
def aplusi(ar, ray, ind, dex):
    if ind > dex:
        temp = dex
        dex = ind
        ind = temp
    if ind < -len(ar):
        ind = 0
    if dex > len(ar):
        dex = len(ar)
    for i in range (ind, dex):
        print(f"{ar[i]} + {ray[i]} = {ar[i] + ray[i]}")

ar = [1, 3, 7, 15]
ray = [2, 6, 14, 22]
ind = int(input(f"6. Введите последовательно первый и второй индексы (от {-len(ar)} до {len(ar)})\n: "))
dex = int(input(": "))
if ind != dex:
    aplusi(ar, ray, ind, dex)
else:
    print("\nа где")

# 7
print("\n7. ")
def stock(b):
    check = True
    for i in b:
        bank = 0
        st = 0
        nst = 0
        for j in range(len(b[i])):
            if b[i][j] % 2 == 0:
                st += b[i][j]
            else:
                nst += b[i][j]
        bank = st - nst
        print(f'\n{i} имеют:\nДоходы в размере {st} кредитов\nРасходы в размере {nst} кредитов\nПрибыль в размере {bank} кредитов')
        if bank < 0:
            check = False
    return check

business = {
    'Team 17': [random.randint(500, 1000), random.randint(500, 1000), random.randint(500, 1000), random.randint(500, 1000), random.randint(500, 1000)], 
    'COMRA': [random.randint(500, 1000), random.randint(500, 1000), random.randint(500, 1000), random.randint(500, 1000), random.randint(500, 1000)],
    'A-B06M24 Gang': [random.randint(500, 1000), random.randint(500, 1000), random.randint(500, 1000), random.randint(500, 1000), random.randint(500, 1000)],
    'Hellbound Razers': [random.randint(500, 1000), random.randint(500, 1000), random.randint(500, 1000), random.randint(500, 1000), random.randint(500, 1000)],
    'The Blues Hood': [random.randint(500, 1000), random.randint(500, 1000), random.randint(500, 1000), random.randint(500, 1000), random.randint(500, 1000)]
}
res = stock(business)
print("\nВсе бизнесы прибыльны?\n", res)

# 8
print("\n8. ")
def armageddon(team):
    for name in range(len(team)):
        if 's' in team[name][len(team[name]) - 1]:
            team[name] = None
    return team

team = ["Agent Dennis", "Spadge", "Boggy B", "Dr. Awesome", "Chicken Legs", "Tapper", "Andy D", "Seventies Babe"]
print(team)
res = armageddon(team)
print(res)