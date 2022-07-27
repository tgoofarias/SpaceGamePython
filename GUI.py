class GUI:
    def __init__(self):
        self.buttons = ["W", "A", "S", "D", "O"]

    def directionMenu(self):
        print(f"Mover:        ^ cima({self.buttons[0]})       ")
        print(f"              |            ")
        print(f"<-esquerda({self.buttons[1]})   direita ({self.buttons[3]}) -> ")
        print(f"              |            ")
        print(f"              v baixo ({self.buttons[2]})     ")
        print(f"Escolha \"O\" para sair.")
        direction = input("Qual direção mover? ").lower()

        return direction
