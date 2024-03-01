class Anagram:
    def __init__(self, word):
        self.word = word.lower()
        self.sorted_word = sorted(self.word)
        print("Initialized word:", self.word)
        print("Sorted word:", self.sorted_word)

    def match(self, words):
        print("Matching words:", words)
        return [word for word in words if self.is_anagram(word)]

    def is_anagram(self, word):
        if len(word) != len(self.word):
            return False
        sorted_word = sorted(word.lower())
        print("Checking if", word, "is an anagram of", self.word)
        return sorted_word == self.sorted_word


anagram = Anagram("listen")
words_to_check = ["enlist", "silent", "inlets", "orange", "listen"]
print("Anagrams:", anagram.match(words_to_check))
