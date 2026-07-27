import customtkinter as ctk

from UI.Cards import BaseCard

app = ctk.CTk()

app.geometry("600x300")

card = BaseCard(
    app,
    "🎯 Mục tiêu"
)

card.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=20
)

ctk.CTkLabel(
    card.body,
    text="• Hiểu khái niệm hàm số bậc nhất."
).pack(anchor="w")

ctk.CTkLabel(
    card.body,
    text="• Hiểu ý nghĩa hệ số a."
).pack(anchor="w")

app.mainloop()