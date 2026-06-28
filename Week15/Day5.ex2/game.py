import random


class Game:
    def get_user_item(self):
        valid_items = ["rock", "paper", "scissors"]

        while True:
            user_item = input("Choose rock, paper or scissors: ").lower().strip()

            if user_item in valid_items:
                return user_item

            print("Invalid choice. Please choose rock, paper or scissors.")

    def get_computer_item(self):
        valid_items = ["rock", "paper", "scissors"]
        return random.choice(valid_items)

    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return "draw"

        if user_item == "rock" and computer_item == "scissors":
            return "win"

        if user_item == "paper" and computer_item == "rock":
            return "win"

        if user_item == "scissors" and computer_item == "paper":
            return "win"

        return "loss"

    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)

        print()
        print(f"You selected: {user_item}")
        print(f"The computer selected: {computer_item}")
        print(f"You {result}!")

        return result
