import tkinter as tk

def my_func1():
    text = entry.get()
    if text:
        label.config(text=f"Ви ввели: {text}")
    else:
        label.config(text="Введіть текст:")


root = tk.Tk()
root.title("Простий додаток")
root.geometry("500x500")

label = tk.Label(root, text="Введіть текст:")
label.pack(pady=5)

entry = tk.Entry(root)
entry.pack(pady=5)

button = tk.Button(root, text="Оновити", command=my_func1)
button.pack(pady=5)

clear_button = tk.Button(root, text="Очистити", command=lambda: [entry.delete(0, tk.END), label.config(text="Введіть текст:")])
clear_button.pack(pady=5)

root.mainloop()
