from class_definitions import *

ALLOWABLE_METHODS = {'newModel': Model,
                     'newList': List,
                     'newCard': Card}

agent = Presenter()
view = View()

# Begin 

myBoard = Board('My Board')

for i in range(3):
    myBoard.add_child(List(f"List {i}"))

print(myBoard.children)

"""
# Input loop
while (1):
    
    instructions = agent.take_input()

    for instruct in instructions:
        try:
            eval(instruct, {__builtins__:None}, ALLOWABLE_METHODS)
        except NameError:
            print("Error: Agent attempting to use disallowed method. Aborting")
            # Abort using sys.exit()
        except:
            print(f'Failed while trying to carry out instruction: {instruct}')

"""