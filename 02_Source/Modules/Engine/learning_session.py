"""
EduFormula AI

Learning Session

Version 2.1
"""


class LearningSession:
    """
    Quản lý toàn bộ trạng thái của một phiên học.
    """

    def __init__(
        self,
        learning_path,
        lesson=None,
        problem=None,
        context=None
    ):

        # --------------------------
        # Learning Information
        # --------------------------

        self.lesson = lesson
        self.problem = problem
        self.context = context

        # --------------------------
        # Teaching
        # --------------------------

        self.current_script = None

        # --------------------------
        # Learning Path
        # --------------------------

        self.learning_path = learning_path
        self.current_index = 0

        # --------------------------
        # Statistics
        # --------------------------

        self.completed = []
        self.mistakes = []
        self.history = []

    # =================================================
    # Learning Information
    # =================================================

    def get_lesson(self):
        return self.lesson

    def get_problem(self):
        return self.problem

    def get_context(self):
        return self.context

    # =================================================
    # Teaching Script
    # =================================================

    def set_current_script(self, script):

        self.current_script = script

    def get_current_script(self):

        return self.current_script

    # =================================================
    # Learning Step
    # =================================================

    def current_step(self):

        if self.current_index >= len(self.learning_path):
            return None

        return self.learning_path[self.current_index]

    def complete_current_step(self):

        step = self.current_step()

        if step:

            self.completed.append(step["step"])

            self.current_index += 1

    # =================================================
    # Learning Result
    # =================================================

    def add_mistake(self, skill):

        self.mistakes.append(skill)

    def is_finished(self):

        return self.current_index >= len(self.learning_path)

    def get_progress(self):

        return {

            "completed": len(self.completed),

            "total": len(self.learning_path),

            "mistakes": self.mistakes

        }