import tkinter as tk
from tkinter import ttk, messagebox
from src.algorithms.caesar import caesar_cipher
from src.algorithms.affine import affine_cipher

class CryptifyApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Cryptify App")
        self.root.geometry("600x700")
        self.root.configure(bg="#2E3440")
        self.setup_ui()

    def setup_ui(self):
        # Custom Fonts
        title_font = ("Helvetica", 20, "bold")
        label_font = ("Helvetica", 12)
        button_font = ("Helvetica", 12, "bold")

        # Colors
        bg_color = "#2E3440"  # Dark background
        fg_color = "#D8DEE9"  # Light text
        accent_color = "#5E81AC"  # Blue accent
        button_color = "#81A1C1"  # Light blue button

        # Title Label
        title_label = tk.Label(
            self.root,
            text="Cryptify",
            font=title_font,
            bg=bg_color,
            fg=accent_color,
        )
        title_label.pack(pady=20)

        # Text Entry
        tk.Label(
            self.root,
            text="Enter Text:",
            font=label_font,
            bg=bg_color,
            fg=fg_color,
        ).pack()
        self.entry_text = tk.Text(
            self.root,
            height=5,
            width=50,
            font=label_font,
            bg="#4C566A",  # Darker background for text box
            fg=fg_color,
            insertbackground=fg_color,  # Cursor color
        )
        self.entry_text.pack(pady=10)

        # Key Entry
        tk.Label(
            self.root,
            text="Enter Key:",
            font=label_font,
            bg=bg_color,
            fg=fg_color,
        ).pack()
        self.entry_key = tk.Entry(
            self.root,
            font=label_font,
            bg="#4C566A",
            fg=fg_color,
            insertbackground=fg_color,
        )
        self.entry_key.pack(pady=10)

        # Algorithm Selection
        tk.Label(
            self.root,
            text="Select Algorithm:",
            font=label_font,
            bg=bg_color,
            fg=fg_color,
        ).pack()
        self.algorithm_var = tk.StringVar(value="Caesar")
        algorithms = [("Caesar Cipher", "Caesar"), ("Affine Cipher", "Affine")]
        for text, value in algorithms:
            tk.Radiobutton(
                self.root,
                text=text,
                variable=self.algorithm_var,
                value=value,
                font=label_font,
                bg=bg_color,
                fg=fg_color,
                selectcolor=bg_color,
                activebackground=bg_color,
                activeforeground=fg_color,
            ).pack()

        # Mode Selection
        tk.Label(
            self.root,
            text="Select Mode:",
            font=label_font,
            bg=bg_color,
            fg=fg_color,
        ).pack()
        self.mode_var = tk.StringVar(value="encrypt")
        modes = [("Encrypt", "encrypt"), ("Decrypt", "decrypt")]
        for text, value in modes:
            tk.Radiobutton(
                self.root,
                text=text,
                variable=self.mode_var,
                value=value,
                font=label_font,
                bg=bg_color,
                fg=fg_color,
                selectcolor=bg_color,
                activebackground=bg_color,
                activeforeground=fg_color,
            ).pack()

        # Process Button
        process_button = tk.Button(
            self.root,
            text="Process",
            font=button_font,
            bg=button_color,
            fg=bg_color,
            activebackground=accent_color,
            activeforeground=bg_color,
            command=self.process_text,
        )
        process_button.pack(pady=20)

        # Result Display
        tk.Label(
            self.root,
            text="Result:",
            font=label_font,
            bg=bg_color,
            fg=fg_color,
        ).pack()
        self.result_text = tk.Text(
            self.root,
            height=5,
            width=50,
            font=label_font,
            bg="#4C566A",
            fg=fg_color,
            insertbackground=fg_color,
        )
        self.result_text.pack(pady=10)

        # Copy to Clipboard Button
        copy_button = tk.Button(
            self.root,
            text="Copy to Clipboard",
            font=button_font,
            bg=button_color,
            fg=bg_color,
            activebackground=accent_color,
            activeforeground=bg_color,
            command=self.copy_to_clipboard,
        )
        copy_button.pack(pady=10)

    def process_text(self):
        text = self.entry_text.get("1.0", tk.END).strip()
        key = self.entry_key.get()
        algorithm = self.algorithm_var.get()
        mode = self.mode_var.get()

        if not text or not key:
            messagebox.showwarning("Input Error", "Please enter text and key.")
            return

        try:
            if algorithm == "Caesar":
                key = int(key)
                result = caesar_cipher(text, key, mode)
            elif algorithm == "Affine":
                key_a, key_b = map(int, key.split(','))
                result = affine_cipher(text, key_a, key_b, mode)
            else:
                result = "Invalid algorithm selected."
        except ValueError:
            result = "Invalid key format."

        self.result_text.delete("1.0", tk.END)
        self.result_text.insert(tk.END, result)

    def copy_to_clipboard(self):
        result = self.result_text.get("1.0", tk.END).strip()
        if result:
            self.root.clipboard_clear()
            self.root.clipboard_append(result)
            messagebox.showinfo("Copied", "Result copied to clipboard!")
        else:
            messagebox.showwarning("Copy Error", "No result to copy.")

    def run(self):
        self.root.mainloop()