from class_definitions import *
import sys


# Helper functions
def retrieveKey():
    return open(".config", "r").readline()

# Create presenter and view components

agent = Presenter()
view = View()

# Begin 

boards = {}

# Create and store a board
my_board = Board("My Board")
boards[my_board.id] = my_board

# Determine allowable methods for GPT

ALLOWABLE_OBJ = {'view': view,
                 'my_board': my_board,
                 'Board': Board,
                 'List': List,
                 'Card': Card}


my_board.add_child(List("List title 1"))
my_board.add_child(List("List title 2"))
my_board.add_child(List("List title 4"))

view.view_board(my_board)


print("\n")


third = List("List title 3")
third_id = third.id

#third.add_child(Card("Agenda", "Finish programming this thing"))
my_board.add_child(third)
third.add_child(Card("Agenda", "Finish programming this thing"))
view.view_list(my_board.get_child_by_id(third_id))


"""
# Input loop
while (1):


    

    
    #instructions = agent.take_input()
    instructions = []
    instructions.append(input())

    for instruct in instructions:
        eval(instruct, {'__builtins__':None}, ALLOWABLE_OBJ)
    """

