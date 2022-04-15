#Author: Trey Phillips
from graphics import *
import random


class Token:

    def __init__(self, column, row, color):

        self.x = x_list[column]
        self.y = y_list[row]
        self.edge = Circle(Point(self.x, self.y), 55)
        self.color4 = color + "4"
        self.color2 = color + "2"
        self.edge.setFill(self.color4)
        self.inner = Circle(Point(self.x, self.y), 42.5)
        self.inner.setFill(self.color2)
        self.logo = Text(Point(self.x, self.y), chr(960))
        self.logo.setSize(36)
        self.logo.setTextColor(self.color4)
        self.logo.setStyle("bold")

    def draw(self):
        self.edge.draw(board)
        self.inner.draw(board)
        self.logo.draw(board)


def are_four_diagonal():
    """ Checks if the win conditions of having four matching pieces in a row
    diagonally is met

    Returns:
        True or False
    """
    for y in range(6):
        for x in range(7):
            try:
                diagonal_list = []
                for i in range(4):
                    val = board_list[y + i][x - i]
                    if val != ' ':
                        diagonal_list.append(val)
                    if len(diagonal_list) > 5:
                        diagonal_list.pop()
                if diagonal_list.count('1') == 4:
                    return True
                if diagonal_list.count('2') == 4:
                    return True
            except:
                pass

            try:
                diagonal_list = []
                for i in range(4):
                    val = board_list[y + i][x + i]
                    if val != ' ':
                        diagonal_list.append(val)
                    if len(diagonal_list) > 5:
                        diagonal_list.pop()
                if diagonal_list.count('1') == 4:
                    return True
                if diagonal_list.count('2') == 4:
                    return True
            except:
                pass


def are_four_horizontal():
    """ Checks if the win conditions of having four matching pieces in a row
     vertically is met

        Returns:
            True or False
    """
    for y in range(6):
        row_list = []
        for x in range(7):
            val = board_list[y][x]
            if val != " ":
                row_list.append(val)
            else:
                row_list.append(" ")
            if len(row_list) > 4:
                row_list.pop(0)

            if row_list.count('1') == 4:
                return True
            elif row_list.count('2') == 4:
                return True
            else:
                continue
    return False


def are_four_vertical():
    """ Checks if the win conditions of having four matching pieces in a row
    vertically is met

    Returns:
        True or False
    """
    for x in range(7):
        column_list = []
        for y in range(len(board_list)):
            val = board_list[y][x]
            if val != " ":
                column_list.append(val)
            if len(column_list) > 4:
                column_list.pop()
        if column_list.count('1') == 4:
            return True
        if column_list.count('2') == 4:
            return True


def build_board(win):
    """ Creates the game-board upon a Graph Win object

    Parameters:
        win: A GraphWin object

    Returns:
        Nothing, called for side-effects
    """
    for y_ind in range(len(board_list)):
        for x_ind in range(len(board_list[y_ind])):
            y = y_list[y_ind]
            x = x_list[x_ind]
            color = board_list[y_ind][x_ind]
            if color == "1":
                color = get_player_color(color)
            elif color == "2":
                color = get_player_color("2")
            else:
                color = "White"

            if color == "White":
                draw_circle(x, y, color)
            else:
                draw_token(x, y, color)


def check_win_cons():
    """ Calls all three of the functions which check if a player has won
     the game

    Returns:
        True if any of the conditions are met, else returns False
    """
    if are_four_vertical() or are_four_horizontal() or are_four_diagonal():
        return True
    else:
        return False


def color_picker(win_name):
    """ Creates a window which displays multiple colors and allows the user
    to select a color from the window

    Parameters:
        win_name: The Name of the Window created

    Return:
        The color clicked by the user
    """
    win = GraphWin(win_name, 1200, 400)
    win.setCoords(0, 2, 4, 0)
    print("Pick a color on the window.")

    color_names = [
        "Red", "Orange", "Yellow", "Green",
        "Cyan", "Blue", "Purple", "Magenta"
    ]
    color_xuls = [0, 1, 2, 3, 0, 1, 2, 3]
    color_yuls = [0, 0, 0, 0, 1, 1, 1, 1]

    for (x, y, color) in zip(color_xuls, color_yuls, color_names):
        rectangle(x, y, x + 1, y + 1, color, win)

    click = win.getMouse()
    cx = click.getX()
    cy = click.getY()
    win.close()
    for (x, y, color) in zip(color_xuls, color_yuls, color_names):
        if x < cx < x + 1 and y < cy < y + 1:
            return color


