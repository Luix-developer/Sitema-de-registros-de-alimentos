


import sqlite3

def criar_banco():
    conn = sqlite3.connect('banco_de_alimentos.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS alimentos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    quantidade INTEGER NOT NULL
                 )''')

    conn.commit()
    conn.close()

criar_banco()
import tkinter as tk
from tkinter import messagebox
import sqlite3

class SistemaRegistroAlimentos:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de Alimentos")

       
        tk.Label(root, text="Nome do Alimento:").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(root, text="Quantidade:").grid(row=1, column=0, padx=10, pady=10)

        self.nome_entry = tk.Entry(root)
        self.nome_entry.grid(row=0, column=1, padx=10, pady=10)

        self.quantidade_entry = tk.Entry(root)
        self.quantidade_entry.grid(row=1, column=1, padx=10, pady=10)

        
        self.adicionar_button = tk.Button(root, text="Adicionar Alimento", command=self.adicionar_alimento)
        self.adicionar_button.grid(row=2, column=0, columnspan=2, pady=10)

       
        self.lista_alimentos = tk.Listbox(root, width=50)
        self.lista_alimentos.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        
        self.atualizar_lista()

    def adicionar_alimento(self):
        nome = self.nome_entry.get()
        quantidade = self.quantidade_entry.get()

        if not nome or not quantidade:
            messagebox.showwarning("Aviso", "Por favor, preencha todos os campos.")
            return

        try:
            quantidade = int(quantidade)
        except ValueError:
            messagebox.showwarning("Aviso", "Quantidade deve ser um número inteiro.")
            return

        conn = sqlite3.connect('banco_de_alimentos.db')
        c = conn.cursor()
        c.execute('INSERT INTO alimentos (nome, quantidade) VALUES (?, ?)', (nome, quantidade))
        conn.commit()
        conn.close()

        self.nome_entry.delete(0, tk.END)
        self.quantidade_entry.delete(0, tk.END)
        self.atualizar_lista()

    def atualizar_lista(self):
        self.lista_alimentos.delete(0, tk.END)

        conn = sqlite3.connect('banco_de_alimentos.db')
        c = conn.cursor()
        c.execute('SELECT nome, quantidade FROM alimentos')
        alimentos = c.fetchall()
        conn.close()

        for alimento in alimentos:
            self.lista_alimentos.insert(tk.END, f"{alimento[0]} - {alimento[1]} unidades")

if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaRegistroAlimentos(root)
    root.mainloop()

