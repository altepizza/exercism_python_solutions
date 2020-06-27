class Luhn:

    def _check_card_num(self, card_num):
        self.is_valid = False

        card_num = card_num.replace(' ', '')
        if len(card_num) > 1:
            try:
                digits = [int(digit) for digit in card_num]
            except ValueError:
                return False
            double_me = False
            for index, num in reversed(list(enumerate(digits))):
                if double_me:
                    if num * 2 > 9:
                        digits[index] = num * 2 - 9
                    else:
                        digits[index] = num * 2
                    double_me = False
                else:
                    double_me = True
            if sum(digits) % 10 == 0:
                return True
        return False

    def __init__(self, card_num):
        self.is_valid = self._check_card_num(card_num)

    def valid(self):
        return self.is_valid
