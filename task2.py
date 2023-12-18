import time

class TextAdventureGame:
    def __init__(self):
        self.player_name = ""
        self.inventory = []

    def print_slow(self, text):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.05)
        print()

    def get_player_name(self):
        self.print_slow("Welcome to the Text Adventure Game!")
        self.print_slow("What's your name?")
        self.player_name = input("> ")

    def start_game(self):
        self.get_player_name()
        self.print_slow(f"Hello, {self.player_name}! Let the adventure begin.")

        self.print_slow("You find yourself in a dark forest. There are two paths ahead.")
        choice = self.get_user_choice(["Go left", "Go right"])

        if choice == 1:
            self.path_left()
        else:
            self.path_right()

    def get_user_choice(self, options):
        self.print_slow("Choose an option:")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")

        while True:
            try:
                choice = int(input("> "))
                if 1 <= choice <= len(options):
                    return choice
                else:
                    self.print_slow("Invalid choice. Try again.")
            except ValueError:
                self.print_slow("Invalid input. Enter a number.")

    def path_left(self):
        self.print_slow("You chose the left path.")
        self.print_slow("You encounter a friendly wizard who gives you a magic potion.")
        self.inventory.append("Magic Potion")
        self.print_slow("You continue your journey.")

        self.print_slow("You reach a river. What do you want to do?")
        choice = self.get_user_choice(["Swim across", "Look for a bridge"])

        if choice == 1:
            self.game_over("You were attacked by river monsters while swimming.")
        else:
            self.print_slow("You find a hidden bridge and safely cross the river.")
            self.final_scene()

    def path_right(self):
        self.print_slow("You chose the right path.")
        self.print_slow("You stumble upon a treasure chest.")
        self.inventory.append("Gold Coins")
        self.print_slow("You continue your journey.")

        self.print_slow("You come across a cave. What do you want to do?")
        choice = self.get_user_choice(["Enter the cave", "Bypass the cave"])

        if choice == 1:
            self.game_over("You were captured by trolls inside the cave.")
        else:
            self.print_slow("You avoid the cave and move forward.")
            self.final_scene()

    def final_scene(self):
        self.print_slow("Congratulations! You have reached the end of your adventure.")
        self.print_slow("Your inventory:")
        for item in self.inventory:
            print(f"- {item}")
        self.print_slow("Thanks for playing!")

    def game_over(self, message):
        self.print_slow("Game Over!")
        self.print_slow(message)
        self.print_slow("Better luck next time.")
        exit()

if __name__ == "__main__":
    game = TextAdventureGame()
    game.start_game()
