class Luhn:
    def __init__(self, card_num):
        self.is_valid = False
        card_num = card_num.replace(' ', '')

        if len(card_num) > 1:
            try:
                digits = [int(digit) for digit in card_num]
                double_me = False
                for index, num in reversed(list(enumerate(digits))):
                    if double_me:
                        print(index, num, digits[index])
                        if digits[index] * 2 > 9:
                            digits[index] = digits[index] * 2 - 9
                        else:
                            digits[index] = digits[index] * 2
                        double_me = False
                    else:
                        double_me = True
                if sum(digits) % 10 == 0:
                    self.is_valid = True
            except ValueError:
                pass

    def valid(self):
        return self.is_valid
