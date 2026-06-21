import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator

# Function to translate text
def translate_text():
    try:
        input_text = text_input.get("1.0", tk.END).strip()

        if not input_text:
            messagebox.showwarning("Warning", "Please enter text!")
            return

        source = languages[source_lang.get()]
        target = languages[target_lang.get()]

        translated = GoogleTranslator(
            source=source,
            target=target
        ).translate(input_text)

        text_output.delete("1.0", tk.END)
        text_output.insert(tk.END, translated)

    except Exception as e:
        messagebox.showerror("Error", str(e))


# Language dictionary
languages = {
    "English": "en",
    "Hindi": "hi",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Tamil": "ta",
    "Telugu": "te",
    "Japanese": "ja",
    "Chinese": "zh-CN",
    "Arabic": "ar"
}

# Main window
root = tk.Tk()
root.title("Language Translation Tool")
root.geometry("700x500")
root.resizable(False, False)

# Heading
title = tk.Label(
    root,
    text="🌐 Language Translation Tool",
    font=("Arial", 18, "bold")
)
title.pack(pady=10)

# Input Label
tk.Label(root, text="Enter Text:", font=("Arial", 12)).pack()

# Input Text Box
text_input = tk.Text(root, height=6, width=70)
text_input.pack(pady=5)

# Frame for dropdowns
frame = tk.Frame(root)
frame.pack(pady=10)

# Source Language
tk.Label(frame, text="Source Language").grid(row=0, column=0, padx=10)

source_lang = tk.StringVar()
source_combo = ttk.Combobox(
    frame,
    textvariable=source_lang,
    values=list(languages.keys()),
    state="readonly"
)
source_combo.grid(row=1, column=0, padx=10)
source_combo.current(0)

# Target Language
tk.Label(frame, text="Target Language").grid(row=0, column=1, padx=10)

target_lang = tk.StringVar()
target_combo = ttk.Combobox(
    frame,
    textvariable=target_lang,
    values=list(languages.keys()),
    state="readonly"
)
target_combo.grid(row=1, column=1, padx=10)
target_combo.current(1)

# Translate Button
translate_btn = tk.Button(
    root,
    text="Translate",
    font=("Arial", 12, "bold"),
    bg="lightblue",
    command=translate_text
)
translate_btn.pack(pady=10)

# Output Label
tk.Label(root, text="Translated Text:", font=("Arial", 12)).pack()

# Output Text Box
text_output = tk.Text(root, height=6, width=70)
text_output.pack(pady=5)

root.mainloop()