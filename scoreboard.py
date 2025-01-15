from turtle import Turtle

alignment = "center"
font_chosen = ("Arial", 20, "normal")  # so that it can be easy to change later

with open("data.txt") as data:
    high_score_recorded = data.read()




class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(high_score_recorded)
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.update_scoreboard()
        self.hideturtle()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", align=alignment, font= font_chosen)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}    High Score {self.high_score}", align=alignment, font=font_chosen)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score

            with open("data.txt", mode="w") as data:
                data.write(str(self.high_score))

        self.score = 0
        self.update_scoreboard()


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

