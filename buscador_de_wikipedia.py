import wikipedia
import tkinter as tk


wikipedia.set_lang("es")


def search(event):
    content = search_box.get()
    result = wikipedia.summary(content, sentences=1)
    T.delete("1.0", tk.END)
    T.insert(tk.END, result)


wimdow = tk.Tk()
wimdow.title("buscador de wikipedia")
wimdow.geometry("600x600")
search_box = tk.Entry(wimdow)
search_box.place(x=0, y=0)
search_box.bind('<Return>', search)
T = tk.Text(wimdow)
search_box.pack()
T.pack()
T.insert(tk.END, "test")
wimdow.mainloop()
