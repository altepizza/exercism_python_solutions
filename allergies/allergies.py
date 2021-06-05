class Allergies:

    def _get_binary_list_from(self, value):
        return [int(i) for i in bin(value)[2:]]

    def __init__(self, score):
        self.SCORES = {
            'eggs': self._get_binary_list_from(1),
            'peanuts': self._get_binary_list_from(2),
            'shellfish': self._get_binary_list_from(4),
            'strawberries': self._get_binary_list_from(8),
            'tomatoes': self._get_binary_list_from(16),
            'chocolate': self._get_binary_list_from(32),
            'pollen': self._get_binary_list_from(64),
            'cats': self._get_binary_list_from(128)
        }
        self.MY_SCORE = self._get_binary_list_from(score)

    def allergic_to(self, item):
        item_score_position = len(self.SCORES.get(item, [0]))
        if len(self.MY_SCORE) >= item_score_position:
            return bool(self.MY_SCORE[-item_score_position])
        return False

    @property
    def lst(self):
        allergies_list = []
        LIST_OF_SCORES = list(self.SCORES)
        for index, candidate in enumerate(reversed(self.MY_SCORE)):
            if candidate == 1:
                if index < len(LIST_OF_SCORES):
                    allergies_list.append(LIST_OF_SCORES[index])
        return allergies_list
