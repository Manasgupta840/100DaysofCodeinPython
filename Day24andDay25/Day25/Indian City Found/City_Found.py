import turtle
import pandas as pd

ALIGNMENT = 'center'
FONT = ("Arial", 10, "normal")
FONT2 = ("Arial", 20, "normal")

screen = turtle.Screen()
screen.title("Indian States Game")
image = "imgonline-com-ua-resize-ifG2DWYaUSu70f.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("states_coordinates.csv")
all_states = data.states.to_list()
length = len(all_states)
game_is_on = True
count = 0
tim = turtle.Turtle()
tim.hideturtle()
while game_is_on:
    city_name = screen.textinput(title=f"{count}/{length}Guess the State", prompt="What's another state's name").lower().strip()
    if city_name == "exit":
        pd.DataFrame(all_states).to_csv("missed_states")
        break
    if city_name in all_states:
        count += 1
        city = data[data.states == city_name]
        tim.penup()
        tim.goto(float(city.x), float(city.y))
        tim.write(f"{city_name.title()}", align=ALIGNMENT, font=FONT)
        all_states.remove(city_name)
    if count == length:
        tim.write(f"Game Over", align=ALIGNMENT, font=FONT2)
        break

# def get_mouse_click_coor(x, y):
#     city_name = screen.textinput(title="Guess the State", prompt="What's another state's name").lower()
#     print(city_name + "," + str(x) + "," + str(y))
#
#
# turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()