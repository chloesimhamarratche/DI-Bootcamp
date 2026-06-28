class AnagramChecker:
    def __init__(self, file_path):
        with open(file_path, "r") as file:
            words = file.read().splitlines()

        self.word_list = []

        for word in words:
            self.word_list.append(word.lower())

    def is_valid_word(self, word):
        word = word.lower()
        return word in self.word_list

    def is_anagram(self, word1, word2):
        word1 = word1.lower()
        word2 = word2.lower()

        return sorted(word1) == sorted(word2) and word1 != word2

    def get_anagrams(self, word):
        word = word.lower()
        anagrams = []

        for current_word in self.word_list:
            if self.is_anagram(word, current_word):
                anagrams.append(current_word)

        return anagrams