import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.root.geometry("400x500")
        self.root.config(bg="#2c3e50")

        self.tasks = []

        # Main Frame
        self.frame = tk.Frame(self.root, bg="#34495e")
        self.frame.pack(pady=10)

        # Listbox to display tasks
        self.listbox = tk.Listbox(
            self.frame,
            width=50,
            height=10,
            font=('Arial', 12),
            bg="#ecf0f1",
            fg="#2c3e50",
            selectbackground="#3498db",
            selectforeground="#ecf0f1"
        )
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        # Scrollbar for the listbox
        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

        # Entry box for adding new tasks
        self.entry = tk.Entry(
            self.root,
            font=('Arial', 12),
            bg="#ecf0f1",
            fg="#2c3e50",
            borderwidth=2,
            relief=tk.GROOVE
        )
        self.entry.pack(pady=10)

        # Button to add a new task
        self.add_button = tk.Button(
            self.root,
            text="Add Task",
            width=48,
            command=self.add_task,
            bg="#1abc9c",
            fg="#ecf0f1",
            activebackground="#16a085",
            activeforeground="#ecf0f1",
            relief=tk.FLAT
        )
        self.add_button.pack(pady=5)

        # Button to delete a task
        self.delete_button = tk.Button(
            self.root,
            text="Delete Task",
            width=48,
            command=self.delete_task,
            bg="#e74c3c",
            fg="#ecf0f1",
            activebackground="#c0392b",
            activeforeground="#ecf0f1",
            relief=tk.FLAT
        )
        self.delete_button.pack(pady=5)

        # Button to delete all tasks
        self.clear_button = tk.Button(
            self.root,
            text="Clear All Tasks",
            width=48,
            command=self.clear_tasks,
            bg="#f39c12",
            fg="#ecf0f1",
            activebackground="#e67e22",
            activeforeground="#ecf0f1",
            relief=tk.FLAT
        )
        self.clear_button.pack(pady=5)

    def add_task(self):
        task = self.entry.get()
        if task != "":
            self.tasks.append(task)
            self.update_listbox()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def delete_task(self):
        try:
            selected_task_index = self.listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task.")

    def clear_tasks(self):
        self.tasks = []
        self.update_listbox()

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            self.listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
