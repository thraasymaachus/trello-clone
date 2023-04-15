from class_definitions import *


# Helper functions
def retrieveKey():
    return open(".config", "r").readline()



# Create presenter and view components

agent = Presenter()
view = View()

# Begin 

boards = {}
instructions = []

# Create and store a board
my_board = Board("My Board")
boards[my_board.id] = my_board

# Determine allowable methods for GPT

ALLOWABLE_OBJ = {'view': view,
                 'my_board': my_board,
                 'Board': Board,
                 'List': List,
                 'Card': Card}


# Input loop
while (1):

    
    instruction = agent.take_input().strip().translate({ord(i): None for i in '`'})
    # INPUT: Make a new list on my board called 'To Do'

    print(instruction)
    # OUTPUT: my_board.add_child(List(title='To Do'))

    eval(instruction, {'__builtins__':None}, ALLOWABLE_OBJ)

    view.view_board(my_board)
    
    time.sleep(1) # Ensure no excess API calls
    
    break
