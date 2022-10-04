from turtle import Turtle, Screen
import pandas as pd
import time

screen = Screen()
turtle = Turtle()
turtle.penup()

screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x , y):
#     print(x, y)
#
#
# screen.onscreenclick(get_mouse_click_coor)
# screen.mainloop()

state_data = pd.read_csv("50_states.csv")
state_names = state_data["state"].tolist()
guessed_list = []
print(state_names)


while len(guessed_list) != len(state_data):
    answer_state = screen.textinput(title="Guess the State", prompt=f"What's another state's name? {len(guessed_list)}/50").title()
    if answer_state in state_names and answer_state not in guessed_list:
        guessed_list.append(answer_state)
        x = int(state_data[state_data.state == answer_state].x)
        y = int(state_data[state_data.state == answer_state].y)
        new_turtle = Turtle()
        new_turtle.penup()
        new_turtle.hideturtle()
        new_turtle.goto(x, y)
        new_turtle.write(answer_state, font=('Arial', 8, 'normal'))
    if answer_state == "Exit":
        break
    time.sleep(0.1)
    print(answer_state.title())

states_to_learn = [x for x in state_names if x not in guessed_list]
df = pd.DataFrame(states_to_learn, columns=["Statest to Learn"])
df.to_csv("states_to_learn.csv")
print(df)
