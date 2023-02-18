import random
import time
import tkinter as tk

matrice = tk.Tk()
matrice.title("MATRICE")
matrice.geometry("1080x720")
matrice.minsize(480,360)
matrice.configure(bg="black")

frame = tk.Frame(matrice)
frame.pack()

# Création de la matrice de labels
labels = []
for i in range(50):
    labels.append([])
    for j in range(50):
        labels[i].append(tk.Label(frame, text="", width=3,bg="black", foreground="green", font = ("Arial", 10)))
        labels[i][j].grid(row=i, column=j)

# Fonction de mise à jour de la matrice
def update_matrix():
    for i in range(50):
        for j in range(50):
            labels[i][j]["text"] = str(random.randint(1, 9))
    matrice.after(500, update_matrix)

# Mise à jour initiale de la matrice
update_matrix()

# Démarrage de la boucle Tkinter
matrice.mainloop()

