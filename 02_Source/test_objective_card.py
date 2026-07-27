import customtkinter as ctk

from UI.Cards import ObjectiveCard

app = ctk.CTk()

app.geometry("700x450")

card = ObjectiveCard(
    app,
    [
        "Hiểu khái niệm hàm số bậc nhất.",
        "Hiểu ý nghĩa hệ số a.",
        "Nhận biết đồ thị."
    ]
)

card.pack(
    fill="x",
    padx=20,
    pady=20
)

app.mainloop()