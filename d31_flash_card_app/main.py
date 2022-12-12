from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash card Mo1der App")
window.minsize(width=900, height=600)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


front_image = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img_file = PhotoImage(file=".\images\card_front.png")
front_image.create_image(400, 263, image=front_img_file)
front_image.grid(row=0, column=0, columnspan=2)



#
# tomato_img = PhotoImage(file="tomato.png")
# canvas.create_image(100, 112, image=tomato_img)
# timer_text = canvas.create_text(102, 134, text="00:00", fill="white", font=(FONT_NAME, 29, "bold"))
#
#
#
#
# my_image = PhotoImage(file="path/to/image_file.png")
# button = Button(image=my_image, highlightthickness=0)
#

window.mainloop()