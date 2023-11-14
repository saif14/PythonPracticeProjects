from guizero import App, Text, Picture

app = App(title="Wanted")
app.bg = "#FBFBD0"

wanted_text = Text(app, text="Wanted!")
wanted_text.size = 50
wanted_text.font = "Courier"

pic = Picture(app, image="snake.png")

app.display()




