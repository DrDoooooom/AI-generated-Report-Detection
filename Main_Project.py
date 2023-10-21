import tkinter as tk
from tkinter import filedialog, ttk
import pdfplumber
import spacy


class TextDetector:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def is_ai_text(self, text):
        """
        Uses the named entity recognition (NER) capability of the spaCy library to classify text as either AI-generated or human-written.
        Returns True if the predicted entity is 'ORG', indicating AI-generated text.
        """
        doc = self.nlp(text)
        for ent in doc.ents:
            if ent.label_ == 'ORG':
                return True
        return False


class MainApplication:
    def __init__(self):
        self.text_detector = TextDetector()

        # Create the main window
        self.root = tk.Tk()
        self.root.configure(bg="black")
        self.root.title("AI Gnerated Report Detection")
        self.root.geometry('500x500')

        # Browse button
        self.browse_button = ttk.Button(self.root, text="Browse File", command=self.browse_file)
        self.browse_button.grid(row=0, column=0, padx=10, pady=10, sticky='n')

        # Result label
        self.result_label = tk.Label(self.root, text="", bg="black", fg="white", font=("Arial", 12, "bold"))
        self.result_label.grid(row=1, column=0, padx=10, pady=10, sticky='n')

        # Center the widgets in the window
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.browse_button.grid(pady=(150, 10))
        self.result_label.grid(pady=10)

        # Start the GUI event loop
        self.root.mainloop()

    def browse_file(self):
        """
        Opens a file dialog box and reads the contents of the selected file.
        Performs AI detection on the text and updates the result label.
        """
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, 'rb') as file:
                if file_path.endswith('.pdf'):
                    text = self.read_pdf(file)
                else:
                    text = file.read().decode('utf-8', errors='ignore')
                if self.text_detector.is_ai_text(text):
                    self.result_label.configure(text="The text is likely written by AI.", foreground="red")
                else:
                    self.result_label.configure(text="The text is likely written by a human.", foreground="green")

    def read_pdf(self, file):
        """
        Reads the text contents of a PDF file using pdfplumber library.
        """
        with pdfplumber.open(file) as pdf:
            text = ''
            for page in pdf.pages:
                text += page.extract_text()
            return text


if __name__ == '__main__':
    app = MainApplication()
