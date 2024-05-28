import turtle
import time
import random

DELAY = 0.1

class SnakeGame:
    def __init__(self):
        self.score = 0
        self.high_score = 0
        self.delay = DELAY

        self.window = turtle.Screen()
        self.window.title("Snake Game")
        self.window.bgcolor("white")
        self.window.setup(width=600, height=600)
        self.window.tracer(0)

        self.head = turtle.Turtle()
        self.head.shape("square")
        self.head.color("black")
        self.head.penup()
        self.head.goto(0, 0)
        self.head.direction = "Stop"

        self.food = turtle.Turtle()
        self.food.speed(0)
        self.food.penup()
        self.food.shape("circle")
        self.food.color("red")
        self.food.goto(0, 100)

        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.shape("square")
        self.pen.color("black")
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(0, 250)
        self.update_score()

        self.segments = []

        self.window.listen()
        self.window.onkeypress(self.go_up, "Up")
        self.window.onkeypress(self.go_down, "Down")
        self.window.onkeypress(self.go_left, "Left")
        self.window.onkeypress(self.go_right, "Right")

    def go_up(self):
        if self.head.direction != "down":
            self.head.direction = "up"

    def go_down(self):
        if self.head.direction != "up":
            self.head.direction = "down"

    def go_left(self):
        if self.head.direction != "right":
            self.head.direction = "left"

    def go_right(self):
        if self.head.direction != "left":
            self.head.direction = "right"

    def move(self):
        if self.head.direction == "up":
            y = self.head.ycor()
            self.head.sety(y + 20)
        if self.head.direction == "down":
            y = self.head.ycor()
            self.head.sety(y - 20)
        if self.head.direction == "left":
            x = self.head.xcor()
            self.head.setx(x - 20)
        if self.head.direction == "right":
            x = self.head.xcor()
            self.head.setx(x + 20)

    def update_score(self):
        self.pen.clear()
        self.pen.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("candara", 24, "bold"))

    def generate_food(self):
        colors = random.choice(['red', 'green', 'black'])
        shapes = random.choice(['square', 'triangle', 'circle'])
        self.food.color(colors)
        self.food.shape(shapes)
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        self.food.goto(x, y)

    def add_segment(self):
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("black")
        new_segment.penup()
        self.segments.append(new_segment)

    def check_collision(self):
        if (
            self.head.xcor() > 290
            or self.head.xcor() < -290
            or self.head.ycor() > 290
            or self.head.ycor() < -290
        ):
            self.game_over()

        for segment in self.segments:
            if segment.distance(self.head) < 20:
                self.game_over()

    def game_over(self):
        time.sleep(1)
        self.head.goto(0, 0)
        self.head.direction = "Stop"

        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()

        self.score = 0
        self.delay = DELAY
        self.update_score()

    def play(self):
        while True:
            self.window.update()

            if self.head.distance(self.food) < 20:
                self.generate_food()
                self.add_segment()
                self.score += 10
                if self.score > self.high_score:
                    self.high_score = self.score
                self.update_score()

            self.check_collision()

            if len(self.segments) > 0:
                x = self.head.xcor()
                y = self.head.ycor()
                self.segments[0].goto(x, y)

            for i in range(len(self.segments) - 1, 0, -1):
                x = self.segments[i - 1].xcor()
                y = self.segments[i - 1].ycor()
                self.segments[i].goto(x, y)

            if len(self.segments) > 0:
                x = self.head.xcor()
                y = self.head.ycor()
                self.segments[0].goto(x, y)

            self.move()

            time.sleep(self.delay)


if __name__ == "__main__":
    game = SnakeGame()
    game.play()
