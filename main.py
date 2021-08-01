import pandas
from turtle import Turtle, Screen, shape

screen = Screen()
screen.title("U.S. States Name Game")
image = "blank_states_img.gif"
screen.addshape(image)
shape(image)
score = 0

state_name = Turtle()
state_name.hideturtle()
state_name.color("black")
state_name.pu()

states_coordinates = pandas.read_csv("50_states.csv")
list_of_states = states_coordinates.state.to_list()
x_pos = states_coordinates.x.to_list()
y_pos = states_coordinates.y.to_list()

guessed_list = []
while score < 50:
    # TODO: Modify and save the data
    guess = screen.textinput(f"{score}/50 states scored", "Guess a state").title()

    if guess.title() == "Exit":
        missing_states = [state for state in list_of_states if state not in guessed_list]
        states_to_learn = pandas.DataFrame(missing_states)
        states_to_learn.to_csv("States to learn.csv")
        break

    if guess in list_of_states and guess not in guessed_list:
        score += 1
        index = list_of_states.index(guess)
        coordinate = float(x_pos[index]), float(y_pos[index])
        guessed_list.append(guess)
        state_name.goto(tuple(coordinate))
        state_name.write(guess, False, "center")

exit_command = screen.textinput("", f"Your score was {score}")

