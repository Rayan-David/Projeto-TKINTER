from tkinter import *
from tkinter import messagebox
from tkinter import ttk

janela = Tk()
janela.title("Cadastro de Pacientes")
janela.geometry("700x500")

abas = ttk.Notebook(janela)
abas.pack(fill="both", expand=True)

aba1 = Frame(abas)
abas.add(aba1, text="Cadastro")

aba2 = Frame(abas)
abas.add(aba2, text="Lista de Pacientes")

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
).pack(pady=20)

colunas = ("Nome", "CPF", "Data de Nascimento", "Telefone", "Email", "Convênio/SUS", "Contato de Emergência")

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