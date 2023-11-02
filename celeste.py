import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

# Variável global para armazenar a imagem selecionada
imagem_selecionada = None

# Função para lidar com a seleção do arquivo de imagem
def selecionar_imagem():
    global imagem_selecionada
    arquivo = filedialog.askopenfilename()
    if arquivo:
        imagem = Image.open(arquivo)
        foto = ImageTk.PhotoImage(imagem)
        imagem_selecionada = cv2.imread(arquivo)

        # Crie uma nova janela para exibir a imagem
        nova_janela = tk.Toplevel()
        nova_janela.title("Visualização da Imagem")
        label_imagem = tk.Label(nova_janela, image=foto)
        label_imagem.pack()
        nova_janela.mainloop()

# Função para aplicar ruído branco em uma imagem
def aplicar_ruido():
    global imagem_selecionada
    if imagem_selecionada is not None:
        ruido = np.random.normal(0, 25, imagem_selecionada.shape).astype(np.uint8)
        imagem_com_ruido = cv2.add(imagem_selecionada, ruido)
        cv2.imshow('Imagem com Ruído Branco', imagem_com_ruido)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

# Função para remover o ruído branco e tornar a imagem nítida
def remover_ruido():
    global imagem_selecionada
    if imagem_selecionada is not None:
        # Aplicar a filtragem bilateral
        imagem_nitida = cv2.bilateralFilter(imagem_selecionada, d=9, sigmaColor=75, sigmaSpace=75)
        cv2.imshow('Imagem Nitida', imagem_nitida)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

# Crie a janela
janela = tk.Tk()
janela.title("Inserir e Remover Ruído Branco")

# Personalize a aparência da janela
janela.geometry("400x300")  # Define o tamanho da janela
janela.configure(bg="black")  # Define a cor de fundo da janela

# Exibição da imagem selecionada
label_imagem = tk.Label(janela)
label_imagem.pack()

# Rótulo para instrução "Primeiro, selecione a imagem desejada."
rotulo_instrucao1 = tk.Label(janela, text="Primeiro, selecione a imagem desejada.", bg="black", fg="white" )
rotulo_instrucao1.pack(pady=5)

# Botão para selecionar imagem
botao_selecionar = tk.Button(janela, text="Selecionar Imagem", command=selecionar_imagem, bg="darkred", fg="white")
botao_selecionar.pack(pady=5)  # Define um espaçamento entre o botão e outros widgets

# Rótulo para instrução "Apos a imagem abrir em outra janela, selecione uma das duas opçoes abaixo:"
rotulo_instrucao2 = tk.Label(janela, text="Após a imagem abrir em outra janela, selecione uma das duas opções abaixo:", bg="black", fg="white")
rotulo_instrucao2.pack(pady=5)

# Botão para aplicar ruído branco
botao_aplicar_ruido = tk.Button(janela, text="Aplicar Ruído Branco (borrar imagem)", command=aplicar_ruido, bg="darkred", fg="white")
botao_aplicar_ruido.pack(pady=5)

# Botão para remover o ruído branco
botao_remover_ruido = tk.Button(janela, text="Remover Ruído Branco (limpar imagem)", command=remover_ruido, bg="darkred", fg="white")
botao_remover_ruido.pack(pady=5)

# Iniciar o loop principal da GUI
janela.mainloop()
