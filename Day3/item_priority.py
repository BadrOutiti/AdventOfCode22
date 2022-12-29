import string
class ItemPriority:
    def __init__(self):
        alphabet_lower = list(string.ascii_lowercase)
        alphabet_upper = list(string.ascii_uppercase)
        self._alphabet_array = alphabet_lower + alphabet_upper

    def calculate_priority(self, letter):
        prio = 1

        for let in self._alphabet_array:
            if let == letter:
                return prio
            else:
                prio = prio + 1


