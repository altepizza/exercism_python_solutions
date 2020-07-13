class Luhn:

    def __init__(self, card_num):
        self.is_valid = Luhn._check_card_num(card_num)

    def valid(self):
        return self.is_valid

    @staticmethod
    def _check_card_num(card_num):
        card_num = card_num.replace(' ', '')
        if len(card_num) > 1:
            try:
                digits = [int(digit) for digit in card_num]
            except ValueError:
                return False
            digits.reverse()
            for index, number in enumerate(digits):
                if index % 2 > 0:
                    if number * 2 > 9:
                        digits[index] = number * 2 - 9
                    else:
                        digits[index] = number * 2
            if sum(digits) % 10 == 0:
                return True
        return False
