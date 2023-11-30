from tkinter import *

from game import Game, SCREEN_WIDTH, SCREEN_HEIGHT

PLAY_BUTTON_PATH = "images\play_button.png"
QUIT_BUTTON_PATH = "images\quit_button.png"

class Menu(Tk):
    def __init__(self, *args, **kwargs) -> None:
        Tk.__init__(self, *args, **kwargs)

        self.title("Road Crossing Game 🚗")
        self.resize_window(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)

        self.current_score = 0
        self.button_images = {
            "play": PhotoImage(file=PLAY_BUTTON_PATH),
            "quit": PhotoImage(file=QUIT_BUTTON_PATH)
        }

        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)

        self.frames = {}
        for F in (MainMenu, ScoreMenu, Game):
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
        elif page_name == "ScoreMenu":
            frame.update_score(self.current_score)

    def resize_window(self, width, height):
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()

        x = (ws / 2) - (width / 2)
        y = (hs / 2) - (height / 2)

        self.geometry(f"{width}x{height}+{int(x)}+{int(y)}")

    def delete_game_frame(self):
        self.frames["Game"].delete_game()

    def exit_game(self):
        self.delete_game_frame()
        self.destroy()


class MainMenu(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        # label = Label(self, text="This is the MainMenu page")
        # label.pack(side="top", fill="x", pady=10)

        bg_image = PhotoImage(file='images\plan_main_menu.png')
        bg_label = Label(self, image=bg_image)
        bg_label.image = bg_image
        #bg_label.place(x=0, y=0)
        bg_label.pack()

        start_game_btn = Button(
            self,
            text="Start Game",
            image=controller.button_images["play"],
            command=lambda: controller.show_frame("Game"),
            bd=0
        )
        #start_game_btn.pack()
        start_game_btn.config(width=378, height=120)
        start_game_btn.place(x=459,y=225)
        #start_game_btn.lift()
        
        exit_game_btn = Button(
            self,
            #text="Exit Game",
            image=controller.button_images["quit"],
            command=lambda: controller.exit_game(),
            bd=0
        )
        exit_game_btn.config(width=386, height=120)
        exit_game_btn.place(x=455,y=367)
        #exit_game_btn.pack()
        # exit_game_btn.lift()

        
        #start_game_btn.place(x=459,y=225)
        #exit_game_btn.place(x=459,y=367)
        
        

        # button2 = Button(
        #     self,
        #     text="Go to ScoreMenu",
        #     command=lambda: controller.show_frame("ScoreMenu"),
        # )
        # exit_game_btn = Button(
        #     self, text="Exit Game", command=lambda: controller.exit_game()
        # )

        # button2.pack()


class ScoreMenu(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        self.score = self.controller.current_score
        self.label = Label(self, text=f"Score: {self.score}")
        self.label.pack(side="top", fill="x", pady=10)
        back_btn = Button(
            self,
            text="Go Back to Main Menu",
            command=lambda: controller.show_frame("MainMenu"),
        )
        back_btn.pack()

    def update_score(self, score):
        self.score = score
        self.label.config(text=f"Score: {self.score}")