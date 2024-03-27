import tkinter as tk
from tkinter import messagebox, ttk, simpledialog
from cryptography.fernet import Fernet

try:
    with open('key.txt', 'rb') as file:
        key = file.read()
except FileNotFoundError:
    key = Fernet.generate_key()
    with open('key.txt', 'wb') as file:
        file.write(key)

fernet = Fernet(key)

site_web_entry = None
nom_utilisateur_entry = None
mot_de_passe_entry = None


def chiffrer_mot_de_passe(chaine):
    encryptage = fernet
    return encryptage.encrypt(chaine.encode('utf-8'))

def dechiffrer_mot_de_passe(chaine_crypter):
    decryptage = fernet
    return decryptage.decrypt(chaine_crypter).decode('utf-8')


def afficher_gestionnaire():
    global site_web_entry, nom_utilisateur_entry, mot_de_passe_entry

    fenetre = tk.Tk()
    fenetre.title("Gestionnaire de mots de passe")


    container = tk.Frame(fenetre)
    container.pack(padx=10, pady=10)
    site_web_label = tk.Label(container, text="Site Web:")
    site_web_label.pack(pady=(10, 0))
    site_web_entry = tk.Entry(container)
    site_web_entry.pack(pady=5, fill='x')
    nom_utilisateur_label = tk.Label(container, text="Nom d'utilisateur:")
    nom_utilisateur_label.pack()
    nom_utilisateur_entry = tk.Entry(container)
    nom_utilisateur_entry.pack(pady=5, fill='x')
    mot_de_passe_label = tk.Label(container, text="Mot de passe:")
    mot_de_passe_label.pack()
    mot_de_passe_entry = tk.Entry(container, show='*')
    mot_de_passe_entry.pack(pady=5, fill='x')
    ajouter_bouton = tk.Button(container, text="Ajouter mot de passe", command=ajouter_mot_de_passe)
    ajouter_bouton.pack(pady=10)
    afficher_bouton = tk.Button(container, text="Afficher les mots de passe", command=afficher_mots_de_passe)
    afficher_bouton.pack(pady=10)
    quitter_bouton = tk.Button(container, text="Quitter le programme", command=fenetre.quit)
    quitter_bouton.pack(pady=10)

    fenetre.mainloop()


def ajouter_mot_de_passe():
    site_web = site_web_entry.get()
    nom_utilisateur = nom_utilisateur_entry.get()
    mot_de_passe = mot_de_passe_entry.get()

    if site_web and nom_utilisateur and mot_de_passe:
        site_web_chiffre = chiffrer_mot_de_passe(site_web)
        nom_utilisateur_chiffre = chiffrer_mot_de_passe(nom_utilisateur)
        mot_de_passe_chiffre = chiffrer_mot_de_passe(mot_de_passe)

        with open("mots_de_passe.txt", "ab") as fichier:
            site_web_chiffre = site_web_chiffre.lstrip(b"b'").rstrip(b"'")
            nom_utilisateur_chiffre = nom_utilisateur_chiffre.lstrip(b"b'").rstrip(b"'")
            mot_de_passe_chiffre = mot_de_passe_chiffre.lstrip(b"b'").rstrip(b"'")

            ligne = f"{site_web_chiffre.decode()}gestion{nom_utilisateur_chiffre.decode()}gestion{mot_de_passe_chiffre.decode()}\n"
            fichier.write(ligne.encode('utf-8'))

        site_web_entry.delete(0, tk.END)
        nom_utilisateur_entry.delete(0, tk.END)
        mot_de_passe_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")


