import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

def get_folder_size(path):
    """Recursively calculates total size of folder in bytes, skipping symlinks."""
    total = 0
    for root, dirs, files in os.walk(path, followlinks=False):
        # Remove symlinked directories from dirs so os.walk doesn't descend into them
        dirs[:] = [d for d in dirs if not os.path.islink(os.path.join(root, d))]
        for f in files:
            try:
                fp = os.path.join(root, f)
                if not os.path.islink(fp):
                    total += os.path.getsize(fp)
            except Exception:
                pass  # Optionally log the error
    return total

def human_readable_size(size, decimal_places=1):
    for unit in ['B','KB','MB','GB','TB']:
        if size < 1024:
            return f"{size:.{decimal_places}f} {unit}"
        size /= 1024
    return f"{size:.{decimal_places}f} PB"

def populate_tree(tree, parent, path):
    entries = []
    for entry in os.listdir(path):
        abs_path = os.path.join(path, entry)
        if os.path.isdir(abs_path):
            size = get_folder_size(abs_path)
        else:
            try:
                size = os.path.getsize(abs_path)
            except Exception:
                size = 0
        entries.append((entry, abs_path, size))

    # Sort by size, largest first
    entries.sort(key=lambda x: x[2], reverse=True)

    for entry, abs_path, size in entries:
        display_name = f"{entry} ({human_readable_size(size)})"
        node = tree.insert(parent, 'end', text=display_name, open=False, values=[abs_path])
        if os.path.isdir(abs_path):
            # Add a dummy child so the expand arrow appears
            tree.insert(node, 'end', text='Loading...')

def on_open(event):
    node = tree.focus()
    print(f"Opening: {node}")
    abs_path = tree.item(node, 'values')[0]
    # If already populated, do nothing
    if tree.get_children(node) and tree.item(tree.get_children(node)[0], 'text') != 'Loading...':
        return
    # Remove dummy
    tree.delete(*tree.get_children(node))
    populate_tree(tree, node, abs_path)

def choose_directory():
    selected_dir = filedialog.askdirectory()
    print(f"Selected directory: {selected_dir}")
    if selected_dir:
        tree.delete(*tree.get_children())  # Clear existing
        # Show the selected directory as the root node
        display_name = f"{os.path.basename(selected_dir) or selected_dir} ({human_readable_size(get_folder_size(selected_dir))})"
        root_node = tree.insert('', 'end', text=display_name, open=True, values=[selected_dir])
        populate_tree(tree, root_node, selected_dir)

# GUI setup
root = tk.Tk()
root.title("Directory Tree Viewer with Sizes")
root.geometry("700x500")

# Button to choose folder
btn = tk.Button(root, text="Choose Directory", command=choose_directory)
btn.pack(pady=5)

# Treeview widget
tree = ttk.Treeview(root)
tree.pack(fill='both', expand=True)
tree["columns"] = ("fullpath",)
tree.column("fullpath", width=0, stretch=False)
tree.bind("<<TreeviewOpen>>", on_open)

root.mainloop()
