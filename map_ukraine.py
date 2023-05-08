import turtle
import pandas as pd

screen = turtle.Screen()
screen.setup(1200, 726)
screen.title("Вгадай області України")
image = 'data/data_map.gif'
screen.addshape(image)
turtle.shape(image)
play_game = True
data = pd.read_csv('data/map_ukraine.csv', sep=';', encoding='windows-1251')
all_district = data.state.to_list()
all_district_answer = []
count = 0
while len(all_district_answer) < 25:
    answer = screen.textinput(f'Згадай назву ({count}/25)', 'Назви область України').title()
    if answer in all_district:
        all_district_answer.append(answer)
        a = turtle.Turtle()
        a.hideturtle()
        a.penup()
        ans_data = data[data.state == answer]
        a.goto(int(ans_data.x), int(ans_data.y))
        a.write(ans_data.state.item())
        count += 1

    if answer == 'Exit':
        data_read = pd.DataFrame((set(all_district) - set(all_district_answer)))
        print(data_read)
        data_read.to_csv('data/learn_district_ukraine_25.csv')
        break


# for district in all_district:
#     a = turtle.Turtle()
#     a.hideturtle()
#     a.penup()
#     ans_data = data[data.state == district]
#     a.goto(int(ans_data.x), int(ans_data.y))
#     a.write(ans_data.state.item())
turtle.mainloop()
