import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Quiz")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

game_over = False

while game_over == False:
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
    


screen.exitonclick()