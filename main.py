import tkinter                 # Default
import PIL.Image, PIL.ImageTk  # pip install pillow
import cv2                     # pip install opencv-python

# Dimentions of main screen
SET_WIDTH = 703
SET_HEIGHT = 620

# GUI Setup Starts Here

# Setting the Welcome Screen
window = tkinter.Tk()
window.title("Decision Review System (DRS) By Ajay, Payal, Gayatri")
window.resizable(0, 0)
cv_img = cv2.cvtColor(cv2.imread("./img/welcome.jpg"), cv2.COLOR_BGR2RGB)
btnback = cv2.cvtColor(cv2.imread("./img/btn.png"), cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window, width=SET_WIDTH, height=SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
btnphoto = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(btnback))
image_on_canvas = canvas.create_image(0, 0, ancho=tkinter.NW, image=photo)
image_on_canvas1 = canvas.create_image(0, 412, ancho=tkinter.NW, image=btnphoto)
canvas.pack()

# Setting Buttons to Control Playback

btn = tkinter.Button(window, text="<< Backward (Slow)", width=35, activebackground="yellow", bd=3, bg="#d0fefe", pady=4, font=('Helvetica', '10'), relief="groove")
btn.place(x=50, y=440)

btn = tkinter.Button(window, text="<< Backward (Fast)", width=35, activebackground="blue", bd=3, bg="#d0fefe", pady=4, font=('Helvetica', '10'), relief="groove")
btn.place(x=50, y=475)

btn = tkinter.Button(window, text="Forward (Slow) >>", width=35, activebackground="yellow", bd=3, bg="#d0fefe", pady=4, font=('Helvetica', '10'), relief="groove")
btn.place(x=360, y=440)

btn = tkinter.Button(window, text="Forward (Fast) >>", width=35, activebackground="blue", bd=3, bg="#d0fefe", pady=4, font=('Helvetica', '10'), relief="groove")
btn.place(x=360, y=475)

btn = tkinter.Button(window, text="OUT", width=74, activebackground="red", bd=3, bg="#d0fefe", pady=4, font=('Helvetica', '10'), relief="groove")
btn.place(x=50, y=530)

btn = tkinter.Button(window, text="NOT OUT", width=74, activebackground="green", bd=3, bg="#d0fefe", pady=4, font=('Helvetica', '10'), relief="groove")
btn.place(x=50, y=565)

window.mainloop()