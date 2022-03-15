from typing import Optional, Any, Union
from cbrf_requester import custom_day_request, current_day_request


class Money:
    def __init__(self, value: Optional[int] = None, currency: Optional[str] = None):
        self.value = value
        self.currency = currency

    def check_type_addition_subtraction_comparison(self, other: Any) -> bool:
        if type(other) == Money and self.currency == other.currency:
            return True
        else:
            raise TypeError('Можно осуществлять операции только с объектом "Money" с совпадающей валютой.')

    def check_type_multiplication_division(self, other: Union[int, float]) -> bool:
        if type(other) == int or type(other) == float:
            return True
        else:
            raise TypeError('Вы хотите сделать нечто необычное. Делить и умножать деньги можно только на число.')

    def __add__(self, other):
        if self.check_type_addition_subtraction_comparison(other):
            self.value = self.value + other.value
        return Money(self.value, self.currency)

    def __sub__(self, other):
        if self.check_type_addition_subtraction_comparison(other):
            self.value = self.value - other.value
        return Money(self.value, self.currency)

    def __iadd__(self, other):
        if self.check_type_addition_subtraction_comparison(other):
            self.value += other.value
        return Money(self.value, self.currency)

    def __isub__(self, other):
        if self.check_type_addition_subtraction_comparison(other):
            self.value -= other.value
        return Money(self.value, self.currency)

    def __mul__(self, other: Union[int, float]):
        if self.check_type_multiplication_division(other):
            self.value = self.value * other
        return Money(self.value, self.currency)

    def __truediv__(self, other):
        if self.check_type_multiplication_division(other):
            self.value = self.value / other
        return Money(self.value, self.currency)

    def __imul__(self, other: Union[int, float]):
        if self.check_type_multiplication_division(other):
            self.value *= other
        return Money(self.value, self.currency)

    def __itruediv__(self, other):
        if self.check_type_multiplication_division(other):
            self.value /= other
        return Money(self.value, self.currency)

    def __lt__(self, other) -> bool:
        if self.check_type_addition_subtraction_comparison(other):
            return self.value < other.value

    def __le__(self, other) -> bool:
        if self.check_type_addition_subtraction_comparison(other):
            return self.value <= other.value

    def __eq__(self, other) -> bool:
        if self.check_type_addition_subtraction_comparison(other):
            return self.value == other.value

    def __ne__(self, other) -> bool:
        if self.check_type_addition_subtraction_comparison(other):
            return self.value != other.value

    def __gt__(self, other) -> bool:
        if self.check_type_addition_subtraction_comparison(other):
            return self.value > other.value

    def __ge__(self, other) -> bool:
        if self.check_type_addition_subtraction_comparison(other):
            return self.value >= other.value

    def convert_to_usd(self):
        ...

    def convert_to_currency(self):
        ...

    def __repr__(self) -> str:
        return f"{__class__.__name__}, {self.value}, {self.currency}"

    def __str__(self) -> str:
        return f"{self.currency} {self.value * 0.01}"


if __name__ == "__main__":
    usd = Money(312, 'usd')
    rur = Money(510, 'usd')
    print("rur", rur, type(rur))
    print("usd", type(usd))
    # usd = usd + rur
    # usd += rur
    # usd = usd / 2.1
    # print(usd, type(usd))
    print(usd == rur)
