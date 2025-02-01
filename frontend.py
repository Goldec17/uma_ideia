from tkinter import *
from sys import platform as sys_name


class janela_login:
    def __init__(self):
        self.root = Tk()
        self.config_janela()
        self.frames()
        self.widgets_janela()
        
        self.root.mainloop()
    
    def config_janela(self):
        self.root.title("Aplicativo Teste - V 1.0.0.1")
        if sys_name != "Android":
            self.root.state("zoomed")
        self.root.configure(bg="white")
        self.root.resizable(False, False)
    
    def frames(self):
        self.frame_center = Frame(self.root, bd=4, relief=GROOVE)
        self.frame_widgets = Frame(self.frame_center, bd=2, relief=RIDGE)
        
        self.frame_center.place(relx=0.2, rely=0.2, relwidth=0.6, relheight=0.6)
        self.frame_widgets.place(relx=0.1, rely=0.02, relwidth=0.8, relheight=0.96)
        
        self.frame_center.configure(bg="white")
        self.frame_widgets.configure(bg="white")
        
        
    def widgets_janela(self):
        def button_forget_pass():
            self.clicks = 0
            def troca():
                self.clicks += 1
                if self.clicks % 2 == 1:
                    self.men_lab_ace = "Insira seu celular:"
                    
                    self.label_acess.destroy()
                    self.label_acess = Label(self.frame_widgets, text=self.men_lab_ace)
                    self.label_acess.place(relx=0.01, rely=0.1, relheight=0.1)
                    self.label_acess.configure(bg="white", font="consolas 25 bold")
                    
                    self.men_tro_num_ema = "Prefiro usar o email"
                    
                    self.button_troca = Button(self.frame_widgets, text=self.men_tro_num_ema, bd=2, relief=GROOVE, command=troca)
                    self.button_troca.place(relx=0.35, rely=0.7, relwidth=0.3, relheight=0.08)
                    self.button_troca.configure(bg="white", font="consolas 12 bold")
                    
                else:
                    self.men_lab_ace = "Insira seu email:"
                    
                    self.label_acess.destroy()
                    self.label_acess = Label(self.frame_widgets, text=self.men_lab_ace)
                    self.label_acess.place(relx=0.01, rely=0.1, relheight=0.1)
                    self.label_acess.configure(bg="white", font="consolas 25 bold")
                    
                    self.men_tro_num_ema = "Prefiro usar o celular"
                    
                    self.button_troca = Button(self.frame_widgets, text=self.men_tro_num_ema, bd=2, relief=GROOVE, command=troca)
                    self.button_troca.place(relx=0.35, rely=0.7, relwidth=0.3, relheight=0.08)
                    self.button_troca.configure(bg="white", font="consolas 12 bold")
                    
            self.frame_widgets.destroy()
            self.frame_widgets = Frame(self.frame_center, bd=2, relief=RIDGE)
            self.frame_widgets.place(relx=0.1, rely=0.02, relwidth=0.8, relheight=0.96)
            self.frame_widgets.configure(bg="white")
            
            self.men_lab_ace = "Insira seu email:"
            self.men_tro_num_ema = "Prefiro usar o celular"
            
            self.label_acess = Label(self.frame_widgets, text=self.men_lab_ace)
            self.entry_acess = Entry(self.frame_widgets, bd=2, relief=GROOVE)
            self.label_password = Label(self.frame_widgets, text="Sua nova senha: ")
            self.entry_password = Entry(self.frame_widgets, bd=2, relief=GROOVE)
            self.button_troca = Button(self.frame_widgets, text=self.men_tro_num_ema, bd=2, relief=GROOVE, command=troca)
            self.button_submit = Button(self.frame_widgets, text="Trocar senha", bd=2, relief=GROOVE)
            
            self.label_acess.place(relx=0.01, rely=0.1, relheight=0.1)
            self.entry_acess.place(relx=0.01, rely=0.22, relwidth=0.98, relheight=0.1)
            self.label_password.place(relx=0.01, rely=0.44, relheight=0.1)
            self.entry_password.place(relx=0.01, rely=0.56, relwidth=0.98, relheight=0.1)
            self.button_troca.place(relx=0.35, rely=0.7, relwidth=0.3, relheight=0.08)
            self.button_submit.place(relx=0.25, rely=0.85, relwidth=0.5, relheight=0.1)
            
            self.label_acess.configure(bg="white", font="consolas 25 bold")
            self.entry_acess.configure(bg="white", font="consolas 25")
            self.label_password.configure(bg="white", font="consolas 25 bold")
            self.entry_password.configure(bg="white", font="consolas 25")
            self.button_troca.configure(bg="white", font="consolas 12 bold")
            self.button_submit.configure(bg="white", font="consolas 25 bold")
        
        def login():
            def login_sucess():
                print("Em construção!")
            
            def login_fall():
                print("Em construção!")
            
        self.label_acess = Label(self.frame_widgets, text="ID de acesso: ")
        self.entry_acess = Entry(self.frame_widgets, bd=2, relief=GROOVE)
        self.label_password = Label(self.frame_widgets, text="Senha de acesso: ")
        self.entry_password = Entry(self.frame_widgets, bd=2, relief=GROOVE)
        self.button_pass_new = Button(self.frame_widgets, text="Esqueci minha senha!", bd=2, relief=GROOVE, command=button_forget_pass)
        self.button_acess = Button(self.frame_widgets, text="Entrar", bd=2, relief=GROOVE)
        self.button_new_acess = Button(self.frame_widgets, text="Registrar", bd=2, relief=GROOVE)
        
        self.label_acess.place(relx=0.01, rely=0.1, relheight=0.1)
        self.entry_acess.place(relx=0.01, rely=0.22, relwidth=0.98, relheight=0.1)
        self.label_password.place(relx=0.01, rely=0.44, relheight=0.1)
        self.entry_password.place(relx=0.01, rely=0.56, relwidth=0.98, relheight=0.1)
        self.button_pass_new.place(relx=0.35, rely=0.7, relwidth=0.3, relheight=0.08)
        self.button_acess.place(relx=0.1, rely=0.85, relwidth=0.3, relheight=0.1)
        self.button_new_acess.place(relx=0.6, rely=0.85, relwidth=0.3, relheight=0.1)
        
        self.label_acess.configure(bg="white", font="consolas 25 bold")
        self.entry_acess.configure(bg="white", font="consolas 25")
        self.label_password.configure(bg="white", font="consolas 25 bold")
        self.entry_password.configure(bg="white", font="consolas 25")
        self.button_pass_new.configure(bg="white", font="consolas 12 bold")
        self.button_acess.configure(bg="white", font="consolas 25 bold")
        self.button_new_acess.configure(bg="white", font="consolas 25 bold")
