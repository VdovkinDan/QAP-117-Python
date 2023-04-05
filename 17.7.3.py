per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('Введите сумму: '))
percent =list(per_cent.values())
deposit = []
for i in percent:
    percent = int((i * money) / 100)
    deposit.append(percent)
print(deposit, end="\n")
print('Максимальная сумма, которую вы можете заработать:', (max(deposit)))