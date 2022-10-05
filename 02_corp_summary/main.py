import statistics
from typing import Dict, List
import csv
import os


def parse_data_for_dep_empl_info(dataset: list) -> dict:
    """
    Парсинг сырого датасета, чтобы далее посчитать требуемые агрегации
    """
    DEP_COL_NUM = 1
    SALARY_COL_NUM = 5
    parsed_data = {}

    for row in dataset:
        cur_dep = row[DEP_COL_NUM]
        cur_salary = row[SALARY_COL_NUM]
        if cur_dep in parsed_data:
            parsed_data[cur_dep]["count"] += 1
            parsed_data[cur_dep]["salaries_list"].append(cur_salary)
        else:
            parsed_data[cur_dep] = {'count': 1, 'salaries_list': [cur_salary]}
    return dict(sorted(parsed_data.items()))


def prepare_dep_empl_info(dataset: list) -> List[List]:
    """
    Подготовка данных для отчёта по департаментам:
    название, численность, "вилка" зарплат в виде мин – макс, среднюю зарплату
    """
    parsed_data = parse_data_for_dep_empl_info(dataset)
    dep_empl_info = [
        ['Департамент', 'Численность', 'Макс ЗП', 'Мин ЗП', 'Срдн ЗП']]

    for dep_name, info in parsed_data.items():
        salaries_list = [float(s) for s in info['salaries_list']]
        cur_row = [
            dep_name, info['count'], max(salaries_list), min(salaries_list),
            round(statistics.mean(salaries_list), 2)
        ]
        dep_empl_info.append(cur_row)
    return dep_empl_info


def dump_dep_empl_info(dataset: list) -> None:
    """
    Сохраняет сводный отчёт по департаментам в csv:
    название, численность, "вилка" зарплат в виде мин – макс,
    среднюю зарплату
    """
    dep_empl_info = prepare_dep_empl_info(dataset)
    parent_path = os.path.dirname(os.path.realpath(__file__))
    output_path = os.path.join(
        parent_path, 'data_result', 'Department_Employee_Info.csv'
        )
    with open(output_path, "w") as f:
        writer = csv.writer(f)
        writer.writerows(dep_empl_info)
        print(f'Отчет выгружен в файл {output_path}\n\n\n')


def show_dep_empl_info(dataset: list) -> None:
    """
    Выводит сводный отчёт по департаментам:
    название, численность, "вилка" зарплат в виде мин – макс,
    среднюю зарплату
    """
    dep_empl_info = prepare_dep_empl_info(dataset)
    COL_WIDTH = 14  # ширина колонки
    line_between_rows = '+' + (COL_WIDTH * '-' + '+') * len(dep_empl_info[0])
    display_data = [
        ((COL_WIDTH - 1) * len(dep_empl_info) - 2) * '_',
        '|                        Сводный отчёт по департаментам' +
        '                    |',
        line_between_rows
    ]
    for row in dep_empl_info:
        row_to_str = [str(x) for x in row]
        cur_display_row = '|'
        for el in row_to_str:
            cur_display_row += (COL_WIDTH - len(el) - 1) * ' ' + el + ' |'
        display_data.extend([cur_display_row, line_between_rows])

    # вывести в консоль
    for line in display_data:
        print(line)
    print("\n\n\n")


def parse_data_for_orgstruct(dataset: list) -> Dict[str, List[str]]:
    """
    Парсит отчет о сотрудниках компании и возвращает словарь
    {'Департамент1': ['Отдел 1', ..., 'Отдел N'], ..., '': ['', ..., '']}
    """
    DEP_COL_NUM = 1
    DIVISION_COL_NUM = 2
    parsed_data = {}

    for row in dataset:
        cur_dep = row[DEP_COL_NUM]
        cur_div = row[DIVISION_COL_NUM]
        if cur_dep in parsed_data:
            cur_dep_divisions = parsed_data[cur_dep]
            if cur_div not in cur_dep_divisions:
                cur_dep_divisions.append(cur_div)
        else:
            parsed_data[cur_dep] = [cur_div]
    return dict(sorted(parsed_data.items()))


def show_org_struct(dataset: list) -> None:
    """
    Подготавливает структурированную строку с оргструктурой:
    департамент - отделы
    """
    parsed_orgstruct_data = parse_data_for_orgstruct(dataset)
    COL_WIDTH = 25  # ширина колонки
    display_data = [
        '___________________________________________________',
        '|                   ОРГСТРУКТУРА                  |',
        '|------------------------+------------------------|',
        '|      Деапартамент      |         Отдел          |',
        '+------------------------+------------------------+'
    ]
    for dep, division in parsed_orgstruct_data.items():
        for i, cur_div in enumerate(division):
            if i == 0:
                cur_str = '|' + (COL_WIDTH - len(dep) - 1) * ' ' + dep + '|'
            else:
                cur_str = '|' + (COL_WIDTH - 1) * ' ' + '|'
            cur_str += (COL_WIDTH - len(cur_div) - 1) * ' ' + cur_div + '|'
            display_data.append(cur_str)
        display_data.append('+' + ((COL_WIDTH-1) * '-' + '+') * 2)

    # вывод в консоль
    for line in display_data:
        print(line)
    print('\n\n\n')


def get_source_data() -> list:
    """
    Возвращает датасет для дальнейшей работы.
    Генерализированный доступ к файлу с датасетом (без хардкода пути).
    """
    parent_path = os.path.dirname(os.path.realpath(__file__))
    data_path = os.path.join(parent_path, 'data_src', 'Corp_Summary.csv')
    with open(data_path, 'r') as csvfile:
        data = csv.reader(csvfile, delimiter=';')
        dataset = [lst for lst in data]
    return dataset


def menu() -> None:
    """Меню и первичная загрузка файла."""
    dataset = get_source_data()[1:]
    choice = 0
    while choice not in ('q', 'Q'):
        choice = input(
            'Выберите необходимое действие:\n'
            '\t1 - Отобразить оргструктуру\n'
            '\t2 - Отобразить сводный отчет по департаментам\n'
            '\t3 - Выгрузить сводный отчет по департаментам в csv\n'
            'Выбор: '
        )
        if choice == '1':
            show_org_struct(dataset)
        elif choice == '2':
            show_dep_empl_info(dataset)
        elif choice == '3':
            dump_dep_empl_info(dataset)
        elif choice in ('q', 'Q'):
            print('Завершение работы. \nВсего доброго!')
        else:
            print('Некорректный ввод. Выберите одну из трех опций, '
                  'либо "q" для завершения работы\n')


if __name__ == '__main__':
    print('>>>\n>>>\nДобро пожаловать в программу "CORP SUMMARY"!\n')
    menu()
