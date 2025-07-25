from turtle import Turtle,Screen
import turtle,pandas    
window=Screen()
window.setup(1380,640)
window.title("octo code")
#window.bgcolor("black")
window.bgpic("lesson7/worldmap.gif")
count_country=0
# def my_function(x,y):
#     print(x,y)
# turtle.onscreenclick(my_function)
data=pandas.read_csv("lesson7/coordinates.csv")
countries=data.country.to_list()
guessed=[]
while len(guessed)<22:
    answer=window.textinput(f"{count_country}/23 guessed","type a country name and hit enter").title()#وده لان المستخدم ممكن يكتب اول حرف سمال وهو كابيتال في الملف 
    if answer in countries:
        guessed.append(answer)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        country_x=data[data.country==answer]["x"].item()
        country_y=data[data.country==answer]["y"].item()
        t.goto(country_x,country_y)
        t.fillcolor("red")
        t.begin_fill()
        t.circle(15)
        t.end_fill()
        t.write(answer,font=("arial",15))




# turtle.mainloop()
# دولة 22 هلغيها لاني هخلي اللعبة تفضل شغالة لغاية مايخمن