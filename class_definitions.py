import uuid
import openai
import time

# Define a constant for language model fine tuning
LLM_FINE_TUNE = {
    "base": "python class Model has attributes id, title, children[], & functions add_child(child), rm_child(child). class Board and List derive from Model. class Card has attributes type, title, content. Assume there is a board called my_board. Convert the following input to a single python statement that uses the provided information, without python builtins:\n",
    "verbose": "python class Model has attributes id, title, children[], & functions add_child(child), rm_child(child), get_child_by_title(title). class Board and List derive from Model. class Card has attributes type, title, content. class view has functions view_board(board), view_list(list), & view_card(card), each of which displays the content of a Board, List, or Card nicely. Assume there is a board called my_board. No justification of your response is required. Using the provided information and no python builtins, convert any input the user gives you into a single line of python code, preceded by nothing, and followed by nothing",
}
INITIALIZER = "verbose"

# Set the API key. Find yours here (https://platform.openai.com/account/api-keys)
API_KEY = "sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

# Define a base class for the kanban objects, with a unique id, title, and list of children
class Model:
    def __init__(self, title) -> None:
        self.id = uuid.uuid4()
        self.title = title
        self.children = []
        self.activity = []

   # Add a child object to the children list
    def add_child(self, child):
        self.children.append(child)

    # Remove a child object from the children list
    def rm_child(self, child):
        self.children.remove(child)

    # Placeholder for logging activity
    def log_activity(self, child):
        pass

    # Get a child object by its title
    def get_child_by_title(self, title):
        for child in self.children:
            if child.title == title:
                return child
        return None

    # Get a child object by its id
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

# Define a View class for displaying Board, List, and Card objects
class View:
    def __init__(self) -> None:
        pass

    # Display a board's title and its children's titles (lists)
    def view_board(self, board):
        print(board.title)

        for list in board.children:
            print(list.title)

    # Display a list's title and its children's titles (cards)
    def view_list(self, list):
        print(list.title)

        for card in list.children:
            print(card.title)

    # Display a card's title and content
    def view_card(self, card):
        print(card.title)
        print(card.content)
        
# Define a Presenter class for handling user input and parsing it using GPT-3.5-turbo or equivalent
class Presenter:
    def __init__(self) -> None:
        openai.api_key = API_KEY

    def take_input(self):
        query = input()
        instructions = self.gpt_parse(query)
        
        return instructions

    def gpt_parse(self, query):
        reply = openai.ChatCompletion.create( # Need to use ChatCompletion if using GPT-X.
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": LLM_FINE_TUNE[INITIALIZER]},
                {"role": "user", "content": query},
            ],
            temperature=0
        )

        print(reply)
        try:
            return reply['choices'][0]['message']['content']
        except:
            print(f"couldn't return output. It was type: {type(reply)}")