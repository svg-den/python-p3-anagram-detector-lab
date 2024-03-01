class Anagram:
    def __init__(self, word):
        self.word = word.lower()
        self.sorted_word = sorted(self.word)

    def match(self, words):
        return [word for word in words if self.is_anagram(word)]

    def is_anagram(self, word):
        if len(word) != len(self.word):
            return False
        return sorted(word.lower()) == self.sorted_word
