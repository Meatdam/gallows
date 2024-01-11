class Hangman:
    """
    содержит висильника, состояние победы по умолчанию False,
    board щифрование слова, по умаолчаню None
    """
    def __init__(self, wrong, board=None, win=False, stages=None):
        self.wrong = wrong
        self.stages = ["",
                       "________                ",
                       "|                       ",
                       "|          |            ",
                       "|          O            ",
                       "|         /|\           ",
                       "|         / \           ",
                       "|                       "
                       ]
        self.board = ["____"]
        self.win = win

    def __repr__(self):
        return f"Возвращаю: {self.wrong}"
