import customtkinter as ctk

from UI.Cards import VariableCard

app = ctk.CTk()

app.geometry("800x650")

variable = {

    "symbol": "a",

    "name": "Hệ số góc",

    "meaning":
        "Cho biết độ dốc của đường thẳng.",

    "effect":
        "a > 0: Đồ thị đi lên\n"
        "a < 0: Đồ thị đi xuống\n"
        "|a| càng lớn thì đường càng dốc.",

    "unit": "",

    "tips": [
        "Nhìn dấu của a để xác định chiều của đồ thị."
    ]
}

card = VariableCard(
    app,
    variable
)

card.pack(
    fill="x",
    padx=20,
    pady=20
)

app.mainloop()