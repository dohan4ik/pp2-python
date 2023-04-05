from tkinter import *


class PaintApp:

    def __init__(self, master):
        self.master = master
        master.title("Paint")

        # создаем холст
        self.canvas = Canvas(master, width=400, height=400, bg="white")
        self.canvas.pack()

        # создаем кнопку "Rectangle"
        self.rect_button = Button(master, text="Rectangle", command=self.draw_rectangle)
        self.rect_button.pack()

        # создаем кнопку "Eraser"
        self.eraser_button = Button(master, text="Eraser", command=self.activate_eraser)
        self.eraser_button.pack()

        # задаем начальные координаты прямоугольника
        self.rect_start = None
        # флаг, указывающий, активен ли ластик
        self.eraser_active = False

    def activate_eraser(self):
        self.eraser_active = True

    def deactivate_eraser(self):
        self.eraser_active = False

    def draw_rectangle(self):
        # устанавливаем начальные координаты прямоугольника
        self.canvas.bind("<Button-1>", self.set_rect_start)
        # устанавливаем конечные координаты прямоугольника
        self.canvas.bind("<ButtonRelease-1>", self.draw_rect)

    def set_rect_start(self, event):
        self.rect_start = (event.x, event.y)

    def draw_rect(self, event):
        if self.rect_start:
            # получаем конечные координаты прямоугольника
            rect_end = (event.x, event.y)
            # рисуем прямоугольник или ластик
            if self.eraser_active:
                self.canvas.create_rectangle(self.rect_start[0], self.rect_start[1], rect_end[0], rect_end[1],
                                             outline=self.canvas["bg"], width=5)
            else:
                self.canvas.create_rectangle(self.rect_start[0], self.rect_start[1], rect_end[0], rect_end[1],
                                             outline="black")
            # сбрасываем начальные координаты прямоугольника
            self.rect_start = None


root = Tk()
paint_app = PaintApp(root)
root.mainloop()