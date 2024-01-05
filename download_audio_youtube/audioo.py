import tkinter as tk
from tkinter import messagebox
from pytube import YouTube

def converter():
    try:
        video_url = entry_video.get()
        youtube = YouTube(video_url)
        
        # Obtendo a melhor stream de áudio disponível
        audio_stream = youtube.streams.filter(only_audio=True).first()
        
        # Baixando apenas o áudio
        audio_stream.download('.python/video')

        messagebox.showinfo("Sucesso", "Áudio salvo com sucesso")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")

root = tk.Tk()
root.title("Conversor de áudio")

label_crit1 = tk.Label(root, text="*Coloque seu link aqui:")
label_crit1.pack()

entry_video = tk.Entry(root)
entry_video.pack()

btn_baixar = tk.Button(root, text="Baixar Áudio", command=converter)
btn_baixar.pack()

root.mainloop()
