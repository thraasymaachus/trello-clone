from class_definitions import *
import sys


# Helper functions
def retrieveKey():
    return open(".config", "r").readline()


# Determine allowable methods for GPT

ALLOWABLE_METHODS = {'newModel': Model,
                     'newList': List,
                     'newCard': Card}


# Create presenter and view components

agent = Presenter()
view = View()

# Begin 

myBoard = Board('My Board')

# Input loop
while (1):
    
    instructions = agent.take_input()

    for instruct in instructions:
        try:
            eval(instruct, {__builtins__:None}, ALLOWABLE_METHODS)
        except NameError:
            print("Error: Agent attempting to use disallowed method. Aborting")
            sys.exit()
        except:
            print(f'Failed while trying to carry out instruction: {instruct}')

