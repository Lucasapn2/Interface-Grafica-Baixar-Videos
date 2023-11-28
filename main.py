import tkinter as tk  # Importa o módulo tkinter e o renomeia como tk
import customtkinter  # Importa o módulo customtkinter
from pytube import YouTube  # Importa a classe YouTube do módulo pytube
import customtkinter as Ctk  # Renomeia o módulo customtkinter como Ctk


def baixar():
    try:
        # Obtém o link do vídeo da entrada de texto
        yt_link = entrada_link.get()
        youtube_video = YouTube(yt_link, on_progress_callback=on_progress)
        video = youtube_video.streams.get_highest_resolution()

        # Configuração do título do vídeo
        title.configure(text=youtube_video.title, text_color="white")
        finalizar_label.configure(text="")

        # Mostra a barra de progresso antes de iniciar o download
        porcentagem.pack()
        progressBar.pack(padx=10, pady=10)

        # Inicia o download do vídeo
        video.download()

        finalizar_label.configure(text="Download Concluído", text_color="green")
    except Exception as e:
        print(f"Erro ao baixar: {e}")
        finalizar_label.configure(text="Download inválido", text_color="red")


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_download = total_size - bytes_remaining

    # Calcula a porcentagem de conclusão do download
    percentagem_of_completion = bytes_download / total_size * 100
    per = str(int(percentagem_of_completion))

    # Atualiza o texto da porcentagem
    porcentagem.configure(text=per + '%')

    # Corrigindo o método update
    porcentagem.update()

    print(percentagem_of_completion)
    progressBar.set(float(percentagem_of_completion) / 100)


# Criação da janela principal
Janela = Ctk.CTk()
Janela.title("Baixar Video")
Janela.geometry("400x300")

# Label e entrada para inserir o link do vídeo
text_label = Ctk.CTkLabel(Janela, text="Digite o link que deseja baixar:")
text_label.pack(pady=10, padx=10)

url_var = tk.StringVar()
entrada_link = Ctk.CTkEntry(Janela, width=350, height=40, textvariable=url_var,
                            placeholder_text="Digite o Link que Deseja Baixar")
entrada_link.pack(pady=10, padx=10)

# Botão para iniciar o download
button_download = Ctk.CTkButton(Janela, text="Baixar", command=baixar)
button_download.pack(pady=10, padx=10)

# Configuração do título, label de finalização, porcentagem e barra de progresso
title = customtkinter.CTkLabel(Janela, text="")
title.pack()

finalizar_label = customtkinter.CTkLabel(Janela, text="")
finalizar_label.pack()

# Porcentagem
porcentagem = customtkinter.CTkLabel(Janela, text="0%")
progressBar = customtkinter.CTkProgressBar(Janela, width=400, progress_color="teal")
progressBar.set(0)

# Inicia o loop principal da aplicação
Janela.mainloop()
