#from engine import Engine
import turtle
from turtle import Turtle, Screen
import pandas

my_screen = Screen()
my_screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")
#engine = Engine()

game_is_on = True

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guess_list = []

while len(guess_list) < 50:
    guess = my_screen.textinput(title=f"{len(guess_list)}/50", prompt="Name a state")
    if guess == "exit":
        states_left = [state for state in all_states if state not in guess_list]
        new_page = pandas.DataFrame(states_left)
        new_page.to_csv("states_to_learn.csv")
        break
    if guess.capitalize() in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == guess.capitalize()]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(guess.capitalize())
        guess_list.append(guess)





