# Import Libraries
import base64
from tkinter import *
import customtkinter

# Themes
customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

# Window Configuration
root = customtkinter.CTk()
root.title('Encode or Decode Base64')
root.geometry('600x300')
root.resizable(width=False, height=False)

# Functions
def encode():
    user_value = entry_text.get()
    a = f'{user_value}'
    encoded = base64.b64encode(bytes(f'{a}', 'utf-8'))
    answer_text.set(encoded)
    
def decode():
    user_value = entry_text.get()
    a = f'{user_value}'
    decoded = base64.b64decode(a).decode("utf-8")
    answer_text.set(decoded)

# String Variables
entry_text = StringVar()
answer_text = StringVar()

# Label: Instructions
inst1 = customtkinter.CTkLabel(root, text="Input encrypted/or plaintext here:") 
inst1.pack(pady="75", anchor='center')

# Entry: Input string for Encryption/Decryption
entry1 = customtkinter.CTkEntry(root, width=400, textvariable=entry_text) 
entry1.place(relx=0.5, rely=0.35, anchor=CENTER)

# Encode Button
encode_button = customtkinter.CTkButton(root, text="Encode Text", command=encode) 
encode_button.place(relx=0.35, rely=0.5, anchor=CENTER)

# Decode Button
decode_button = customtkinter.CTkButton(root, text="Decode Base64", command=decode) 
decode_button.place(relx=0.65, rely=0.5, anchor=CENTER)

# Results
ent = customtkinter.CTkEntry(root, width=400, textvariable=answer_text)
ent.place(relx=0.5, rely=0.65, anchor=CENTER)

root.mainloop()