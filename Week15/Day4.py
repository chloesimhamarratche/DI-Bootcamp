import random
import json


# ============================================================
# Exercise 1 : Random Sentence Generator
# ============================================================

def get_words_from_file(file_path):
    with open(file_path, "r") as file:
        content = file.read()

    words = content.split()
    return words


def create_words_file():
    words = [
        "hello", "world", "python", "developer", "school",
        "student", "computer", "code", "happy", "beautiful",
        "random", "sentence", "project", "learning", "future",
        "israel", "friend", "family", "music", "coffee"
    ]

    with open("words.txt", "w") as file:
        for word in words:
            file.write(word + "\n")


def get_random_sentence(length):
    words = get_words_from_file("words.txt")
    random_words = random.choices(words, k=length)
    sentence = " ".join(random_words).lower()
    return sentence


def random_sentence_main():
    print("===== Exercise 1 : Random Sentence Generator =====")
    print("This program generates a random sentence.")
    print("Choose a sentence length between 2 and 20 words.")

    create_words_file()

    try:
        user_input = input("Enter the sentence length: ")
        length = int(user_input)

        if length < 2 or length > 20:
            print("Error: the number must be between 2 and 20.")
            return

        sentence = get_random_sentence(length)
        print(sentence)

    except ValueError:
        print("Error: please enter a valid number.")


# ============================================================
# Exercise 2 : Working with JSON
# ============================================================

def json_exercise():
    print()
    print("===== Exercise 2 : Working with JSON =====")

    sample_json = """
    {
        "company": {
            "employee": {
                "name": "Emma",
                "payable": {
                    "salary": 7000,
                    "bonus": 800
                }
            }
        }
    }
    """

    data = json.loads(sample_json)

    salary = data["company"]["employee"]["payable"]["salary"]
    print("Salary:", salary)

    data["company"]["employee"]["birth_date"] = "2003-12-25"

    with open("modif_sample.json", "w") as file:
        json.dump(data, file, indent=4)

    print("JSON file saved successfully.")


# ============================================================
# Run everything
# ============================================================

random_sentence_main()
json_exercise()
