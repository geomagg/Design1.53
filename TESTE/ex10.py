import tkinter as tk
from tkinter import filedialog

def open_file():
	file_path = filedialog.askopenfilename(
		title="Select a Text File", filetypes=[("Text files", "*.txt")])
	if file_path:
		with open(file_path, 'r') as file:
			content = file.read()
			text_widget.delete(1.0, tk.END) # Clear previous content
			text_widget.insert(tk.END, content)


# Create the main window
root = tk.Tk()
root.title("Text File Reader")

# Create a Text widget to display the content
text_widget = tk.Text(root, wrap="word", width=40, height=10)
text_widget.pack(pady=10)

# Create a button to open the file
open_button = tk.Button(root, text="Open File", command=open_file)
open_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
