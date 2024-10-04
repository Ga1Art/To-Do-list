import tkinter as tk
from tkinter import messagebox
import os

# Имя файла для хранения задач
TASKS_FILE = "tasks.txt"

# Функция для загрузки задач из файла
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            tasks = file.readlines()
            for task in tasks:
                listbox_tasks.insert(tk.END, task.strip())

# Функция для сохранения задач в файл
def save_tasks():
    tasks = listbox_tasks.get(0, tk.END)
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Функция для добавления задачи в список
def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
        save_tasks()  # Сохраняем задачи после добавления
    else:
        messagebox.showwarning("Ошибка", "Введите задачу")

# Функция для удаления выбранной задачи
def delete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
        save_tasks()  # Сохраняем задачи после удаления
    except IndexError:
        messagebox.showwarning("Ошибка", "Выберите задачу для удаления")

# Функция для очистки всего списка задач
def clear_tasks():
    listbox_tasks.delete(0, tk.END)
    save_tasks()  # Сохраняем изменения после очистки

# Создание главного окна
root = tk.Tk()
root.title("To-do List")

# Создание виджетов интерфейса
frame_tasks = tk.Frame(root)
frame_tasks.pack()

listbox_tasks = tk.Listbox(frame_tasks, height=10, width=50)
listbox_tasks.pack(side=tk.LEFT)

scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tk.Entry(root, width=50)
entry_task.pack()

button_add_task = tk.Button(root, text="Добавить задачу", width=48, command=add_task)
button_add_task.pack()

button_delete_task = tk.Button(root, text="Удалить задачу", width=48, command=delete_task)
button_delete_task.pack()

button_clear_tasks = tk.Button(root, text="Очистить список", width=48, command=clear_tasks)
button_clear_tasks.pack()

# Загрузка задач из файла при запуске программы
load_tasks()

# Запуск главного цикла программы
root.mainloop()