def afficher_mots_de_passe():
    mots_de_passe = []

    fenetre_mots_de_passe = tk.Toplevel()
    fenetre_mots_de_passe.title("Mots de passe")
    tableau = ttk.Treeview(fenetre_mots_de_passe, columns=("Nom d'utilisateur", "Mot de passe"))
    tableau.heading("#0", text="Site Web")
    tableau.heading("#1", text="Nom d'utilisateur")
    tableau.heading("#2", text="Mot de passe")
    tableau.pack()

    def afficher_mot_de_passe_reel():
        selection = tableau.selection()
        if selection:
            index = tableau.index(selection)
            mot_de_passe_reel = mots_de_passe[index]
            messagebox.showinfo("Mot de passe sélectionné", mot_de_passe_reel)
        else:
            messagebox.showinfo("Information", "Sélectionnez d'abord une ligne.")

    def supprimer_ligne_selectionnee():
        selection = tableau.selection()
        if selection:
            index = tableau.index(selection)
            with open("mots_de_passe.txt", "r") as fichier:
                lignes = fichier.readlines()
            with open("mots_de_passe.txt", "w") as fichier:
                for i, ligne in enumerate(lignes):
                    if i != index:
                        fichier.write(ligne)
            tableau.delete(selection)
        else:
            messagebox.showinfo("Information", "Sélectionnez d'abord une ligne.")



    def modifier_mot_de_passe():
        selection = tableau.selection()
        if selection:
            site_web = tableau.item(selection, "text")
            nom_utilisateur = tableau.item(selection, "values")[0]
            ancien_mot_de_passe = tableau.item(selection, "values")[1]
            supprimer_ligne_selectionnee()
            new_site_web = simpledialog.askstring("Modifier le site web",f"Site Web: {site_web}\nNom d'utilisateur: {nom_utilisateur}\nAncien mot de passe: {ancien_mot_de_passe}\nNouveau site web:")
            if new_site_web is not None:
                new_nom_utilisateur = simpledialog.askstring("Modifier le nom d'utilisateur",f"Site Web: {new_site_web}\nAncien nom d'utilisateur: {nom_utilisateur}\nNouveau nom d'utilisateur:")
                if new_nom_utilisateur is not None:
                    new_mot_de_passe = simpledialog.askstring("Modifier le mot de passe", f"Site Web: {new_site_web}\nNom d'utilisateur: {new_nom_utilisateur}\nAncien mot de passe: {ancien_mot_de_passe}\nNouveau mot de passe:")
                    if new_mot_de_passe is not None:
                        new_site_web_chiffre = chiffrer_mot_de_passe(new_site_web)
                        new_nom_utilisateur_chiffre = chiffrer_mot_de_passe(new_nom_utilisateur)
                        new_mot_de_passe_chiffre = chiffrer_mot_de_passe(new_mot_de_passe)
                        with open("mots_de_passe.txt", "a") as fichier:
                            fichier.write(
                                f"{new_site_web_chiffre.decode()}gestion{new_nom_utilisateur_chiffre.decode()}gestion{new_mot_de_passe_chiffre.decode()}\n")

                        tableau.insert("", "end", text=new_site_web, values=(new_nom_utilisateur, new_mot_de_passe))
            else:
                messagebox.showinfo("Information", "Sélectionnez d'abord une ligne.")

    with open("mots_de_passe.txt", "rb") as fichier:
        mots_de_passe_chiffres = fichier.readlines()
        for info in mots_de_passe_chiffres:
            try:
                site_web_chiffre, nom_utilisateur_chiffre, mot_de_passe_chiffre = info.split(b'gestion')
                site_web = dechiffrer_mot_de_passe(site_web_chiffre)
                nom_utilisateur = dechiffrer_mot_de_passe(nom_utilisateur_chiffre)
                mot_de_passe = dechiffrer_mot_de_passe(mot_de_passe_chiffre)
                mots_de_passe.append(mot_de_passe)
                mot_de_passe_masque = '*' * len(mot_de_passe)
                tableau.insert("", "end", text=site_web, values=(nom_utilisateur, mot_de_passe_masque))
            except Exception as e:
                print(f"Erreur lors du déchiffrement : {e}")
                messagebox.showerror("Erreur", "Impossible de déchiffrer un mot de passe.")

    afficher_mot_bouton = tk.Button(fenetre_mots_de_passe, text="Afficher le mot de passe sélectionné",command=afficher_mot_de_passe_reel)
    afficher_mot_bouton.pack()
    modifier_bouton = tk.Button(fenetre_mots_de_passe, text="Modifier", command=modifier_mot_de_passe)
    modifier_bouton.pack()
    supprimer_bouton = tk.Button(fenetre_mots_de_passe, text="Supprimer la ligne sélectionnée",command=supprimer_ligne_selectionnee)
    supprimer_bouton.pack()

    tableau.column("#0", width=150)
    tableau.column("#1", width=150)
    tableau.column("#2", width=150)

    fenetre_mots_de_passe.mainloop()


def quitter_programme():
    fenetre.quit()


afficher_gestionnaire()
