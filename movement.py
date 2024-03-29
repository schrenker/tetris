# function that checks if spawning a figure wouldn't mean a game over
def is_creation_possible(figure, game_state):
    for coord in figure.shape:
        if game_state.area[coord[0]][coord[1]][0] == 'X':
            return False
    return True


# two functions that check if figure can move down. If not possible, it returns
# false which is then saved to is_figure_playable, which then terminates
# playable figure
def move_down(figure, game_state):
    if not is_down_possible(figure, game_state):
        return False
    else:
        figure.move_down()
        return True


def is_down_possible(figure, game_state):
    for i in range(len(figure.shape)):
        if (
            figure.shape[i][0] >= len(game_state.area) - 1
            or game_state.area[figure.shape[i][0] + 1][figure.shape[i][1]][0]
            == "X"
        ):
            game_state.add_figure_to_state(figure)
            return False
    return True


# functions that check for side movement
def move_left(figure, game_state):
    if not is_left_possible(figure, game_state):
        return False
    else:
        figure.move_left()
        return True


def is_left_possible(figure, game_state):
    for i in range(len(figure.shape)):
        if (
            figure.shape[i][1] <= 0
            or game_state.area[figure.shape[i][0]][figure.shape[i][1] - 1][0]
            == "X"
        ):
            return False
    return True


def move_right(figure, game_state):
    if not is_right_possible(figure, game_state):
        return False
    else:
        figure.move_right()
        return True


def is_right_possible(figure, game_state):
    for i in range(len(figure.shape)):
        if (
            figure.shape[i][1] >= len(game_state.area[0]) - 1
            or game_state.area[figure.shape[i][0]][figure.shape[i][1] + 1][0]
            == "X"
        ):
            return False
    return True


# Figure rotation. It basically moves figure to point 0, 0, rotates them around
# that point and moves them back.
def rotate(figure, game_state):
    check, temp = is_rotation_possible(figure, game_state)
    if check:
        figure.shape = temp
        return True
    else:
        return False

# function that checks if rotation is possible. It checks all possible factors,
# figure possibility for being rotated, coordinates and surroundings. If it's
# possible it returns already rotated figure to save cpu time, with figures
# pivot changed if they require so
def is_rotation_possible(figure, game_state):
    if not figure.rotateable:
        return False, None
    temp = figure.shape[:]
    # first coord is ALWAYS the pivot
    for i in range(1, len(temp)):
        x, y = temp[i][1], temp[i][0]
        temp[i] = [
            (x - temp[0][1]) + temp[0][0],
            (y - temp[0][0]) * -1 + temp[0][1],
        ]
    for j in range(len(temp)):
        if (
            temp[j][1] >= len(game_state.area[0])
            or temp[j][1] <= 0 - 1
            or temp[j][0] >= len(game_state.area)
            or game_state.area[temp[j][0]][temp[j][1]][0] == "X"
        ):
            return False, None
    #pivot swap
    temp[0], temp[1] = temp[1], temp[0]
    return True, temp
