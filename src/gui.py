import customtkinter as ctk
import pandas as pd

def display_listings(df):
    app = ctk.CTk()
    app.title("Past Real Estate Listings")
    app.geometry("800x600")


    frame = ctk.CTkFrame(app)
    frame.pack(pady=20, padx=20, fill="both", expand=True)
    scrollbar = ctk.CTkScrollbar(frame)
    scrollbar.pack(side="right", fill="y")

    listbox = ctk.CTkListbox(frame, yscrollcommand=scrollbar.set)
    listbox.pack(side="left", fill="both", expand=True)
    scrollbar.config(command=listbox.yview)


    for index, row in df.iterrows():
        listbox.insert(
            "end",
            f"Title: {row['title']}\n"
            f"Location: {row['location']}\n"
            f"Rent Price: {row['rent_price']} PLN\n"
            f"Admin Fee: {row['admin_fee']} PLN\n"
            f"Rooms: {row['rooms']}\n"
            f"Size: {row['size']} m²\n"
            "----------------------------------------"
        )
    app.mainloop()
