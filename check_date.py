from typing import Optional
import time



class Date:
    """Класс для работы с датами"""
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

        self.is_valid_date(self.day, self.month, self.year)

    @staticmethod
    def is_leap_year(year: int):
        """Проверяет, является ли год високосным"""

        if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
            return True
        else:
            return False

    def get_max_day(self, month: int, year: int):
        """Возвращает максимальное количество дней в месяце для указанного года"""
        ...  #
        if month in [4, 6, 9, 11]:
            return 30
        elif month not in [2, 4, 6, 9, 11]:
            return 31
        elif month == 2 and self.is_leap_year(year):
            return 29
        else:
            return 28

    def is_valid_date(self, day: int, month: int, year: int):
        """Проверяет, является ли дата корректной"""
        current_time = time.localtime()
        if 0 < day <= self.get_max_day(month, year) and 0 < month <= 12 and 0 < year and (
                day <= current_time.tm_mday and month <= current_time.tm_mon and year <= current_time.tm_year):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.day}, {self.month}, {self.year}"


if __name__ == "__main__":
    date = Date(10, 11, 2020)
    print(date)
    # Write your solution here
