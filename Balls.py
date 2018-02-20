import tkinter
import random

# constants
Width = 640
Height = 480
Bg_colour = 'white'
Bad_colour = 'red'
Colours = ['aqua', 'fuchsia', Bad_colour, 'pink', 'yellow', 'gold', 'chartreuse']
Zero = 0
Main_ball_radius = 30
Main_ball_colour = 'blue'
Init_dx = 1
Init_dy = 1
Delay = 5
Num_of_balls = 10


# balls class
class Balls():
    def __init__(self, x, y, r, colour, dx=0, dy=0):
        self.x=x
        self.y=y
        self.r=r
        self.colour=colour
        self.dx=dx
        self.dy=dy
        
    def draw(self):
        canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill = self.colour, outline=self.colour if self.colour != Bad_colour else 'black')
        
    def hide(self):
        canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill = Bg_colour, outline = Bg_colour)
        
    def is_collision(self, ball):
        a = abs(self.x + self.dx - ball.x)
        b = abs(self.y + self.dy - ball.y)
        return (a*a + b*b)**0.5 <= self.r + ball.r
        
    def move(self):
        # colliding with walls
        if (self.x + self.r + self.dx >= Width) or (self.x - self.r + self.dx <= Zero):
            self.dx = -self.dx
        if (self.y + self.r + self.dy >= Height) or (self.y - self.r + self.dy <= Zero):
            self.dy = -self.dy  
        # colliding with balls
        for ball in balls:
            if self.is_collision(ball):
                if ball.colour != Bad_colour: # good ball
                   ball.hide()
                   balls.remove(ball)
                   self.dx = -self.dx
                   self.dy = -self.dy
                else:
                    self.dx = self.dy = 0
        self.hide()
        self.x += self.dx
        self.y += self.dy
        self.draw()


# mouse events
def mouse_click(event):
    global main_ball
    if event.num == 1:
        if 'main_ball' not in globals():
            main_ball = Balls (event.x, event.y, Main_ball_radius, Main_ball_colour, Init_dx, Init_dy)
            main_ball.draw()
        else: #turn left
            if main_ball.dx * main_ball.dy > 0:
               main_ball.dy = -main_ball.dy
            else:
               main_ball.dx = -main_ball.dx
            
            
    elif event.num == 3: # turn right
           if main_ball.dx * main_ball.dy > 0:
               main_ball.dx = -main_ball.dx
           else:
               main_ball.dy = -main_ball.dy
      
# list of balls
def create_list_of_balls(number):
    lst = []
    while len(lst) < number:
        next_ball = Balls(random.choice(range(0, Width)),     
                          random.choice(range(0, Height)),
                          random.choice(range(15, 35)),
                          random.choice(Colours))
        lst.append(next_ball)
        next_ball.draw()
    return lst


# count of bad balls
def count_bad_balls(list_of_balls):
    res = 0
    for ball in list_of_balls:
        if ball.colour == Bad_colour:
            res += 1
    return res

# main circle game
def main():
    if 'main_ball' in globals():
        main_ball.move()
        if len(balls) - num_of_bad_balls == 0:
            canvas.create_text(Width / 2, Height / 2, text = "You Won!", font = "arial 20", fill = Main_ball_colour)
            main_ball.dx = main_ball.dy = 0
        elif main_ball.dx == 0:
            canvas.create_text(Width / 2, Height / 2, text = "You Lose!", font = "arial 20", fill = Bad_colour)
    root.after(Delay, main)
        


root = tkinter.Tk()
root.title("Balls")
canvas = tkinter.Canvas(root, width=Width, height=Height, bg = Bg_colour)
canvas.pack()
canvas.bind('<Button-1>', mouse_click)
canvas.bind('<Button-3>', mouse_click, '+')
if 'main_ball' in globals():
    del main_ball
balls = create_list_of_balls(Num_of_balls)
num_of_bad_balls = count_bad_balls(balls)
main()
root.mainloop()