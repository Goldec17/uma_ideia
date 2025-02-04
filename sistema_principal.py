# from pytz import timezone
# from datetime import datetime
from tkinter import *
from tkinter import ttk
from sys import platform as sys_name


class janela_home():
    def __init__(self):
        self.root = Tk()
        self.config_windows()
        self.home()
        # self.widgets_home()
        
        self.root.mainloop()
    
    def config_windows(self):
        self.root.title("Home: App Tester - V 1.0.0.1")
        
        if sys_name != "Android":
            self.root.state("zoomed")
        
        self.root.resizable(False, False)
        self.root.configure(bg="white")
    
    def home(self):
        self.frame_center = Frame(self.root, bd=2, relief=GROOVE)
        self.frame_center.place(relx=0.0025, rely=0.01, relwidth=0.995, relheight=0.98)
        self.frame_center.configure(bg="white")
        
        welcome = f"Seja bem-vindo. Meu nome é Kevin, eu desenvolvi este programa, que ainda está em desenvolvimento,\npara um projeto social de introdução tecnológica a área comercial deste cidade!"
        description = f"O sistema foi desenvolvido pensado na visão do usuário(funcionário), esperamos que goste e nos dêem\nfeedbacks frequentes sobre o seu uso!"
        despedida = f"Por enquanto é só isso, fiquem com Deus!\nAss: Kevinho Slovak."
    
        self.text_welcome = Label(self.frame_center, text=welcome)
        self.text_description = Label(self.frame_center, text=description)
        self.text_despedida = Label(self.frame_center, text=despedida)
        
        self.text_welcome.place(relx=0.02, rely=0.1)
        self.text_description.place(relx=0.02, rely=0.5)
        self.text_despedida.place(relx=0.02, rely=0.85)
        
        self.text_welcome.configure(bg="white", font="Consolas 20 bold")
        self.text_description.configure(bg="white", font="Consolas 20 bold")
        self.text_despedida.configure(bg="white", font="Consolas 20 bold")   
        
        