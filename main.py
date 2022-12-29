from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_front = PhotoImage(file="images/card_front.png")
canvas = Canvas(width=800, height=528)
canvas.create_image(400, 268, image=card_front)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_text(400, 150, text="French", font=("ariel", 40, "italic"))
canvas.create_text(400, 263, text="trouve", font=("ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

wrong_image = PhotoImage(file="images/wrong.png")
cross_button = Button(window, image=wrong_image, highlightthickness=0)
cross_button.grid(column=0, row=1)

right_image = PhotoImage(file="images/right.png")
tick_button = Button(window, image=right_image, highlightthickness=0)
tick_button.grid(column=1, row=1)









window.mainloop()
