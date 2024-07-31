import tkinter as tk
from tkinter import ttk
import pandas as pd

class RealEstateApp:
    def __init__(self, root, df):
        self.root = root
        self.df = df
        self.root.title("Real Estate Listings")
        
        self.tree = ttk.Treeview(root)
        self.tree['columns'] = ('Title', 'Location', 'Rent Price', 'Admin Fee', 'Rooms', 'Size')

        self.tree.column("#0", width=0, stretch=tk.NO)
        self.tree.column("Title", anchor=tk.W, width=200)
        self.tree.column("Location", anchor=tk.W, width=200)
        self.tree.column("Rent Price", anchor=tk.CENTER, width=100)
        self.tree.column("Admin Fee", anchor=tk.CENTER, width=100)
        self.tree.column("Rooms", anchor=tk.CENTER, width=100)
        self.tree.column("Size", anchor=tk.CENTER, width=100)

        self.tree.heading("#0", text="", anchor=tk.W)
        self.tree.heading("Title", text="Title", anchor=tk.W)
        self.tree.heading("Location", text="Location", anchor=tk.W)
        self.tree.heading("Rent Price", text="Rent Price", anchor=tk.CENTER)
        self.tree.heading("Admin Fee", text="Admin Fee", anchor=tk.CENTER)
        self.tree.heading("Rooms", text="Rooms", anchor=tk.CENTER)
        self.tree.heading("Size", text="Size", anchor=tk.CENTER)

        for idx, row in df.iterrows():
            self.tree.insert("", tk.END, iid=idx, values=(row['title'], row['location'], row['rent_price'], row['admin_fee'], row['rooms'], row['size']))

        self.tree.pack(pady=20)

def main():
    df = pd.read_csv('data/processed/otodom_data.csv')
    root = tk.Tk()
    app = RealEstateApp(root, df)
    root.mainloop()

if __name__ == "__main__":
    main()
