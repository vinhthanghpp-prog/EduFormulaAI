from UI.Windows.main_window import MainWindow


class Application:
    """
    Quản lý vòng đời của EduFormula AI.
    """

    def __init__(self):
        self.main_window = MainWindow()

    def run(self):
        self.main_window.mainloop()