def draw_circle(x, y, color):
    """ Draws a circle with given radius, center-point, and color upon a
     given win

    Parameters:
        r: A float or int
        x: A float or int
        y: A float or int
        color: A string

    Returns:
        Nothing, called for side-effects
    """
    circ = Circle(Point(x, y), 55)
    circ.setFill(color)
    circ.draw(board)


def draw_scoreboard(win):
    """ Draws a scoreboard upon a given win

    Parameters:
        win: A GraphWin object

    Returns:
        Nothing, called for side-effects
    """
    global scoreboard_text

    scoreboard_text = Text(Point(440, 20), (
        player_1_color
        + " Wins: "
        + str(wins1)
        + "       "
        + player_2_color
        + " Wins: "
        + str(wins2))
    )
    scoreboard_text.setTextColor("White")
    scoreboard_text.setSize(20)
    scoreboard_text.draw(win)


def draw_token(x, y, color):
    """ Draws a player token with a given radius, center-point, and color
    upon a win

    Parameters:
        r: A float or int
        x: A float or int
        y: A float or int
        color: A string

    Returns:
        Nothing, called for side-effects
    """
    token_list = [Token(x_list.index(x), y_list.index(y), color)]
    for token in token_list:
        token.draw()


def endgame():
    """ Performs end-of-round operations to display the winning message and
    options to play again or exit

    Returns:
        Nothing, called for side-effects

    """
    global again_circle, again_text, exit_circle, exit_text

    again_circle = Circle(Point(220, 610), 100)
    again_circle.setFill("Green")
    again_circle.draw(board)
    exit_circle = Circle(Point(660, 610), 100)
    exit_circle.setFill("Red")
    exit_circle.draw(board)
    again_text = Text(Point(220, 610), "Play\nAgain?")
    again_text.setSize((36))
    again_text.draw(board)
    exit_text = Text(Point(660, 610), "Exit")
    exit_text.setSize(36)
    exit_text.draw(board)


def get_column(click):
    """ Takes click and determines which column on the board the click was in

    Parameters:
        click: A point object

    Returns:
        The index of the column the point lies within
    """
    column_val = 1
    for (x1, x2) in zip(x_1_list, x_2_list):
        if x1 < click.getX() < x2:
            return column_val
        column_val += 1
    return 0


def get_distance(point1, point2):
    """ Given two points, finds the distance between the two

    Parameters:
        point1: A point object
        point2: A point object

    Returns:
        The distance between point1 and point2
    """
    x1 = point1.getX()
    x2 = point2.getX()
    y1 = point1.getY()
    y2 = point2.getY()

    distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    return distance


def get_open(column):
    """ Takes a column index and returns the index of the first open spot
    in said column

    Parameters:
        column: An int

    Returns:
        The index of the first open spot in a column
    """
    length = len(board_list)
    column_list = []
    open_spots = []
    for row in board_list:
        column_val = row[column]
        column_list.append(column_val)
    spot_ind = 0
    for spot in column_list:
        if spot_ind > length:
            break
        spot_val = length - spot_ind
        if spot == " ":
            open_spots.append(spot_val)
            spot_ind += 1
            continue
        else:
            spot_ind += 1
    return open_spots[-1]


def get_player_color(current_player):
    """ Given a player, returns the color that is associated with said player

    Parameters:
        current_player: A string representing the player whose turn it is

    Returns:
        The color associated the given player
    """
    if current_player == "1":
        return player_1_color
    elif current_player == "2":
        return player_2_color


def play_round(first_player):
    """ Initializes a round of Connect Four with the given first player

    Parameters:
        first_player: A string representing the player which will have the
        first turn

    Returns:
        Nothing, called for side-effects
    """

    player_color = get_player_color(first_player)
    start_text_string = player_color + ' goes first\n\nClick to start'
    start_text = Text(Point(440, 405), start_text_string)
    start_text.setSize(36)
    start_text.setTextColor(player_color)
    start_text.setStyle("bold")
    player = first_player
    try:
        text_box.undraw()
    except:
        pass
    finally:
        text_box.draw(board)
    start_text.draw(board)
    board.getMouse()
    start_text.undraw()
    text_box.undraw()
    while True:
        click = board.getMouse()
        column = get_column(click)
        try:
            open_spot_ind = get_open(column)
        except:
            print("That was not a valid selection, try again")
            continue
        update_board(column, open_spot_ind, player)
        if check_win_cons():
            global wins1, wins2
            if player == "1":
                wins1 += 1
            elif player == "2":
                wins2 += 1
            winner(player)
            player = other_player(player)
            break
        else:
            player = other_player(player)


