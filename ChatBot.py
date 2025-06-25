import tkinter as tk
from tkinter import scrolledtext
import google.generativeai as go

# ========== Configure Gemini API ==========
API_KEY = "AIzaSyAlSejBp5MIMKzfRFb78vPY0hLG-_zK4bw"
go.configure(api_key=API_KEY)
model = go.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat()

# ========== Send Message Function ==========
def send_message():
    user_msg = user_input.get()
    if user_msg.strip() == "":
        return
    if user_msg.lower() == "exit":
        root.destroy()
        return
    chat_display.insert(tk.END, f"You: {user_msg}\n", "user")
    user_input.delete(0, tk.END)

    response = chat.send_message(user_msg)
    chat_display.insert(tk.END, f"Go: {response.text}\n\n", "bot")
    chat_display.see(tk.END)

# ========== GUI Setup ==========
root = tk.Tk()
root.title("💬 Gemini Chat")
root.geometry("600x600")
root.configure(bg="#f4f4f4")  # Soft light background

# ========== Fonts & Styles ==========
FONT = ("Segoe UI", 12)
HEADER_FONT = ("Segoe UI Semibold", 14)

# ========== Chat Display ==========
chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=FONT, bg="#e2f073", fg="#333333", padx=10, pady=10)
chat_display.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)
chat_display.tag_config("user", foreground="#0066cc", font=("Segoe UI", 12, "bold"))
chat_display.tag_config("bot", foreground="#444444", font=("Segoe UI", 12))
chat_display.config(state=tk.NORMAL)

# ========== User Input Box ==========
input_frame = tk.Frame(root, bg="#f4f4f4")
input_frame.pack(padx=20, pady=10, fill=tk.X)

user_input = tk.Entry(input_frame, font=FONT, bg="#ffffff", fg="#000000", relief=tk.FLAT, highlightthickness=1, highlightbackground="#cccccc")
user_input.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10), ipady=8)
user_input.focus()

# ========== Send Button ==========
send_button = tk.Button(input_frame, text="Send", font=HEADER_FONT, bg="#0066cc", fg="white", activebackground="#005bb5", activeforeground="white", padx=20, pady=8, relief=tk.FLAT, command=send_message)
send_button.pack(side=tk.RIGHT)

# ========== Key Binding ==========
root.bind('<Return>', lambda event: send_message())

# ========== Run ==========
root.mainloop()
