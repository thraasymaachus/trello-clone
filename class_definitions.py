import uuid
import openai
import time

LLM_FINE_TUNE = "python class Model has attributes id, title, children[], & functions add_child(child), rm_child(child). class Board and List derive from Model. class Card has attributes type, title, content. Assume there is a board called my_board. Convert the following input to a single python statement that uses the provided information, without python builtins:\n"
API_KEY = "sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

class Model:
    def __init__(self, title) -> None:
        self.id = uuid.uuid4()
        self.title = title
        self.children = []
        self.activity = []

    def add_child(self, child):
        self.children.append(child)

    def rm_child(self, child):
        self.children.remove(child)

    def log_activity(self, child):
        pass

    def get_child_by_id(self, child_id):
        for child in self.children:
            if child.id == child_id:
                return child
        return None


class Board(Model):
    type = 'Board'

    def __init__(self, title) -> None:
        super().__init__(title)

class List(Model):
    type = 'List'

    def __init__(self, title) -> None:
        super().__init__(title)

class Card:
    type = 'Card'

    def __init__(self, title, content):
        self.id = uuid.uuid4()
        self.title = title
        self.content = content

class View:
    def __init__(self) -> None:
        pass

    def view_board(self, board):
        print(board.title)

        for list in board.children:
            print(list.title)

    def view_list(self, list):
        print(list.title)

        for card in list.children:
            print(card.title)

    def view_card(self, card):
        print(card.title)
        print(card.content)
        
class Presenter:
    def __init__(self) -> None:
        openai.api_key = API_KEY

    def take_input(self):
        query = input()
        instructions = self.gpt_parse(query)
        
        return instructions

    def gpt_parse(self, query):
        reply = openai.ChatCompletion.create( # Need to use ChatCompletion if using gpt-X.
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": LLM_FINE_TUNE},
                {"role": "user", "content": query},
            ],
            temperature=0
        )

        #print(reply)
        try:
            return reply['choices'][0]['message']['content']
        except:
            print(f"couldn't return output. It was type: {type(reply)}")