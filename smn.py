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
    # for nl in range(len(l)):
    #     for ln in range(len(l[nl])):
    #         if l[nl][ln] == '%':
    #             l[nl][ln].replace('%', '')
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
# levelup = [l.replace('%', '') for l in levelup]
res = worldparty(names, payday, levelup)
print(res)