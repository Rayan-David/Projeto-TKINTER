from tkinter import *
from tkinter import ttk
from tkinter import messagebox


janela = Tk()
janela.title("Cadastro de Pacientes")
janela.geometry("1200x500")

abas = ttk.Notebook(janela)
abas.pack(fill="both", expand=True)

#aba1 - Cadastro
aba1 = Frame(abas)
abas.add(aba1, text="Cadastro")

#aba2 - Tabela
aba2 = Frame(abas)
abas.add(aba2, text="Lista de Pacientes")

#Função Cadastrar 

def cadastrar():
    nome = entry_nome.get()
    cpf = entry_cpf.get()
    data_nasc = entry_data_nasc.get()
    telefone = entry_telefone.get()
    email = entry_email.get()
    convenio = entry_convenio.get()
    contato_emergencia = entry_contato_emergencia.get()
    
    if nome == "" or  cpf == "" or data_nasc == "" or telefone == "" or convenio == "" or email == "" or contato_emergencia == "":
        messagebox.showwarning("Erro", "Preencha todos os campos!")
    else:
        tabela.insert("", END, values=(nome, cpf, data_nasc, telefone, email, convenio, contato_emergencia))
        entry_nome.delete(0, END)
        entry_cpf.delete(0, END)
        entry_data_nasc.delete(0, END)
        entry_telefone.delete(0, END)
        entry_email.delete(0, END)
        entry_convenio.delete(0, END)
        entry_contato_emergencia.delete(0, END)
        
        messagebox.showwarning("Sucesso", "Cliente cadastrado")

### Aba cadastro
Label(aba1, text="Nome Completo").pack(pady=5)
entry_nome = Entry(aba1, width=40)
entry_nome.pack()

Label(aba1, text="CPF").pack(pady=5)
entry_cpf = Entry(aba1, width=40)
entry_cpf.pack()

Label(aba1, text="Data de Nascimento").pack(pady=5)
entry_data_nasc = Entry(aba1, width=40)
entry_data_nasc.pack()

Label(aba1, text="Telefone").pack(pady=5)
entry_telefone = Entry(aba1, width=40)
entry_telefone.pack()

Label(aba1, text="Email").pack(pady=5)
entry_email = Entry(aba1, width=40)
entry_email.pack()

Label(aba1, text="Convênio/SUS").pack(pady=5)
entry_convenio = Entry(aba1, width=40)
entry_convenio.pack()

Label(aba1, text="Contato de emergência").pack(pady=5)
entry_contato_emergencia = Entry(aba1, width=40)
entry_contato_emergencia.pack()

Button(
    aba1,
    text="Cadastrar",
    bg="blue",
    fg="white",
    width=20,
    command=cadastrar
).pack(pady=20)

####aba tabela
colunas = ("Nome Completo", "CPF", "Data de Nascimento", "Telefone", "Email", "Convênio/SUS", "Contato de Emergência")

tabela = ttk.Treeview(
    aba2,
    columns=colunas,
    show="headings"
)

for col in colunas:
    tabela.heading(col, text=col)
    tabela.column(col, width=150)

tabela.pack(fill="both", expand=True, pady=20)

janela.mainloop()