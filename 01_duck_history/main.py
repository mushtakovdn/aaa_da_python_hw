def step2_no_umbrella():
    pass


def step2_umbrella():
    pass


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


if __name__ == "__main__":
    step1()
