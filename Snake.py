

import turtle
import time
import random

lower=0.1
score = 0
high_score = 0 
lives = 3

#Window
screen = turtle.Screen()
screen.title("Dylan Snake")
screen.bgcolor("black")
screen.setup(width = 700, height = 700)
screen.tracer(0)
screen.register_shape("snake_up.gif", shape=None)
screen.register_shape("snake_right.gif", shape=None)
screen.register_shape("snake_left.gif", shape=None)
screen.register_shape("snake_down.gif", shape=None)
screen.register_shape("apple.gif", shape=None)
screen.register_shape("snake_body.gif", shape=None)
screen.addshape("gnome.gif", shape=None)

#snake´s head
snake = turtle.Turtle()
snake.speed(0)
snake.shape("snake_up.gif")
snake.penup() #quita rastro
snake.goto(0,0)
snake.direction = "stop"

#food
food = turtle.Turtle()
food.speed(0)
food.shape("apple.gif")
food.penup() #quita rastro
food.color("red")
food.goto(0,100)
food.direction = "stop"

#Creating Gnome
gnome = turtle.Turtle()
gnome.penup()
gnome.shape("gnome.gif")
gnome.goto(1000,1000)

#Scorer
show_score = turtle.Turtle()
show_score.speed(0)
show_score.penup()
show_score.hideturtle()
show_score.color("white")
show_score.goto(0,270)
show_score.write(f"    Lives:  {lives}      Score:  {score}      High Score:    {high_score}     ",align= "center",font=("courier",14,"normal"))

#drawing the borderline
borderline = turtle.Turtle()
borderline.speed(0)
borderline.hideturtle()
borderline.penup()
borderline.goto(-300,240)
borderline.pendown()
borderline.color("white")
borderline.forward(599)
borderline.right(90)
borderline.forward(540)
borderline.right(90)
borderline.forward(599)
borderline.right(90)
borderline.forward(600)
borderline.right(90)
borderline.forward(599)
borderline.right(90)
borderline.forward(60)

#Game Over
game_over= turtle.Turtle()
game_over.speed(0)
game_over.penup()
game_over.hideturtle()
game_over.color("white")
game_over.goto(0,0)

#body
snake_body=[]

#functions

#movement
def up():
    if snake.direction!="down":
        snake.direction="up"
        snake.shape("snake_up.gif")

def down():
    if snake.direction!="up":
        snake.direction="down"
        snake.shape("snake_down.gif")

def left():
    if snake.direction!="right":
        snake.direction="left"
        snake.shape("snake_left.gif")

def right():
    if snake.direction!="left":
        snake.direction="right"
        snake.shape("snake_right.gif")

def move():
    if snake.direction == "up":
        cory=snake.ycor()
        snake.sety(cory + 20)

    if snake.direction == "down":
        cory=snake.ycor()
        snake.sety(cory - 20)

    if snake.direction == "left":
        corx=snake.xcor()
        snake.setx(corx - 20)

    if snake.direction == "right":
        corx=snake.xcor()
        snake.setx(corx + 20)

#keyboard
player_name=screen.textinput("Welcome","Just don't crash and enjoy the game\nPlease write your name and PRESS \"OK\" OR \"ENTER\" TO START THE GAME")
screen.listen()
screen.onkeypress(up,"Up")
screen.onkeypress(down,"Down")
screen.onkeypress(left,"Left")
screen.onkeypress(right,"Right")

while lives > 0:
    screen.update()
    #when crash with walls
    if snake.xcor() > 290 or snake.xcor() < -290 or snake.ycor() < -290 or snake.ycor() > 230:
        game_over.write("Ouch!",align="center",font=("gothic",21,"normal"))
        time.sleep(1)
        game_over.clear()
        score=0
        lives-=1
        gnome.goto(1000,1000)  
        snake.clear
        snake.goto(0,0)
        snake.direction = "stop"
        show_score.clear()
        show_score.write(f"    Lives:  {lives}      Score:  {score}      High Score:    {high_score}     ",align= "center",font=("courier",14,"normal"))

    
        
        for body_part in snake_body:
            body_part.goto(1000,1000)
        snake_body.clear()

    #when the snake eats   
    if snake.distance(food) < 20 :
        xfood = random.randint(-280,280) 
        yfood = random.randint(-280,230)
        food.goto(xfood,yfood) 
        if score > 6 :
            xgnome=random.randint(-290,290)
            ygnome=random.randint(-290,230)
            gnome.goto(xgnome,ygnome)

            if gnome.distance(food) < 25:
                xgnome=random.randint(-290,290)
                ygnome=random.randint(-290,230)
                gnome.goto(xgnome,ygnome)

        body_part = turtle.Turtle()
        body_part.speed(0)
        body_part.shape("snake_body.gif")
        body_part.penup() 
        snake_body.append(body_part)
        score+=3
        if score>high_score:
            high_score=score
        show_score.clear()
        show_score.write(f"    Lives:  {lives}      Score:  {score}      High Score:    {high_score}     ",align= "center",font=("courier",14,"normal"))

    #when crash with gnomes
    if snake.distance(gnome) < 19:
        game_over.write("F*k!NG Gnome!",align="center",font=("gothic",21,"normal"))
        time.sleep(1)
        game_over.clear()
        gnome.goto(1000,1000)
        snake.goto(0,0)
        snake.direction="stop"
        for body_part in snake_body:
            body_part.goto(1000,1000)
        snake_body.clear()
        score=0
        lives-=1
        show_score.clear()
        show_score.write(f"    Lives:  {lives}      Score:  {score}      High Score:    {high_score}     ",align= "center",font=("courier",14,"normal"))


    total_parts = len(snake_body)
    for i in range(total_parts -1,0,-1):
        xbody = snake_body[i-1].xcor()
        ybody = snake_body[i-1].ycor()
        snake_body[i].goto(xbody,ybody)

    if total_parts > 0:
        x = snake.xcor()
        y = snake.ycor()
        snake_body[0].goto(x,y)

    move()
    #when crash with itself
    for body_part in snake_body:
        if body_part.distance(snake) < 10:
            game_over.write("That hurts!",align="center",font=("gothic",21,"normal"))
            time.sleep(1)
            game_over.clear()
            score=0
            lives-=1
            gnome.goto(1000,1000)
            snake.clear
            snake.goto(0,0)
            snake.direction = "stop"
            #cls
            for body_part  in snake_body:
                body_part.goto(1000,1000)
            snake_body.clear()
            #new score
            show_score.clear()
            show_score.write(f"    Lives:  {lives}      Score:  {score}      High Score:    {high_score}     ",align= "center",font=("courier",14,"normal"))

        
    
    time.sleep(lower)
game_over.write(f"GAME OVER\n",align="center",font=("gothic",33,"normal"))
game_over.write(f"\n\n\n{player_name} you got at least {high_score} points, keep trying",align="center",font=("gothic",16,"normal"))
time.sleep(6)



