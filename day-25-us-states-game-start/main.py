import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
timmy = turtle.Turtle()
timmy.penup()
timmy.hideturtle()


data = pandas.read_csv("50_states.csv")
state_name = data['state'].to_list()
game_on = True

# x = data[data['state'] == 'Arizona']['x'].item()
# print(x)
guess_state = []
count = 0
while game_on:
    answer_state = screen.textinput(title=f"{len(guess_state)}/50 State Correct", prompt="What's another state name?").title()
    if answer_state == "Exit":
        State_to_learn = [x for x in state_name if x not in guess_state]
        print(State_to_learn)
        df = pandas.DataFrame(State_to_learn)
        df.to_csv('state_to_learn.csv')
        game_on = False
    for i in state_name:
        if i == answer_state:
            guess_state.append(i)
            new_x = data[data['state'] == i].x.item()
            new_y = data[data['state'] == i].y.item()
            timmy.goto(int(new_x), int(new_y))
            timmy.write(f"{i}", align="center", font=("Courier", 9, "normal"))

# state_to_learn.csv

