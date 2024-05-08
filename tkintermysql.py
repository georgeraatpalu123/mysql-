import tkinter as tk
import sqlite3

def näita_andmed():
  
    conn = sqlite3.connect('andmebaas.db')
    c = conn.cursor()

   
    c.execute("SELECT * FROM andmed")
    andmed = c.fetchall()

    
    for i, rida in enumerate(andmed):
        nimi_silt = tk.Label(aken, text=rida[1])
        nimi_silt.grid(row=i, column=0)
        vanus_silt = tk.Label(aken, text=rida[2])
        vanus_silt.grid(row=i, column=1)


    conn.close()


aken = tk.Tk()
aken.title("Andmete kuvamine")


nupp = tk.Button(aken, text="Kuva andmed", command=näita_andmed)
nupp.grid(row=0, column=0)
e
aken.mainloop()
