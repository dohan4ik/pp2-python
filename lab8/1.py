from tkinter import *


class PaintApp:

    def __init__(self, master):
        self.master = master
        master.title("Paint")

        # create canvas
        self.canvas = Canvas(master, width=400, height=400, bg="white")
        self.canvas.pack()

        # create "Rectangle" button
        self.rect_button = Button(master, text="Rectangle", command=self.draw_rectangle)
        self.rect_button.pack()

        # create "Pencil" button
        self.pencil_button = Button(master, text="Pencil", command=self.activate_pencil)
        self.pencil_button.pack()

        # create "Deactivate Pencil" button
        self.deactivate_pencil_button = Button(master, text="Deactivate Pencil", command=self.deactivate_pencil)
        self.deactivate_pencil_button.pack()

        # create "Red Pencil" button
        self.red_pencil_button = Button(master, text="Red Pencil", command=self.red_pencil)
        self.red_pencil_button.pack()

        # create "Green Pencil" button
        self.green_pencil_button = Button(master, text="Green Pencil", command=self.green_pencil)
        self.green_pencil_button.pack()

        # create "Blue Pencil" button
        self.blue_pencil_button = Button(master, text="Blue Pencil", command=self.blue_pencil)
        self.blue_pencil_button.pack()

        # set initial rectangle start coordinates
        self.rect_start = None
        # flag indicating whether pencil is active
        self.pencil_active = False
        # current pencil color
        self.pencil_color = "black"

    def activate_pencil(self):
        self.pencil_active = True

    def deactivate_pencil(self):
        self.pencil_active = False

    def red_pencil(self):
        self.pencil_color = "red"

    def green_pencil(self):
        self.pencil_color = "green"

    def blue_pencil(self):
        self.pencil_color = "blue"

    def draw_rectangle(self):
        # set initial rectangle start coordinates
        self.canvas.bind("<Button-1>", self.set_rect_start)
        # set final rectangle end coordinates
        self.canvas.bind("<ButtonRelease-1>", self.draw_rect)

    def set_rect_start(self, event):
        self.rect_start = (event.x, event.y)

    def draw_rect(self, event):
        if self.rect_start:
            # get final rectangle end coordinates
            rect_end = (event.x, event.y)
            # draw rectangle or pencil
            if self.pencil_active:
                self.canvas.create_line(self.rect_start[0], self.rect_start[1], rect_end[0], rect_end[1], fill=self.pencil_color, width=2)
            else:
                self.canvas.create_rectangle(self.rect_start[0], self.rect_start[1], rect_end[0], rect_end[1],
                                             outline="black")
            # reset initial rectangle start coordinates
            self.rect_start = None


root = Tk()
paint_app = PaintApp(root)
root.mainloop()