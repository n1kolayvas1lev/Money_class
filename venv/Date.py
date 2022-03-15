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

        if 0 < day <= self.get_max_day(month, year) or 0 > month > 12 or 0 > year:
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.day}, {self.month}, {self.year}"


if __name__ == "__main__":
    date = Date(10, 11, 2020)
    print(date.is_valid_date(10, 11, 2020))
    # Write your solution here
