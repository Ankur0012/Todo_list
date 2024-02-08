import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        listbox.delete(selected_task_index)
    else:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create GUI components
entry = tk.Entry(root, width=40)
add_button = tk.Button(root, text="Add Task", command=add_task, bg="green", fg="white")
delete_button = tk.Button(root, text="Delete Task", command=delete_task, bg="red", fg="white")
listbox = tk.Listbox(root, selectmode=tk.SINGLE)

# Place GUI components on the window
entry.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
add_button.grid(row=1, column=0, padx=10, pady=10)
delete_button.grid(row=1, column=1, padx=10, pady=10)
listbox.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Run the Tkinter event loop
root.mainloop()
