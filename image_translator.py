import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from PIL import Image
import pytesseract
from googletrans import Translator

# Function to handle the translation process
def translate_image():
    file_path = filedialog.askopenfilename(initialdir=r"C:\Users\DELL\OneDrive\Desktop\python")
    target_language = language_var.get()
    if file_path and target_language:
        img = Image.open(file_path)
        text = pytesseract.image_to_string(img, lang='eng')
        translated_text = translator.translate(text, dest=target_language).text
        original_text.set(text)
        translated_text_var.set(translated_text)

# Initialize Tkinter
root = tk.Tk()
root.title("Image Translator App")
root.geometry("400x300")  # Set window size


# Styles
style = ttk.Style()
style.configure("TButton", foreground="black", background="#FBE698") 
style.configure("TLabel", background="#D2B48C") 
style.configure("TFrame", background="#664229")  

# Translator object
translator = Translator()

# Variable to store original and translated text
original_text = tk.StringVar()
translated_text_var = tk.StringVar()

# Variable to store language selection
languages = ["ar", "fr", "de", "ja", "mr", "hi"] 
language_var = tk.StringVar()
language_var.set("es")  # Default language selection

# UI Elements with Styles
frame = ttk.Frame(root)
frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

browse_button = ttk.Button(frame, text="Browse Image", command=translate_image, style="TButton")
original_label = ttk.Label(frame, text="Original Text:", style="TLabel")
original_text_label = ttk.Label(frame, textvariable=original_text, wraplength=350, justify="left", style="TLabel")
translated_label = ttk.Label(frame, text="Translated Text:", style="TLabel")
translated_text_label = ttk.Label(frame, textvariable=translated_text_var, wraplength=650, justify="left", style="TLabel")
language_label = ttk.Label(frame, text="Select Language:", style="TLabel")
language_menu = ttk.OptionMenu(frame, language_var, *languages)

# Grid layout
browse_button.grid(row=0, column=0, columnspan=2, pady=10, sticky="ew")
original_label.grid(row=1, column=0, sticky='w', padx=10, pady=5)
original_text_label.grid(row=1, column=1, sticky='w', padx=10, pady=5)
translated_label.grid(row=2, column=0, sticky='w', padx=10, pady=5)
translated_text_label.grid(row=2, column=1, sticky='w', padx=10, pady=5)
language_label.grid(row=3, column=0, sticky='w', padx=10, pady=5)
language_menu.grid(row=3, column=1, sticky='w', padx=10, pady=5)

# Configure grid weights to make the frame expandable
frame.grid_rowconfigure(10, weight=1)
frame.grid_columnconfigure(10, weight=1)

# Start the Tkinter main loop
root.mainloop()
