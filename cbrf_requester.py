import requests
from check_date import Date
import xml.etree.ElementTree as ET


def current_day_request() -> None:
    """
    Запрос курсов валют с сайта ЦБ (cbr.ru) на текущую дату, если банковский день ещё не окончен
    или на следующий банковский день. Запрос сохраняется в rates.xml.
    :return: None
    """
    cbr_today_currency_rates = 'https://www.cbr.ru/scripts/XML_daily.asp'
    today_rates = requests.get(cbr_today_currency_rates)
    with open('rates.xml', 'wb') as f:
        f.write(today_rates.content)


def custom_day_request() -> None:
    """
    Запрос курсов на произвольную дату до текущего банковского дня.
    :return: None
    """
    print('Введите дату, для которой запрашиваются курсы валют.')
    print('=' * 60)
    custom_date = None
    while True:
        day = int(input('Введите день в формате "дд": '))
        month = int(input('Введите месяц в формате "мм": '))
        year = int(input('Введите год в формате "гггг": '))
        date = Date(day, month, year)
        if date.is_valid_date(day=day, month=month, year=year):
            custom_date = str(f"{day}/{month}/{year}")
            break
        else:
            print('Некорректная дата.')
            continue
    cbr_custom_currency_rates = requests.get(f'https://www.cbr.ru/scripts/XML_daily.asp?date_req={custom_date}')
    with open('custom_rates.xml', 'wb') as f:
        f.write(cbr_custom_currency_rates.content)


def rates_parser() -> tuple[dict[str | None, float], list[str]]:
    """
    Парсер загруженного файла с курсами валюты. Возвращает:
    1. Человекочитаемое представление курса на запрошенную дату.
    2. Словарь с парой {международное краткое наименование валюты/стоимость единицы валюты в рублях}.
    :return: tuple[dict[str | None, float], list[str]]
    """
    source = None
    while True:
        print()
        command = int(input('Выберите день для получения курса валюты. 1 - сегодня, 2 - день по выбору, '
                            '3 - ничего не обновлять, использовать старый файл с данными: '))
        if command == 1:
            current_day_request()
            source = 'rates.xml'
            break
        elif command == 2:
            custom_day_request()
            source = 'custom_rates.xml'
            break
        elif command == 3:
            source = 'rates.xml'
            break
        else:
            continue

    tree = ET.parse(source)
    root = tree.getroot()
    print(f"Курсы валют на дату: {root.get('Date')}")
    currencies_dict = {}  # Словарь {<CharCode>: курс 1/1}.
    list_of_charcodes = []  # Список кратких наименований валюты. <CharCode>
    list_of_names = []  # Список полных наименований валюты. <Name>
    list_of_currencies = []  # Текстовый список <Name>, <CharCode> с действительными ценниками для человекочитаемого вывода.
    list_of_nominals = []  # Список кратностей для валюты. Цены могут быть указаны > чем за 1 единицу. <Nominal>
    list_of_courses = []  # Список цен валют как в файле. <Value>

    for char_code in root.findall('Valute/CharCode'):
        list_of_charcodes.append(char_code.text)
    for name in root.findall('Valute/Name'):
        list_of_names.append(name.text)
    for nominal in root.findall('Valute/Nominal'):
        list_of_nominals.append(float(nominal.text.replace(',', '.')))
    for course in root.findall('Valute/Value'):
        list_of_courses.append(float(course.text.replace(',', '.')))

    for i in range(len(list_of_charcodes)):
        currencies_dict[list_of_charcodes[i]] = list_of_courses[i]/list_of_nominals[i]
    for item in range(len(list_of_charcodes)):
        list_of_currencies.append(f'{list_of_charcodes[item]} - '
                                  f'1(один) {list_of_names[item]} - '
                                  f'{currencies_dict[list_of_charcodes[item]]} RUR')
    return currencies_dict, list_of_currencies


if __name__ == '__main__':
    # custom_day_request()
    # current_day_request()
    rates_parser()
