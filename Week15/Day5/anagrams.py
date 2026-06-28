from anagram_checker import AnagramChecker


def show_menu():
    print()
    print("===== Anagram Checker =====")
    print("1. Enter a word")
    print("2. Exit")


def validate_user_input(user_input):
    user_input = user_input.strip()

    if " " in user_input:
        print("Error: please enter only one word.")
        return None

    if not user_input.isalpha():
        print("Error: please enter letters only.")
        return None

    return user_input.lower()


def main():
    checker = AnagramChecker("words.txt")

    while True:
        show_menu()

        choice = input("Choose an option: ")

        if choice == "2":
            print("Goodbye!")
            break

        elif choice == "1":
            user_word = input("Enter a word: ")
            valid_word = validate_user_input(user_word)

            if valid_word is None:
                continue

            print()
            print(f'YOUR WORD: "{valid_word.upper()}"')

            if checker.is_valid_word(valid_word):
                print("This is a valid English word.")

                anagrams = checker.get_anagrams(valid_word)

                if len(anagrams) > 0:
                    print("Anagrams for your word:", ", ".join(anagrams))
                else:
                    print("No anagrams found for your word.")
            else:
                print("This is not a valid English word.")

        else:
            print("Invalid choice. Please choose 1 or 2.")


main()