import customtkinter as ctk


class LessonSelector(ctk.CTkFrame):

    def __init__(self, parent, on_select=None):

        super().__init__(parent)

        self.on_select = on_select

        self.title = ctk.CTkLabel(
            self,
            text="📚 Danh sách bài học",
            font=("Segoe UI", 22, "bold")
        )

        self.title.pack(pady=(20, 15))

        self.lesson_frame = ctk.CTkFrame(self)

        self.lesson_frame.pack(fill="both", expand=True)

    def load_lessons(self, lessons):

        for widget in self.lesson_frame.winfo_children():
            widget.destroy()

        for lesson in lessons:

            btn = ctk.CTkButton(
                self.lesson_frame,
                text=f'{lesson["id"]}. {lesson["title"]}',
                height=40,
                command=lambda l=lesson: self.select_lesson(l)
            )

            btn.pack(fill="x", padx=20, pady=5)

    def select_lesson(self, lesson):

        if self.on_select:
            self.on_select(lesson)