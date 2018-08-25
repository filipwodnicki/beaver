from app.woodcut.board import Board


def greedy_algorithm( pieces, material_size ):

    board_collection = []

    # Algorithm

    board_collection.append(Board(material_size))

    pieces.sort(reverse=True)  # sort in ascending order

    def try_placing(piece):
        for board in board_collection:
            if board.space_remaining >= piece:
                board.insert(piece)
                pieces.remove(piece)
                return True
        return False

    for piece in pieces[:]:  # pieces[:] is a copy for the purposes of the algorithm, otherwise our pieces[] would get modified

        #     print ( board_collection[0].contents )
        if try_placing(piece) == True:
            pass
        else:
            board_collection.append(Board(material_size))
            board_collection[-1].insert(piece)
            pieces.remove(piece)

    return board_collection

def chartify(board_collection):
    """Take a Board_collection result and returns output in a format the Chart.js accepts:
    This format is master list of lists. Each list is all nth items from all Boards"""

    max_num_items = 0
    num_boards = len(board_collection)

    # Get the max # of items in a single board
    for board in board_collection:
        if len(board.contents) > max_num_items:
            max_num_items = len(board.contents)
    ##### FUTURE: complete this step in as few lines as possible 

    # Generate Labels based on the number of Boards present
    labels = []
    for i in range(0,num_boards):
        labels.append("Board " + str(i+1)) #i+1 so we get Board 1, 2, 3 rather than Board 0, 1, 2...
    ##### FUTURE: complete this step in as few lines as possible 

    # initialize output to be a list of lists with all empty values
    # example: [[all 1st items],[all 2nd items],[all 3rd items],...,[all nth items]]
    #step 1: add as many empty lists as there are max_num_items
    output = []
    for i in range(0,max_num_items):
        output.append( [] ) #we now have a list of items
    #step 2: add as many empty strings to each empty list as there are Boards
    for all_nth in output:
        for i in range(0,num_boards):
            all_nth.append('')
    ##### FUTURE: complete this step in as few lines as possible 

    for counter1, board in enumerate(board_collection):
        for counter2, value in enumerate(board.contents):
            output[counter2][counter1] = value


    # print ( "Output:", output )

    #Add Space remaining
    unused = []
    for board in board_collection:
        unused.append(board.space_remaining)

    # print( "Unused:", unused)
    
    data = {
        'labels' : labels, # 'labels': ['Board 0', 'Board 1', 'Board 2', 'Board 3'],
        'output' : output, # 'output': [[7, 6, 5, 4], [1, 2, 3, '']],
        'unused' : unused, # 'unused': [0, 0, 0, 4],
        'num_boards' : num_boards, # 'num_boards': 4,
        'max_num_items' : max_num_items, # 'max_num_items': 2
    }

    return data