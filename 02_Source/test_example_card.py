import customtkinter as ctk

from UI.Cards import ExampleCard

app = ctk.CTk()

app.geometry("900x600")

example = {

    "title": "Ví dụ 1",

    "content":

    "Cho hàm số y = 2x + 3.\n\n"

    "Xác định chiều của đồ thị.\n\n"

    "Ta có a = 2 > 0.\n"

    "Vì vậy đồ thị đi lên từ trái sang phải."

}

card = ExampleCard(
    app,
    example
)

card.pack(
    fill="x",
    padx=20,
    pady=20
)

app.mainloop()