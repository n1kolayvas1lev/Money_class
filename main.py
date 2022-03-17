from __future__ import annotations
from typing import Optional, Any, Union

from cbrf_requester import rates_parser


class Money:
    """
    По умолчанию используется российский рубль.
    """
    currencies_dict = {}
    list_of_currencies = []

    def __init__(self, value: Optional[int] = None, currency: Optional[str] = 'RUR'):
        self.value = value
        self.currency = currency

    @staticmethod
    def __show_me_your_money() -> None:
        print('Выберите валюту для конвертации.')
        for item in Money.list_of_currencies:
            print(item)

    @classmethod
    def update_course(cls) -> None:
        """
        Функция обновления курса и списка валют.
        :return: None
        """
        overwhelming_power = rates_parser()
        cls.currencies_dict = overwhelming_power[0]
        cls.list_of_currencies = overwhelming_power[1]

    def convert_rur_to_usd(self):
        """
        Конвертирует рубли в USD.
        :return: None
        """
        if self.currency.upper() == 'RUR':
            self.currency = 'USD'
            self.value /= Money.currencies_dict['USD']
        else:
            raise ValueError('Это нельзя превратить в доллары.')

    def convert_to_rur(self) -> None:
        """
        Может сконвертировать НЕ рублёвый экземпляр класса Money в рублёвый,
        если международный код присутствует в списке конвертируемых валют.
        :return: None
        """
        if self.currency.upper() != 'RUR' and self.currency.upper() in Money.currencies_dict:
            self.value *= Money.currencies_dict[self.currency.upper()]
            self.currency = 'RUR'
        else:
            raise ValueError('Что-то пошло не так.')

    def convert_rur_to_currency(self) -> None:
        """
        Преобразует рубли в выбранную валюту.
        :return: None
        """
        self.__show_me_your_money()
        while True:
            value = str.upper(input('Трёхбуквенный международный код: '))
            print(value)
            if value in Money.currencies_dict:
                self.currency = value
                self.value /= Money.currencies_dict[value]
                break
            else:
                print('Ошибка в коде или код не существует.')
                continue

    def universal_conversion(self) -> None:
        """
        Универсальный конвертер для валюты в валюту, основываясь на курсе рубля.
        :return: None
        """
        print(f'Вы конвертируете {self.value/100} {self.currency}.')
        self.__show_me_your_money()
        while True:
            value = str.upper(input('Трёхбуквенный международный код: '))
            print(value)
            if value in Money.currencies_dict and value != self.currency:
                self.value *= Money.currencies_dict[self.currency.upper()]
                self.value /= Money.currencies_dict[value]
                self.currency = value
                break
            else:
                print('Ошибка в коде или код не существует.')
                continue

    def __check_type_addition_subtraction_comparison(self, other: Any) -> bool:
        """
        Проверка типа и наименования валюты для сравнения и сложения экземпляров класса Money.
        :param other: class Money
        :return: bool
        """
        if type(other) == Money and self.currency == other.currency:
            return True
        else:
            raise TypeError('Можно осуществлять операции только с объектом "Money" с совпадающей валютой.')

    @staticmethod
    def __check_type_multiplication_division(other: Union[int, float]) -> bool:
        """
        Проверка типа переменной для умножения и деления.
        :param other: Union[int, float]
        :return: bool
        """
        if type(other) == int or type(other) == float:
            return True
        else:
            raise TypeError('Вы хотите сделать нечто необычное. Делить и умножать деньги можно только на число.')

    def __add__(self, other) -> Money:
        if self.__check_type_addition_subtraction_comparison(other):
            self.value = self.value + other.value
        return Money(self.value, self.currency)

    def __sub__(self, other) -> Money:
        if self.__check_type_addition_subtraction_comparison(other):
            self.value = self.value - other.value
        return Money(self.value, self.currency)

    def __iadd__(self, other) -> Money:
        if self.__check_type_addition_subtraction_comparison(other):
            self.value += other.value
        return Money(self.value, self.currency)

    def __isub__(self, other) -> Money:
        if self.__check_type_addition_subtraction_comparison(other):
            self.value -= other.value
        return Money(self.value, self.currency)

    def __mul__(self, other: Union[int, float]) -> Money:
        if self.__check_type_multiplication_division(other):
            self.value = self.value * other
        return Money(self.value, self.currency)

    def __truediv__(self, other) -> Money:
        if self.__check_type_multiplication_division(other):
            self.value = self.value / other
        return Money(self.value, self.currency)

    def __imul__(self, other: Union[int, float]) -> Money:
        if self.__check_type_multiplication_division(other):
            self.value *= other
        return Money(self.value, self.currency)

    def __itruediv__(self, other) -> Money:
        if self.__check_type_multiplication_division(other):
            self.value /= other
        return Money(self.value, self.currency)

    def __lt__(self, other) -> bool:
        if self.__check_type_addition_subtraction_comparison(other):
            return self.value < other.value

    def __le__(self, other) -> bool:
        if self.__check_type_addition_subtraction_comparison(other):
            return self.value <= other.value

    def __eq__(self, other) -> bool:
        if self.__check_type_addition_subtraction_comparison(other):
            return self.value == other.value

    def __ne__(self, other) -> bool:
        if self.__check_type_addition_subtraction_comparison(other):
            return self.value != other.value

    def __gt__(self, other) -> bool:
        if self.__check_type_addition_subtraction_comparison(other):
            return self.value > other.value

    def __ge__(self, other) -> bool:
        if self.__check_type_addition_subtraction_comparison(other):
            return self.value >= other.value

    def __repr__(self) -> str:
        return f"{__class__.__name__}, {self.value}, {self.currency}"

    def __str__(self) -> str:
        return f"{self.currency} {self.value * 0.01}"


if __name__ == "__main__":
    Money.update_course()
    usd = Money(100, 'usd')
    print(usd)
    usd.universal_conversion()
    print(usd)
    # rur = Money(100000)
    # rur.convert_rur_to_currency()
    # print(rur)
    # rur.convert_to_rur()
    # rur.convert_to_usd()
    # print(rur)
    # print("rur", rur, type(rur))
    # print("usd", type(usd))
    # usd = usd + rur
    # usd += rur
    # usd = usd / 2.1
    # print(usd, type(usd))
    # print(usd == rur)

    # print(Money.currencies_dict)
    # print(Money.list_of_currencies)
