def maskify(cc):
    if len(cc) > 4:
        return '#' * (len(cc) - 4) + cc[-4:]
    else:
        return cc


print(maskify(input('Введите номер Вашей карты: ')))
