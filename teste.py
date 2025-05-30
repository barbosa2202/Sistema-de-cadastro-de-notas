import tkinter as tk
from tkinter import messagebox
from registrar_notas import RegistroNotas

a = RegistroNotas()

def adicionar_nota(a):
    matricula = entry_matricula.get()
    aluno = entry_nome.get()
    semestre = entry_semestre.get()
    materia = entry_materia.get()
    nota = entry_nota.get()
    
    
    a.adicionar_notas_em_lote([(matricula, aluno, semestre, materia, nota)])
    messagebox.showinfo("Sucesso", f"Nota adicionada para {aluno}!")
    limpar_campos()

def exibir_notas():
    notas_janela = tk.Toplevel(root)
    notas_janela.title("Notas Registradas")
    texto = tk.Text(notas_janela, width=80, height=20)
    texto.pack()
    if not a.notas:
        texto.insert(tk.END, "Nenhuma nota registrada ainda.\n")
        return
    for matricula, dados in a.notas.items():
        texto.insert(tk.END, f"Matrícula: {matricula} | Aluno: {dados['aluno']}\n")
        for semestre, materias in dados["semestres"].items():
            texto.insert(tk.END, f"  Semestre: {semestre}\n")
            for materia, nota in materias.items():
                texto.insert(tk.END, f"    Matéria: {materia} | Nota: {nota}\n")
        texto.insert(tk.END, "\n")
def limpar_campos():
    entry_matricula.delete(0, tk.END)
    entry_nome.delete(0, tk.END)
    entry_semestre.delete(0, tk.END)
    entry_materia.delete(0, tk.END)
    entry_nota.delete(0, tk.END)


root = tk.Tk()
root.title("Registro de Notas")
root.geometry("400x350")
tk.Label(root, text="matricula:").pack()
entry_matricula = tk.Entry(root)
entry_matricula.pack()
tk.Label(root, text="nome do aluno:").pack()
entry_nome = tk.Entry(root)
entry_nome.pack()
tk.Label(root, text="semestre:\n").pack()
entry_semestre = tk.Entry(root)
entry_semestre.pack()
tk.Label(root, text="materia\n").pack()
entry_materia = tk.Entry(root)
entry_materia.pack()
tk.Label(root, text="nota:\n").pack()
entry_nota = tk.Entry(root)
entry_nota.pack()
tk.Button(root, text="Adicionar Nota", command=lambda: adicionar_nota(a)).pack(pady=10)
tk.Button(root, text="Exibir Notas", command=exibir_notas).pack(pady=5)
root.mainloop()