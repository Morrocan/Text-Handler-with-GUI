import tkinter as tk 
from tkinter import filedialog, messagebox  # <- En gros ici on importe 2 sous-modules, filedialog et messagebox.

# Madame Samah nous a dit de créer la classe FileManager qui doit contenir -> Un attribut pour stocker le chemin du fichier + 4 méthodes (rwcs)

# init pour initialiser les attributs de l'objet -> self pour accéder aux attributs et méthodes de l'objet
# interaction avec un objet externe

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
        self.open_button = tk.Button(master, text="Ouvrir un fichier", command=self.open_file)
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

    # **Enlève l'indentation ici pour que la méthode soit au niveau de la classe** 
    def open_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Fichier Texte", "*.txt")])
        if self.file_path:
            try:
                with open(self.file_path, 'r') as file:
                    content = file.read()
                    self.text_area.delete(1.0, tk.END)
                    self.text_area.insert(tk.END, content)
            except Exception as e:
                messagebox.showerror("Erreur", f"Erreur lors de l'ouverture de fichier : {e}")

    # **Enlève l'indentation ici pour que la méthode soit au niveau de la classe** 
    def save_file(self):
        if self.file_path:
            try:
                with open(self.file_path, 'w') as file:
                    content = self.text_area.get(1.0, tk.END)
                    file.write(content)
                    messagebox.showinfo("Succès", "Fichier sauvegardé avec succès.")
            except Exception as e:
                messagebox.showerror("Erreur", f"Erreur lors de la sauvegarde du fichier : {e}")
        else:
            messagebox.showwarning("Avertissement", "Veuillez d'abord ouvrir un fichier.")

    # **Enlève l'indentation ici pour que la méthode soit au niveau de la classe** 
    def count_lines(self):
        if self.file_path:
            try:
                with open(self.file_path, 'r') as file:
                    lines = file.readlines()
                    line_count = len(lines)
                    messagebox.showinfo("Nbr de lignes", f"Nombre de lignes : {line_count}")
            except Exception as e:
                messagebox.showerror("Erreur", f"Erreur lors du comptage des lignes : {e}")
        else:
            messagebox.showwarning("Attention", "Veuillez d'abord ouvrir un fichier.")

    # **Enlève l'indentation ici pour que la méthode soit au niveau de la classe** 
    def search_keyword(self):
        keyword = self.keyword_entry.get()
        if self.file_path and keyword:
            try:
                with open(self.file_path, 'r') as file:
                    lines = file.readlines()
                    matches = [line for line in lines if keyword in line]
                    if matches:
                        resultat = "Lignes contenant '{}' :\n\n".format(keyword) + "\n".join(matches)
                        messagebox.showinfo("Résultats de la recherche", resultat)
                    else:
                        messagebox.showinfo("Résultats de la recherche", f"Aucune ligne ne contient le mot clé '{keyword}'.")
            except Exception as e:
                messagebox.showerror("Erreur", f"Erreur lors de la recherché du mot clé : {e}")
        else:
            messagebox.showwarning("Avertissement", "Veuillez d'abord ouvrir un fichier et entrer un mot-clé.")

# Exécution de l'application
if __name__ == "__main__":
    root = tk.Tk()
    app = FileManager(root)
    root.mainloop()
