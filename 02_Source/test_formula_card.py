import customtkinter as ctk

from UI.Cards import FormulaCard

print("1. Import thành công")

app = ctk.CTk()
print("2. Tạo app")

app.geometry("800x500")

formula = {
    "expression": "y = ax + b",
    "description": "Biểu diễn mối quan hệ tuyến tính giữa x và y."
}

card = FormulaCard(app, formula)
print("3. Tạo FormulaCard")

card.pack(fill="x", padx=20, pady=20)
print("4. Pack thành công")

print("5. Bắt đầu mainloop")
app.mainloop()

print("6. Kết thúc")