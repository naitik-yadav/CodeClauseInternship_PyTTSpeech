import pyttsx3
import tkinter as tk
from tkinter import ttk


def convert_text_to_speech():
    text = text_entry.get()
    selected_voice = voice_var.get()
    rate = rate_var.get()

    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    if selected_voice == 'Male':
        engine.setProperty('voice', voices[0].id)
    elif selected_voice == 'Female':
        engine.setProperty('voice', voices[1].id)

    engine.setProperty('rate', rate)

    engine.say(text)
    engine.runAndWait()


app = tk.Tk()
app.title("Text-to-Speech Converter")

# Create and place widgets in the window
text_label = tk.Label(app, text="Enter text:")
text_label.pack(pady=10)

text_entry = tk.Entry(app, width=50)
text_entry.pack(pady=10)

voice_label = tk.Label(app, text="Select voice:")
voice_label.pack(pady=10)

voices = ['Male', 'Female']
voice_var = tk.StringVar(value=voices[0])

voice_menu = ttk.Combobox(app, textvariable=voice_var, values=voices)
voice_menu.pack(pady=10)

rate_label = tk.Label(app, text="Speech rate:")
rate_label.pack(pady=10)

rate_var = tk.IntVar(value=150)

rate_slider = tk.Scale(app, from_=50, to=300, variable=rate_var, orient=tk.HORIZONTAL, label="Rate")
rate_slider.pack(pady=10)

convert_button = tk.Button(app, text="Convert to Speech", command=convert_text_to_speech)
convert_button.pack(pady=20)

app.mainloop()