def rectangle(xul, yul, xlr, ylr, color, win):
    """ Given a point, draws a rectangle of a given color upon a given win

        Parameters:
            xul: A float
            color: A string
            win: A GraphWin object

        Returns:
              Nothing, called for side-effects
        """
    rectangle = Rectangle(Point(xul, yul), Point(xlr, ylr))
    rectangle.setFill(color)
    rectangle.draw(win)


def square(xul, color, win):
    """ Given a point, draws a square of a given color upon a given win

    Parameters:
        xul: A float
        color: A string
        win: A GraphWin object

    Returns:
          Nothing, called for side-effects
    """
    square = Rectangle(Point(xul, 0), Point(xul + 1, 1))
    square.setFill(color)
    square.draw(win)


def other_player(current_player):
    """ Given the current player, returns the opposite player

    Parameters:
        current_player: A string representing the current player

    Returns:
        A string representing the opposing player
    """
    if current_player == "1":
        return "2"
    elif current_player == "2":
        return "1"


def update_board(column, row, val):
    """ Updates the value at a given point in the board_list and then redraws
    the board to reflect the change

    Parameters:
        column: An int
        row: An int
        val: A string representing if a player has claimed a spot

    Returns:
        Nothing, called for side-effects
    """
    length = len(board_list)
    row = length - row
    board_list[row][column] = val
    draw_token(x_list[column], y_list[row], get_player_color(val))


def winner(winning_player):
    """ Given a player, displays a string communicating that that player has
    won the game

    Parameters:
        winning_player: A string representing the player who has won the round

    Returns:
        Nothing, called for side-effects
    """
    global win_text, score1_text, score2_text
    win_text = Text(Point(440, 300), (
            get_player_color(winning_player) +
            " Wins!\n\nCurrent Score:\n\n" +
            " : "
    ))
    score1_text = Text(Point(415, 385), str(wins1))
    score1_text.setTextColor(get_player_color("1"))
    score1_text.setSize(36)
    score2_text = Text(Point(465, 385), str(wins2))
    score2_text.setTextColor(get_player_color("2"))
    score2_text.setSize(36)

    win_text.setSize(36)
    win_text.setTextColor("white")
    win_text.setStyle("bold")
    text_box.draw(board)
    win_text.draw(board)
    score1_text.draw(board)
    score2_text.draw(board)

board_list = [
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "]
]
board = GraphWin("Connect Four", 880, 810)
board_color = "Black"
board.setBackground(board_color)
click_x = 0
line_x_list = [2, 127, 252, 377, 502, 627, 752, 877]
player_list = ["1", "2"]
player_1_color = color_picker("Player 1 Color?")
while True:
    player_2_color = color_picker("Player 2 Color?")
    if player_1_color != player_2_color:
        break
    else:
        except_string = (
            "Player 1 already picked that color,"
            "please pick a different color."
            )
        print(except_string)
        continue
text_box = Rectangle(Point(0, 0), Point(880, 810))
text_box.setFill("Black")
wins1 = 0
wins2 = 0
x_list = [65, 190, 315, 440, 565, 690, 815]
x_1_list = [127.5, 252.5, 377.5, 502.5, 627.5, 752.5]
x_2_list = [252.5, 377.5, 502.5, 627.5, 752.5, 877.5]
y_list = [92.5, 217.5, 342.5, 467.5, 592.5, 717.5]
y_list_rev = [717.5, 592.5, 467.5, 342.5, 217.5, 92.5]
first_player = player_list[random.randrange(2)]
draw_scoreboard(board)
build_board(board)
while True:
    first_player = other_player(first_player)
    play_round(first_player)
    endgame()
    while True:
        click = board.getMouse()
        distance_again = get_distance(Point(220, 610), click)
        distance_exit = get_distance(Point(660, 610), click)
        if distance_exit > 100 and distance_again > 100:
            continue
        else:
            break
    if distance_again < 100:
        win_text.setText("")
        scoreboard_text.setText(
            player_1_color
            + " Wins: "
            + str(wins1)
            + "       "
            + player_2_color
            + " Wins: "
            + str(wins2)
        )
        score1_text.undraw()
        score2_text.undraw()
        board_list = [
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "]
            ]
        again_circle.undraw()
        again_text.undraw()
        exit_circle.undraw()
        exit_text.undraw()
        build_board(board)
        continue
    elif distance_exit < 100:
        board.close()
        break
