import customtkinter as ctk


class VariableViewer(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        self.title = ctk.CTkLabel(
            self,
            text="🧩 Thành phần công thức",
            font=("Segoe UI", 18, "bold")
        )
        self.title.pack(
            anchor="w",
            padx=20,
            pady=(20, 10)
        )

        self.container = ctk.CTkFrame(self)
        self.container.pack(
            fill="x",
            padx=20,
            pady=10
        )

    def load_variables(self, variables):

        # Xóa dữ liệu cũ
        for widget in self.container.winfo_children():
            widget.destroy()

        # Tạo danh sách biến
        for variable in variables:

            btn = ctk.CTkButton(
                self.container,
                text=f'{variable["symbol"]} - {variable["name"]}',
                anchor="w",
                height=36
            )

            btn.pack(
                fill="x",
                pady=5
            )