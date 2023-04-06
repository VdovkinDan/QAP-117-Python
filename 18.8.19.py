quantity = int(input('Укажите необходимое количество билетов: '))
visitor = [int(input('Укажите возраст посетителя: ')) for i in range(quantity)]
count = 0
for i in visitor:
    if i < 0:
        print(' ')
        print('Неверно указан возраст: ', i )
        print('Пожалуйста, повторите ввод данных.')
        break
    if 0 <= i < 18:
        count += 1*(0)
    if 18 <= i < 25:
        count += 1*(990)
    if i >= 25:
        count += 1*(1390)
if 0 < quantity <= 3:
    print(' ')
    print('Сумма к оплате: ', count, 'рублей')
else:
    print(' ')
    print('Сумма к оплате: ', count - (count * 0.1), 'рублей (с учётом 10% скидки)')
