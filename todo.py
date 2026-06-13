import tkinter as tk

# ---------------- WINDOW ----------------
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x500")

# ---------------- TITLE ----------------
label = tk.Label(root, text="My To-Do App 📝", font=("Arial", 18))
label.pack(pady=10)

# ---------------- INPUT ----------------
task_entry = tk.Entry(root, width=30, font=("Arial", 14))
task_entry.pack(pady=10)

# ---------------- LIST ----------------
task_listbox = tk.Listbox(root, width=40, height=12)
task_listbox.pack(pady=20)

# ---------------- FUNCTIONS ----------------
def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def delete_task():
    selected = task_listbox.curselection()
    if selected:
        task_listbox.delete(selected)

def complete_task():
    selected = task_listbox.curselection()
    if selected:
        task = task_listbox.get(selected)
        task_listbox.delete(selected)
        task_listbox.insert(tk.END, "✔ " + task)

# ---------------- BUTTONS ----------------
add_btn = tk.Button(root, text="Add Task ➕", width=15, command=add_task)
add_btn.pack(pady=5)

complete_btn = tk.Button(root, text="Complete ✔", width=15, command=complete_task)
complete_btn.pack(pady=5)

delete_btn = tk.Button(root, text="Delete 🗑️", width=15, command=delete_task)
delete_btn.pack(pady=5)

# ---------------- RUN ----------------
root.mainloop()