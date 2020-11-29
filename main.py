import tkinter                 # Default
import PIL.Image, PIL.ImageTk  # pip install pillow
import cv2                     # pip install opencv-python
from functools import partial
import threading
import imutils
import time


# Dimentions of main screen
SET_WIDTH = 703
SET_HEIGHT = 620


# Functionality for backend
stream = cv2.VideoCapture("./clips/s2.mp4")
flag = True
def play(speed):
    global flag
    print(f"Speed is {speed}")
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)

    grabbed, frame = stream.read()
    if not grabbed:
        exit()
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)

    if flag:
        canvas.create_text(350, 28, fill="red", font="Times 25 bold", text="Decision Pending")
    flag = not flag


def pending(decision):

    # 1. Display decision pending image and wait for some time
    frame = cv2.cvtColor(cv2.imread("./img/decision pending.jpg"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
    time.sleep(2)

    # 2. Display sponsors image and wait for some time
    frame = cv2.cvtColor(cv2.imread("./img/developer.jpg"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
    time.sleep(2)

    # 3. Display Decision(OUT/NOT OUT) and wait for some time
    if decision == 'out':
        deci_img = "./img/out.jpeg"
    else:
        deci_img = "./img/not out.jpg"
    frame = cv2.cvtColor(cv2.imread(deci_img), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
    time.sleep(3)


def out():
    thread = threading.Thread(target=pending, args=("out",))
    thread.daemon = 1
    thread.start()
    print("OUT...........")


def not_out():
    thread = threading.Thread(target=pending, args=("not out",))
    thread.daemon = 1
    thread.start()
    print("NOT OUT...........")


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
btn = tkinter.Button(window, text="<< Backward (Slow)", width=35, activebackground="yellow", bd=3, bg="#98fb98", pady=4,
                     font=('Helvetica', '10'), relief="groove", command=partial(play, -2))
btn.place(x=50, y=440)


btn = tkinter.Button(window, text="<< Backward (Fast)", width=35, activebackground="blue", bd=3, bg="#98fb98", pady=4,
                     font=('Helvetica', '10'), relief="groove", command=partial(play, -10))
btn.place(x=50, y=475)


btn = tkinter.Button(window, text="Forward (Slow) >>", width=35, activebackground="yellow", bd=3, bg="#98fb98", pady=4,
                     font=('Helvetica', '10'), relief="groove", command=partial(play, 0.5))
btn.place(x=360, y=440)


btn = tkinter.Button(window, text="Forward (Fast) >>", width=35, activebackground="blue", bd=3, bg="#98fb98", pady=4,
                     font=('Helvetica', '10'), relief="groove", command=partial(play, 15))
btn.place(x=360, y=475)


btn = tkinter.Button(window, text="OUT", width=74, activebackground="red", bd=3, bg="#98fb98", pady=4,
                     font=('Helvetica', '10'), relief="groove", command=out)
btn.place(x=50, y=530)


btn = tkinter.Button(window, text="NOT OUT", width=74, activebackground="green", bd=3, bg="#98fb98", pady=4,
                     font=('Helvetica', '10'), relief="groove", command=not_out)
btn.place(x=50, y=565)


window.mainloop()
