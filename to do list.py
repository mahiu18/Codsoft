import tkinter as tk
from tkinter import messagebox, ttk

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        
        self.style = ttk.Style()
        self.style.configure('TButton', font=('Helvetica', 12), padding=5)
        self.style.configure('TEntry', font=('Helvetica', 12))
        self.style.configure('TFrame', background='#f0f0f0')
        self.style.configure('TLabel', font=('Helvetica', 12), background='#f0f0f0')
        self.style.configure('TListbox', font=('Helvetica', 12))

        self.tasks = []
        
        self.frame = ttk.Frame(root, padding="10")
        self.frame.pack(pady=10)
        
        self.task_listbox = tk.Listbox(self.frame, width=50, height=10, font=('Helvetica', 12), bg='#e6e6e6', fg='#000000')
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        self.scrollbar = ttk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
        
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)
        
        self.entry_task = ttk.Entry(root, width=50)
        self.entry_task.pack(pady=10)
        
        self.button_frame = ttk.Frame(root, padding="10")
        self.button_frame.pack(pady=10)
        
        self.add_task_button = ttk.Button(self.button_frame, text="Add Task", command=self.add_task)
        self.add_task_button.pack(side=tk.LEFT, padx=10)
        
        self.update_task_button = ttk.Button(self.button_frame, text="Update Task", command=self.update_task)
        self.update_task_button.pack(side=tk.LEFT, padx=10)
        
        self.remove_task_button = ttk.Button(self.button_frame, text="Remove Task", command=self.remove_task)
        self.remove_task_button.pack(side=tk.LEFT, padx=10)
        
        self.clear_tasks_button = ttk.Button(self.button_frame, text="Clear All Tasks", command=self.clear_all_tasks)
        self.clear_tasks_button.pack(side=tk.LEFT, padx=10)
        
        self.mark_done_button = ttk.Button(self.button_frame, text="Mark as Done", command=self.mark_as_done)
        self.mark_done_button.pack(side=tk.LEFT, padx=10)
    
    def add_task(self):
        task = self.entry_task.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")
    
    def update_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            new_task = self.entry_task.get()
            if new_task:
                self.tasks[selected_task_index[0]] = new_task
                self.task_listbox.delete(selected_task_index)
                self.task_listbox.insert(selected_task_index, new_task)
                self.entry_task.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "You must enter a task.")
        else:
            messagebox.showwarning("Warning", "You must select a task to update.")
    
    def remove_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.tasks.pop(selected_task_index[0])
            self.task_listbox.delete(selected_task_index)
        else:
            messagebox.showwarning("Warning", "You must select a task to remove.")
    
    def clear_all_tasks(self):
        self.tasks.clear()
        self.task_listbox.delete(0, tk.END)
    
    def mark_as_done(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task = self.tasks[selected_task_index[0]]
            self.tasks[selected_task_index[0]] = f"{task} (Done)"
            self.task_listbox.delete(selected_task_index)
            self.task_listbox.insert(selected_task_index, f"{task} (Done)")
        else:
            messagebox.showwarning("Warning", "You must select a task to mark as done.")
    
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()