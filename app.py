import tkinter as tk 
from tkinter import filedialog, messagebox # <- En gros ici on importe 2 sous-modules, filedialog et messagebox.

# Madame Samah nous a dit de créer la classe FileManager qui doit contenir -> Un attribut pour stocker le chemin du fichier + 4 méthodes (rwcs)

class FileManager:
    def __init__(self, master):
        self.master = master
        self.master.title("Gestionnaire de fichiers")
        self.file_path = None

# On va maintenant créer les éléments de l'interface 

        self.label = tk.Label(master, text="Gestionnaire de fichiers TXT")
        self.label.pack(pady=10)
        self.text_area = tk.Text(master, height=15, width=50)
        self.text_area.pack(pady=10)

# Création des boutons de l'interface tkinter

        self.open_button = tk.Button(master, text="Ouvrir un fichier", command=self.file_path)
        self.open_button.pack(pady=5)

        self.save_button = tk.Button(master, text="Sauvegarder", command=self.save_file)
        self.save_button.pack(pady=5)

        self.count_button = tk.Button(master, text="Compter les lignes", command=self.count_lines)
        self.count_button.pack(pady=5)

        self.search_button = tk.Button(master, text="Rechercher un mot-clé", command=self.search_keyword)
        self.search_button.pack(pady=5)

        self.keyword_entry = tk.Entry(master)
        self.keyword_entry.pack(pady=5)

        self.keyword_entry.insert(0, "Entrez le mot-clé ici")

# Maintenant on va écrire les 4 méthodes !

        def file_path(self):
                self.file_path = filedialog.askopenfilename(filetypes=[("Fichier Texte","*.txt")])
                if self.file_path:
                        try:
                                with open(self.file_path, 'r') as file:
                                        content = file.read()
                                        self.text_area.delete(1.0, tk.END)
                                        self.text_area.insert(tk.END, content)
                        except Exception as e:
                                tkinter.messagebox.showerror("Erreur", f"Erreur lors de l'ouverture de fichier : {e}")

# Sauvegarde le contenu de la zone texte dans fichier

        def save_file(self):
                if self.file_path:
                        try:
                                with open(self.file_path, 'w') as file:
                                        content = self.text_area.get(1.0, tk.END)
                                        file.write(content)
                                        message.boxshowinfo("Succès", "Fichier sauvegardé avec succès.")
                                except Exception as e:
                                        messagebox.showerror("Erreur",f"Erreur lors de la sauvegarde du fichier : {e}")
                else:
                        messagebox.showwarning("Avertissement", "Veuillez d'abord ouvrir un fichier.")
