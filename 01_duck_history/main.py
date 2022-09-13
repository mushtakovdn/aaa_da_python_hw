def step3_sober_and_sad():
    print('Утка грустит, потому что она вынуждена была уйти из бара.',
          'Тяжело и грустно не иметь выбора')


def step3_drunk_and_happy():
    print('Утка выпила еще бокальчик апероля и получило то самое чувство',
          'легкого опьянения. Посчитала, что два бокала достаточно и',
          'пошла гулять по городу')


def step3_sober_and_happy():
    print('Утка решила, что зонт она оставлять не хочет,',
          'поэтому не стала пить еще бокал.',
          'Но все равно вышла в хорошем расположении духа.',
          'Хорошо иметь выбор.')


def step2_common():
    print('Барбёрд спросил у утки: "Сок или апероль?"')
    option = ''
    options = ['сок', 'апероль']
    while option not in options:
        option = input('Выберите: {}/{}\n'.format(*options))
    if option == 'сок':
        print('Барбёрд: "Неправильно, это апероль".')
    print('Барбёрд налил утке бокал апероля.',
          'Утка заплатила и поняла, что денег больше нет.')
    print('Барбёрд спросил, будет ли утка еще что-нибудь')


def step2_no_umbrella():
    step2_common()
    print('Утка поняла, что денег нет и выпить еще бокал не получится')
    option = ''
    options = {'нет': False}
    while option not in options:
        option = input('Выберите: {}\n'.format(*options))
    return step3_sober_and_sad()


def step2_umbrella():
    step2_common()
    print('Утка поняла, что не смотря на отсутствие денег,',
          'можно оплатить коктейль, оставив барбёрду зонт')
    option = ''
    options = {'нет': False, 'повторить': True}
    while option not in options:
        option = input('Выберите: {}/{}\n'.format(*options))
    if options[option]:
        return step3_drunk_and_happy()
    step3_sober_and_happy()


def step1():
    print('Утка-маляр 🦆 решила выпить зайти в бар. \nВзять ей зонтик? ☂️')
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    if options[option]:
        return step2_umbrella()
    else:
        return step2_no_umbrella()


if __name__ == '__main__':
    step1()
