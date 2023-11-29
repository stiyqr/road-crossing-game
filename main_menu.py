from tkinter import *

from game import Game

class Menu(Tk):
    def __init__(self, *args, **kwargs) -> None:
        Tk.__init__(self, *args, **kwargs)

        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)

        self.frames = {}
        for F in (MainMenu, PauseMenu, Game):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainMenu")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
        self.tkraise()
        if page_name == "Game":
            frame.play_game()

    def start_game(self, container):
        new_game_frame = type(self.frames["Game"])(parent=container, controller=self)
        # self.frames["Game"] = game_frame
        # new_game_frame.grid(row=0, column=0, sticky="nsew")
        new_game_frame.tkraise()
        new_game_frame.play_game()

    def delete_game_frame(self):
        self.frames.pop("Game")

    def pause_game_frame(self):
        self.frames.pop("PauseMenu")

    def resize_window(self, width, height):
        # self.geometry(f"{width}x{height}")
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()

        x = (ws / 2) - (width / 2)
        y = (hs / 2) - (height / 2)

        self.geometry(f"{width}x{height}+{int(x)}+{int(y)}")


class MainMenu(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        bg_image = PhotoImage(file='images\plan_main_menu.gif')
        self.bg_label = Label(controller, image=bg_image)
        self.bg_label.image = bg_image
        self.bg_label.place(x=0, y=0)

        play_button = ImageButton(controller, image_path="images\play_button.gif", command=self.show_game_frame)
        play_button.place(x=467,y=238)

        quit_button = ImageButton(controller, image_path="images\quit_button.gif", command=self.close_game_frame)
        quit_button.place(x=464,y=369)

        # button1 = Button(
        #     self,
        #     text="Go to PauseMenu",
        #     command=lambda: controller.show_frame("PauseMenu"),
        # )
        # button2 = Button(
        #     self,
        #     text="Go to Game",
        #     command=lambda: controller.show_frame("Game"),
        # )
        # button1.pack()
        # button2.pack()
        
    def show_game_frame(self):
        self.destroy()
        self.controller.show_frame("Game")

    def close_game_frame(self):
        self.controller.destroy()


class PauseMenu(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="This is Pause menu")
        label.pack(side="top", fill="x", pady=10)

        quit_button = ImageButton(self, image_path="images\menu_button.gif", command=lambda: controller.show_frame("MainMenu"))
        quit_button.pack(pady=10)

        # button = Button(
        #     self,
        #     text="Go to the MainMenu page",
        #     command=lambda: controller.show_frame("MainMenu"),
        # )
        # button.pack()

class ImageButton(Frame):
    def __init__(self, parent, image_path, command=None):
        super().__init__(parent)

        self.image = PhotoImage(file=image_path)
        
        self.image_button = Button(self, image=self.image, bd=0, cursor="hand2", command=command)

        self.image_button.config(width=350, height=100)
        self.image_button.pack()

        self.image_button.bind("<Enter>")
        self.image_button.bind("<ButtonRelease-1>")

    def resize_image(image, maxsize):
        r1 = image.size[0]/maxsize[0] # width ratio
        r2 = image.size[1]/maxsize[1] # height ratio
        ratio = max(r1, r2)
        newsize = (int(image.size[0]/ratio), int(image.size[1]/ratio))
        image = image.resize(newsize, Image.ANTIALIAS)
        return image

        # self.image_button.bind("<Enter>", self.on_enter)
        # self.image_button.bind("<ButtonRelease-1>", self.button_unclicked)
        # self.image_button.bind("<Button-1>", self.button_clicked)
        # self.image_button.bind("<Leave>", self.on_leave)

    # def button_clicked(self, event):
    #     self.image_button.config(bd=0)
    #     print("Button clicked!")

    # def button_unclicked(self, event):
    #     self.image_button.config(bd=0)
    #     print("Button unclicked!")

    # def on_enter(self, event):
    #     self.image_button.config(bd=0)
    #     print("Button unclicked!")

    # def on_leave(self, event):
    #     self.image_button.config(bd=0)
    #     print("Button unclicked!")