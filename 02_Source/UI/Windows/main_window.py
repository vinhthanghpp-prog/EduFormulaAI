import customtkinter as ctk

from Modules.Shared.subjects import SUBJECTS

from UI.Components.lesson_viewer import LessonViewer
from UI.Components.lesson_selector import LessonSelector

from Services import LessonCatalogService

from Modules.Lessons.Math.Grade10.linear_function import get_lesson

from UI.Components import LessonSelector
from Core.Navigation import NavigationController


class MainWindow(ctk.CTk):
    """
    Cửa sổ chính của EduFormula AI
    """

    def __init__(self):
        super().__init__()

        self.title("EduFormula AI")
        self.geometry("1200x800")

        # Grid
        self.grid_rowconfigure(1, weight=1)

        # Sidebar
        self.grid_columnconfigure(0, weight=0, minsize=240)

        # Workspace
        self.grid_columnconfigure(1, weight=1)

        self.create_header()
        self.create_sidebar()
        self.create_workspace()
        self.create_statusbar()

    # ==================================================
    # Header
    # ==================================================
    def create_header(self):

        self.header = ctk.CTkFrame(
            self,
            height=50,
            corner_radius=0
        )

        self.header.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="nsew"
        )

        title = ctk.CTkLabel(
            self.header,
            text="EduFormula AI",
            font=("Segoe UI", 28, "bold")
        )

        title.pack(
            side="left",
            padx=20,
            pady=10
        )

    # ==================================================
    # Sidebar
    # ==================================================
    def create_sidebar(self):

        self.sidebar = ctk.CTkFrame(
            self,
            width=240,
            corner_radius=0
        )

        self.sidebar.grid(
            row=1,
            column=0,
            sticky="nsew"
        )

        self.sidebar.grid_propagate(False)

        title = ctk.CTkLabel(
            self.sidebar,
            text="MÔN HỌC",
            font=("Segoe UI", 20, "bold")
        )

        title.pack(
            pady=(25, 25)
        )

        # Tạo nút từ dữ liệu
        for subject_name, info in SUBJECTS.items():

            button = ctk.CTkButton(
                self.sidebar,
                text=f'{info["icon"]}  {subject_name}',
                height=42,
                command=lambda name=subject_name: self.show_subject(name)
            )

            button.pack(
                fill="x",
                padx=18,
                pady=6
            )

    # ==================================================
    # Workspace
    # ==================================================
    def create_workspace(self):

        self.workspace = ctk.CTkFrame(self)

        self.workspace.grid(
            row=1,
            column=1,
            sticky="nsew",
            padx=5,
            pady=5
        )

        self.workspace.grid_columnconfigure(0, weight=1)
        self.workspace.grid_columnconfigure(1, weight=3)
        self.workspace.grid_rowconfigure(0, weight=1)

        self.selector_panel = ctk.CTkFrame(self.workspace)

        self.selector_panel.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(10,5),
            pady=10
        )

        self.viewer_panel = ctk.CTkFrame(self.workspace)

        self.viewer_panel.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=(5,10),
            pady=10
        )

        self.lesson_selector = LessonSelector(
            self.selector_panel,
            on_select=self.on_lesson_selected
        )

        self.lesson_selector.pack(
            fill="both",
            expand=True
        )

        self.lesson_viewer = LessonViewer(
            self.viewer_panel
        )

        self.lesson_viewer.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        self.catalog_service = LessonCatalogService()

        self.navigation = NavigationController(
            self.lesson_viewer
        )   

               
    # ==================================================
    # Status Bar
    # ==================================================
    def create_statusbar(self):

        self.statusbar = ctk.CTkFrame(
            self,
            height=28,
            corner_radius=0
        )

        self.statusbar.grid(
            row=2,
            column=0,
            columnspan=2,
            sticky="ew"
        )

        label = ctk.CTkLabel(
            self.statusbar,
            text="CORE-0.1A      Ready"
        )

        label.pack(
            side="left",
            padx=10
        )

    # ==================================================
    # Dashboard
    # ==================================================
    def show_subject(self, subject_name):

        if subject_name == "Toán":

            lessons = self.catalog_service.get_lessons(
                "Grade10"
            )

            self.lesson_selector.load_lessons(
                lessons
            )

        else:

            self.lesson_selector.load_lessons([])

            self.lesson_viewer.load_lesson(
                {
                    "metadata": {
                        "title": subject_name
                    },

                    "formula": {
                        "expression": ""
                    },

                    "concept": {
                        "content": "Nội dung đang được xây dựng..."
                    }
                }
            )

    def on_lesson_selected(self, lesson):

        self.navigation.open_lesson(
            subject="Toán",
            grade=10,
            lesson_id=lesson["id"]
        )

    def on_lesson_selected(self, lesson):

        self.navigation.open_lesson(
            subject="Toán",
            grade=10,
            lesson_id=lesson["id"]
        )