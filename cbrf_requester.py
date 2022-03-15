import requests
from check_date import Date


def current_day_request():
    cbr_today_currency_rates = 'https://www.cbr.ru/scripts/XML_daily.asp'
    today_rates = requests.get(cbr_today_currency_rates)
    with open('rates.xml', 'wb') as f:
        f.write(today_rates.content)


def custom_day_request():
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
    # print(cbr_custom_currency_rates)


if __name__ == '__main__':
    custom_day_request()
