# hello_tk.py
import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Hello Tkinter")

# Add a label
label = tk.Label(root, text="Hello, world!")
label.pack(padx=20, pady=20)

# Start the GUI event loop
root.mainloop()
