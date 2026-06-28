import string
import re


# ============================================================
# Daily Challenge : Text Analysis
# ============================================================

class Text:
    def __init__(self, text):
        self.text = text

    def word_frequency(self, word):
        words = self.text.lower().split()
        word = word.lower()

        count = words.count(word)

        if count == 0:
            return None

        return count

    def most_common_word(self):
        words = self.text.lower().split()

        word_count = {}

        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

        most_common = max(word_count, key=word_count.get)

        return most_common

    def unique_words(self):
        words = self.text.lower().split()
        unique = list(set(words))

        return unique

    @classmethod
    def from_file(cls, file_path):
        with open(file_path, "r") as file:
            content = file.read()

        return cls(content)


# ============================================================
# Bonus : Text Modification
# ============================================================

class TextModification(Text):
    def remove_punctuation(self):
        modified_text = ""

        for char in self.text:
            if char not in string.punctuation:
                modified_text += char

        return modified_text

    def remove_stop_words(self):
        stop_words = [
            "a", "an", "the", "is", "are", "am", "in", "on", "at",
            "to", "for", "of", "and", "or", "but", "with", "this",
            "that", "it", "as", "be", "by", "from"
        ]

        words = self.text.lower().split()
        filtered_words = []

        for word in words:
            clean_word = word.strip(string.punctuation)

            if clean_word not in stop_words:
                filtered_words.append(word)

        return " ".join(filtered_words)

    def remove_special_characters(self):
        modified_text = re.sub(r"[^A-Za-z0-9\s]", "", self.text)

        return modified_text


# ============================================================
# Test the code
# ============================================================

sample_text = """
Hello world! Hello Python.
Python is amazing, and the world of code is beautiful.
This is a simple text for text analysis.
"""

print("===== Part 1 : Analyzing a Simple String =====")

text = Text(sample_text)

print("Word frequency of 'hello':")
print(text.word_frequency("hello"))

print()

print("Most common word:")
print(text.most_common_word())

print()

print("Unique words:")
print(text.unique_words())

print()


# ============================================================
# Test from file
# ============================================================

print("===== Part 2 : Analyzing Text from a File =====")

with open("sample_text.txt", "w") as file:
    file.write(sample_text)

text_from_file = Text.from_file("sample_text.txt")

print("Most common word from file:")
print(text_from_file.most_common_word())

print()


# ============================================================
# Test Text Modification
# ============================================================

print("===== Bonus : Text Modification =====")

modified_text = TextModification(sample_text)

print("Text without punctuation:")
print(modified_text.remove_punctuation())

print()

print("Text without stop words:")
print(modified_text.remove_stop_words())

print()

print("Text without special characters:")
print(modified_text.remove_special_characters())
