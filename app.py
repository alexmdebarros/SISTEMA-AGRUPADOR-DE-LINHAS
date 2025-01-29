import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import time

def process_csv(input_file, output_file):
    try:
        df = pd.read_csv(input_file, sep=';', encoding='latin1')

        df['VALOR TOTAL BRUTO ESTORNADO EM REPASSE'] = pd.to_numeric(df['VALOR TOTAL BRUTO ESTORNADO EM REPASSE'].str.replace(',', '.'), errors='coerce')
        df['VALOR DE COMISSÃO RESSARCIDA'] = pd.to_numeric(df['VALOR DE COMISSÃO RESSARCIDA'].str.replace(',', '.'), errors='coerce')

        df_grouped = df.sort_values('PARCELA ATUAL', ascending=False).groupby('ID DO PEDIDO MAGAZINE', as_index=False).first()

        df_summed = df.groupby('ID DO PEDIDO MAGAZINE').agg({
            'VALOR TOTAL BRUTO ESTORNADO EM REPASSE': 'sum',
            'VALOR DE COMISSÃO RESSARCIDA': 'sum'
        }).reset_index()

        df_final = df_grouped.drop(['VALOR TOTAL BRUTO ESTORNADO EM REPASSE', 'VALOR DE COMISSÃO RESSARCIDA'], axis=1).merge(df_summed, on='ID DO PEDIDO MAGAZINE')

        df_final['VALOR TOTAL BRUTO ESTORNADO EM REPASSE'] = df_final['VALOR TOTAL BRUTO ESTORNADO EM REPASSE'].apply(lambda x: f"{x:.2f}".replace('.', ','))
        df_final['VALOR DE COMISSÃO RESSARCIDA'] = df_final['VALOR DE COMISSÃO RESSARCIDA'].apply(lambda x: f"{x:.2f}".replace('.', ','))

        df_final.to_csv(output_file, index=False, sep=';', encoding='latin1')
        return True
    except Exception as e:
        print(f"Erro ao processar o arquivo: {e}")
        return False

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        entry_input.delete(0, tk.END)
        entry_input.insert(0, file_path)

def show_processing_message():
    processing_label.config(text="Processando")
    root.update_idletasks()
    time.sleep(1)  # Simula um pequeno delay para criar um efeito de piscamento
    for _ in range(3):
        processing_label.config(text="Processando.")
        root.update_idletasks()
        time.sleep(0.5)
        processing_label.config(text="Processando..")
        root.update_idletasks()
        time.sleep(0.5)
        processing_label.config(text="Processando...")
        root.update_idletasks()
        time.sleep(0.5)

def save_file():
    file_path = entry_input.get()
    if not file_path:
        messagebox.showerror("Erro", "Nenhum arquivo selecionado!")
        return

    output_file = file_path.replace('.csv', '_processado.csv')

    processing_label.pack(pady=10)  # Mostrar o rótulo de processamento

    root.update_idletasks()
    show_processing_message()  # Mostrar a mensagem de processamento com pontos piscando

    if process_csv(file_path, output_file):
        processing_label.pack_forget()  # Ocultar o rótulo de processamento
        messagebox.showinfo("Sucesso", f"Arquivo processado e salvo como {output_file}")
    else:
        processing_label.pack_forget()  # Ocultar o rótulo de processamento
        messagebox.showerror("Erro", "Erro ao processar o arquivo")

# Configuração da janela principal
root = tk.Tk()
root.title("Agrupador de Linhas 1.0")

# Definir cores e fontes
background_color = "#F5F5F5"  # Cor de fundo pastel
button_color = "#00288b"      # Cor do botão
button_text_color = "#FFFFFF" # Cor do texto do botão
font_title = ("Arial", 16, "bold")
font_button = ("Arial", 12, "bold")

# Configurar a cor de fundo
root.configure(bg=background_color)

# Título
title = tk.Label(root, text="Agrupador de Linhas 1.0", font=font_title, bg=background_color, fg=button_color)
title.pack(pady=20)

# Frame principal
frame = tk.Frame(root, bg=background_color)
frame.pack(pady=20)

# Entrada de arquivo
entry_input = tk.Entry(frame, width=40, font=("Arial", 12), bd=2, relief=tk.SOLID)
entry_input.pack(side=tk.LEFT, padx=10)

# Função para estilizar botões
def style_button(button):
    button.config(
        bg=button_color,
        fg=button_text_color,
        font=font_button,
        relief=tk.RAISED,
        borderwidth=2
    )
    button.bind("<Enter>", lambda e: button.config(bg="#147abb"))
    button.bind("<Leave>", lambda e: button.config(bg=button_color))

# Botão para selecionar arquivo
btn_select = tk.Button(frame, text="Selecionar Arquivo", command=select_file)
style_button(btn_select)
btn_select.pack(side=tk.LEFT, padx=10)

# Botão para processar arquivo
btn_process = tk.Button(frame, text="Processar", command=save_file)
style_button(btn_process)
btn_process.pack(side=tk.LEFT, padx=10)

# Rótulo para mostrar mensagem de processamento
processing_label = tk.Label(root, text="", font=("Arial", 12, 'bold'), bg=background_color, fg=button_color)

root.mainloop()
