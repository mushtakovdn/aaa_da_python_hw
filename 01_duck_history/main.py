from typing import Union


def get_option(options: Union[list, dict]):
    """Получение выбора из заданных опций"""
    instruction = 'Выберите: '
    for i in range(len(options) - 1):
        instruction += '{}/'
    instruction += '{}\n'

    option = ''
    while option not in options:
        option = input(instruction.format(*options))
    return option


def step3_sober_and_sad():
    """Конец истории в ситуации, когда у утки не было зонтика"""
    print('Утка грустит, потому что она вынуждена была уйти из бара.',
          'Тяжело и грустно не иметь выбора')


def step3_drunk_and_happy():
    """Конец истории в ситуации, когда утка пропила свой зонтик"""
    print('Утка выпила еще бокальчик апероля и получило то самое чувство',
          'легкого опьянения. Посчитала, что два бокала достаточно и',
          'пошла гулять по городу')


def step3_sober_and_happy():
    """Конец истории, когда утка вовремя остановилась и сохранила зонт"""
    print('Утка решила, что зонт она оставлять не хочет,',
          'поэтому не стала пить еще бокал.',
          'Но все равно вышла в хорошем расположении духа.',
          'Хорошо иметь выбор.')


def step2_common():
    """Утка в баре, начало этой части"""
    print('Барбёрд спросил у утки: "Сок или апероль?"')
    options = ['сок', 'апероль']
    option = get_option(options)
    if option == 'сок':
        print('Барбёрд: "Неправильно, это апероль".')
    print('Барбёрд налил утке бокал апероля.',
          'Утка заплатила и поняла, что денег больше нет.')
    print('Барбёрд спросил, будет ли утка еще что-нибудь')


def step2_no_umbrella():
    """утка без зонта в баре"""
    step2_common()
    print('Утка поняла, что денег нет и выпить еще бокал не получится')
    options = {'нет': False}
    _ = get_option(options)
    return step3_sober_and_sad()


def step2_umbrella():
    """утка с зонтом в баре"""
    step2_common()
    print('Утка поняла, что не смотря на отсутствие денег,',
          'можно оплатить коктейль, оставив барбёрду зонт')
    options = {'нет': False, 'повторить': True}
    option = get_option(options)
    if options[option]:
        return step3_drunk_and_happy()
    step3_sober_and_happy()


def step1():
    """Начало истории про утку. Есть зонт или нет."""
    print('Утка-маляр 🦆 решила выпить зайти в бар. \nВзять ей зонтик? ☂️')
    options = {'да': True, 'нет': False}
    option = get_option(options)
    if options[option]:
        return step2_umbrella()
    else:
        return step2_no_umbrella()


if __name__ == '__main__':
    step1()
