import customtkinter as ctk

from Modules.Engine import LessonRenderer


lesson = {

    "objectives":[

        "Hiểu khái niệm hàm số bậc nhất.",

        "Hiểu ý nghĩa hệ số a.",

        "Nhận biết đồ thị."
    ]

}


app = ctk.CTk()

app.geometry("700x500")

frame = ctk.CTkScrollableFrame(app)

frame.pack(
    fill="both",
    expand=True
)

renderer = LessonRenderer(frame)

renderer.render(
    lesson
)

app.mainloop()