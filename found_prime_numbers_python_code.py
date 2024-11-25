enter_num = int(input("Введите пожалуйста число: "))
list = []
deliteli = 0
for i in range(2, enter_num):
    for j in range(2, i):
        if i % j == 0:
            deliteli = deliteli + 1
    if deliteli == 0:
        list.append(i)
    else:
        deliteli = 0

print(list)