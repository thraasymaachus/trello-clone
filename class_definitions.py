class Model:
    def __init__(self, title) -> None:
        self.title = title
        self.children = []
        self.activity = [] # Historical activities associated with the object

    def add_child(self, child):
        self.children.append(child)

    def rm_child(self, child):
        self.children.remove(child)

    def log_activity(self, child):
        pass


class Board(Model):
    type = 'Board'

    def __init__(self, title) -> None:
        super().__init__(title)


class List(Board):
    type = 'List'

    def __init__(self, title) -> None:
        super().__init__(title)


class Card:
    def __init__(self, title, content):
        self.title = title
        self.content = content


class View:
    def __init__(self) -> None:
        pass

    def view_board(self, board):
        print(board.title)
        print("Show Board")

    def view_list(self, list):
        print(list.title)
        print("Show List")

    def view_card(self, card):
        print(card.title)
        print("Show Card")
        

class Presenter:
    def __init__(self) -> None:
        pass

    def take_input(self):
        query = input()
        instructions = self.gpt_parse(query)
        
        return instructions

    def gpt_parse(self, query):
        pass