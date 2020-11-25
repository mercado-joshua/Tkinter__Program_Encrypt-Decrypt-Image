#===========================
# Imports
#===========================
import tkinter as tk
from tkinter import ttk, colorchooser as cc, Menu, Spinbox as sb, scrolledtext as st, messagebox as mb, filedialog as fd, simpledialog as sd

#===========================
# Main App
#===========================
class App(tk.Tk):
    """Main Application."""
    #------------------------------------------
    # Initializer
    #------------------------------------------
    def __init__(self):
        super().__init__()
        self.init_config()
        self.init_widgets()

    #-------------------------------------------
    # Window Settings
    #-------------------------------------------
    def init_config(self):
        self.resizable(False, False)
        self.title('Encrypt/Decrypt Image Version 1.0')
        self.iconbitmap('python.ico')
        self.style = ttk.Style(self)
        self.style.theme_use('clam')

    #-------------------------------------------
    # Widgets / Components
    #-------------------------------------------
    def init_widgets(self):
        self.frame = ttk.Frame(self)
        self.frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        label = ttk.Label(self.frame, text='Type your passphrase:')
        label.pack(side=tk.TOP, anchor=tk.W)

        self.entry = ttk.Entry(self.frame)
        self.entry.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5, ipady=5)

        button = ttk.Button(self.frame, text='Encrypt/Decrypt Image', command=self.encrypt_image)
        button.pack(side=tk.TOP, fill=tk.X, padx=5, pady=(0, 5))

    def encrypt_image(self):
        file1 = fd.askopenfile(mode='r', filetype=(('jpg file', '*.jpg'), ('png file', '*.png')))
        filename = file1.name
        # print(filename)

        key = self.entry.get()
        # print(key)

        # read the file
        with open(filename, 'rb') as file:
            image = file.read()

        # convert image to byte
        image = bytearray(image)
        for index, values in enumerate(image):
            image[index] = values^int(key) # xor / interchanging operator

        # write the file
        with open(filename, 'wb') as file:
            file.write(image)

#===========================
# Start GUI
#===========================
def main():
    app = App()
    app.mainloop()

if __name__ == '__main__':
    main()