from tkinter import *
from sys import platform as sys_name
import requests
import json


class janela_login:
    def __init__(self):
        self.link_database = "https://aplicativo-teste-18aac-default-rtdb.firebaseio.com/"
        self.root = Tk()
        self.config_janela()
        self.frames()
        self.widgets_janela()
        
        self.root.mainloop()
    
    def config_janela(self):
        self.root.title("Login: App Tester - V 1.0.0.1")
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
        self.frames()
        def button_forget_pass():
            def retorne():
                self.button_retorne.destroy()
                self.widgets_janela()
                    
            def trocar_senha():
                self.entry_acess_pegar = self.entry_acess.get()
                self.entry_password_pegar = self.entry_password.get()
                
                if self.entry_acess_pegar == "" or self.entry_password_pegar == "":
                    self.label_incorrect = Label(self.frame_widgets, bd=2, relief=GROOVE, text="Algum campo ficou em branco!")
                    self.label_incorrect.place(relx=0.2, rely=0.01, relwidth=0.6, relheight=0.05)
                    self.label_incorrect.configure(bg="white", font="consolas 12 bold")
                    return
                
                self.dados = {
                    "id-acess": self.entry_acess_pegar,
                    "pass-user": self.entry_password_pegar
                }
                
                self.buscar_users = requests.get(f"{self.link_database}id-admin/id-acess/.json")
                self.buscar_pass = requests.get(f"{self.link_database}id-admin/pass-user/.json")
                
                self.buscar_users = self.buscar_users.json()
                self.buscar_pass = self.buscar_pass.json()
                
                if self.buscar_users:
                    num = 0
                    for chave, self.valor_id in self.buscar_users.items():
                        if self.valor_id == self.dados["id-acess"]:
                            break
                        else:
                            continue
                        num += 1
                    
                    num2 = 0
                    for chave, self.valor_pass in self.buscar_pass.items():
                        if num2 == num:
                            if self.valor_id == self.dados["id-acess"] and self.valor_pass == self.dados["pass-user"]:
                                self.label_incorrect = Label(self.frame_widgets, bd=2, relief=GROOVE, text="Você não pode usar a mesma senha!")
                                self.label_incorrect.place(relx=0.2, rely=0.01, relwidth=0.6, relheight=0.05)
                                self.label_incorrect.configure(bg="white", font="consolas 12 bold")
                                return
                            elif self.valor_id != self.dados["id-acess"] and self.valor_pass == self.dados["pass-user"]:
                                self.label_incorrect = Label(self.frame_widgets, bd=2, relief=GROOVE, text="Usuário não encontrado!")
                                self.label_incorrect.place(relx=0.2, rely=0.01, relwidth=0.6, relheight=0.05)
                                self.label_incorrect.configure(bg="white", font="consolas 12 bold")
                                return
                            else:
                                self.new_pass = requests.patch(f"{self.link_database}id-admin/pass-user/.json", json={chave: self.dados["pass-user"]})
                                
                                self.label_acess_sucess = Label(self.frame_widgets, bd=2, relief=GROOVE, text="Senha atualizada com sucesso!")
                                self.label_acess_sucess.place(relx=0.2, rely=0.01, relwidth=0.6, relheight=0.05)
                                self.label_acess_sucess.configure(bg="white", font="consolas 12 bold")
                                return
                                
                            num2 += 1
                        else:
                            continue
                else:
                    self.label_un_user = Label(self.frame_widgets, bd=2, relief=GROOVE, text="Nenhum usuário cadastrado!")
                    self.label_un_user.place(relx=0.2, rely=0.01, relwidth=0.6, relheight=0.05)
                    self.label_un_user.configure(bg="white", font="consolas 12 bold")
                    return
                
            self.frames()
            
            self.men_lab_ace = "Insira seu usuário:"
            
            self.label_acess = Label(self.frame_widgets, text=self.men_lab_ace)
            self.entry_acess = Entry(self.frame_widgets, bd=2, relief=GROOVE)
            self.label_password = Label(self.frame_widgets, text="Sua nova senha: ")
            self.entry_password = Entry(self.frame_widgets, bd=2, relief=GROOVE)
            self.button_submit = Button(self.frame_widgets, text="Trocar senha", bd=2, relief=GROOVE, command=trocar_senha)
            self.button_retorne = Button(self.root, text="Voltar", bd=2, relief=GROOVE, command=retorne)
            
            self.label_acess.place(relx=0.01, rely=0.1, relheight=0.1)
            self.entry_acess.place(relx=0.01, rely=0.22, relwidth=0.98, relheight=0.1)
            self.label_password.place(relx=0.01, rely=0.44, relheight=0.1)
            self.entry_password.place(relx=0.01, rely=0.56, relwidth=0.98, relheight=0.1)
            self.button_submit.place(relx=0.25, rely=0.85, relwidth=0.5, relheight=0.1)
            self.button_retorne.place(relx=0.05, rely=0.85, relwidth=0.15, relheight=0.1)
            
            self.label_acess.configure(bg="white", font="consolas 25 bold")
            self.entry_acess.configure(bg="white", font="consolas 25")
            self.label_password.configure(bg="white", font="consolas 25 bold")
            self.entry_password.configure(bg="white", font="consolas 25")
            self.button_submit.configure(bg="white", font="consolas 25 bold")
            self.button_retorne.configure(bg="white", font="consolas 25 bold")         

        def logar():
            self.id_acess = self.entry_acess.get()
            self.pass_user = self.entry_password.get()
            
            if self.id_acess == "" or self.pass_user == "":
                self.label_incorrect = Label(self.frame_widgets, bd=2, relief=GROOVE, text="Algum campo ficou em branco!")
                self.label_incorrect.place(relx=0.2, rely=0.01, relwidth=0.6, relheight=0.05)
                self.label_incorrect.configure(bg="white", font="consolas 12 bold")
                return
                
            
            self.dados = {
                "id-acess": self.id_acess,
                "pass-user": self.pass_user
            }
            
            self.buscar_users = requests.get(f"{self.link_database}id-admin/id-acess/.json")
            self.buscar_pass = requests.get(f"{self.link_database}id-admin/pass-user/.json")
            
            self.buscar_users = self.buscar_users.json()
            self.buscar_pass = self.buscar_pass.json()
            
            if self.buscar_users:
                num = 0
                for chave, valor in self.buscar_users.items():
                    if valor == self.dados["id-acess"]:
                        break
                    else:
                        continue
                    num += 1
                
                num2 = 0
                for chave, valor in self.buscar_pass.items():
                    if num2 == num:
                        if valor == self.dados["pass-user"]:
                            self.label_acess_sucess = Label(self.frame_widgets, bd=2, relief=GROOVE, text="Usuário logado com sucesso!")
                            self.label_acess_sucess.place(relx=0.2, rely=0.01, relwidth=0.6, relheight=0.05)
                            self.label_acess_sucess.configure(bg="white", font="consolas 12 bold")
                            return
                        else:
                            self.label_incorrect = Label(self.frame_widgets, bd=2, relief=GROOVE, text="Usuário ou senha incorretos!")
                            self.label_incorrect.place(relx=0.2, rely=0.01, relwidth=0.6, relheight=0.05)
                            self.label_incorrect.configure(bg="white", font="consolas 12 bold")
                            return
                        num2 += 1
                    else:
                        continue
            else:
                self.label_un_user = Label(self.frame_widgets, bd=2, relief=GROOVE, text="Nenhum usuário cadastrado!")
                self.label_un_user.place(relx=0.2, rely=0.01, relwidth=0.6, relheight=0.05)
                self.label_un_user.configure(bg="white", font="consolas 12 bold")
                return
            
        def registro():
            self.id_acess = self.entry_acess.get()
            self.pass_user = self.entry_password.get()
            
            if self.id_acess == "" or self.pass_user == "":
                self.label_incorrect = Label(self.frame_widgets, bd=2, relief=GROOVE, text="Algum campo ficou em branco!")
                self.label_incorrect.place(relx=0.2, rely=0.01, relwidth=0.6, relheight=0.05)
                self.label_incorrect.configure(bg="white", font="consolas 12 bold")
                return
            
            self.dados = {
                "id-acess": self.id_acess,
                "pass-user": self.pass_user
            }
            
            self.buscar_users = requests.get(f"{self.link_database}id-admin/id-acess/.json")
            self.buscar_users = self.buscar_users.json()
            
            if self.buscar_users:
                num = 0
                for chave, valor in self.buscar_users.items():
                    if valor == self.dados["id-acess"]:
                        self.label_reg_sucess = Label(self.frame_widgets, bd=2, relief=GROOVE, text="Usuário já cadastrado!")
                        self.label_reg_sucess.place(relx=0.2, rely=0.01, relwidth=0.6, relheight=0.05)
                        self.label_reg_sucess.configure(bg="white", font="consolas 12 bold")
                        return
                    else:
                        num += 1
                        continue
                if num >= len(self.buscar_users) - 1:
                    self.inserir_usuario = requests.post(f"{self.link_database}id-admin/id-acess/.json", data=json.dumps(self.dados["id-acess"]))
                    self.inserir_pass = requests.post(f"{self.link_database}id-admin/pass-user/.json", data=json.dumps(self.dados["pass-user"]))
                        
                    self.label_reg_sucess = Label(self.frame_widgets, bd=2, relief=GROOVE, text="Usuário cadastrado com sucesso!")
                    self.label_reg_sucess.place(relx=0.2, rely=0.01, relwidth=0.6, relheight=0.05)
                    self.label_reg_sucess.configure(bg="white", font="consolas 12 bold")
                    return
            else:
                self.inserir_usuario = requests.post(f"{self.link_database}id-admin/id-acess/.json", data=json.dumps(self.dados["id-acess"]))
                self.inserir_pass = requests.post(f"{self.link_database}id-admin/pass-user/.json", data=json.dumps(self.dados["pass-user"]))
                    
                self.label_reg_sucess = Label(self.frame_widgets, bd=2, relief=GROOVE, text="Usuário cadastrado com sucesso!")
                self.label_reg_sucess.place(relx=0.2, rely=0.01, relwidth=0.6, relheight=0.05)
                self.label_reg_sucess.configure(bg="white", font="consolas 12 bold")
                return
        
        self.label_acess = Label(self.frame_widgets, text="Usuário: ")
        self.entry_acess = Entry(self.frame_widgets, bd=2, relief=GROOVE)
        self.label_password = Label(self.frame_widgets, text="Senha de acesso: ")
        self.entry_password = Entry(self.frame_widgets, bd=2, relief=GROOVE)
        self.button_pass_new = Button(self.frame_widgets, text="Esqueci minha senha!", bd=2, relief=GROOVE, command=button_forget_pass)
        self.button_acess = Button(self.frame_widgets, text="Entrar", bd=2, relief=GROOVE, command=logar)
        self.button_new_acess = Button(self.frame_widgets, text="Registrar", bd=2, relief=GROOVE, command=registro)
        
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
