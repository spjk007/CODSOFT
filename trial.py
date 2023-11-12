import tkinter as tk

def on_scroll(*args):
    listbox.yview(*args)

# Create the main window
root = tk.Tk()
root.title("Scrollbar on Left, List in Center, Buttons on Right")

# Create a frame for the scrollbar on the left
scrollbar_frame = tk.Frame(root)
scrollbar_frame.pack(side=tk.LEFT, padx=10, pady=10)

# Create a scrollbar in the scrollbar frame
scrollbar = tk.Scrollbar(scrollbar_frame, orient=tk.VERTICAL, command=on_scroll)
scrollbar.pack(fill=tk.Y)

# Create a frame for the list in the center
list_frame = tk.Frame(root)
list_frame.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

# Create a listbox in the list frame
listbox = tk.Listbox(list_frame, yscrollcommand=scrollbar.set)
listbox.pack(expand=True, fill=tk.BOTH)

# Add some dummy data to the listbox
for i in range(20):
    listbox.insert(tk.END, f"Item {i}")

# Create a frame for buttons on the right
button_frame = tk.Frame(root)
button_frame.pack(side=tk.RIGHT, padx=10, pady=10)

# Add buttons to the button frame (replace this with your actual button creation)
button1 = tk.Button(button_frame, text="Button 1")
button1.pack(pady=5)
button2 = tk.Button(button_frame, text="Button 2")
button2.pack(pady=5)

# Start the Tkinter event loop
root.mainloop()
