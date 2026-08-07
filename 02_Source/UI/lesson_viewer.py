"""
Lesson Viewer
BUILD-047A Official Release
"""


class LessonViewer:

    def __init__(self):

        self.lesson = None

    def load_lesson(self, lesson):

        self.lesson = lesson

    def get_lesson_title(self):

        if self.lesson is None:
            return ""

        return self.lesson.metadata.lesson

"""
Lesson Viewer
BUILD-047A Official Release
"""


class LessonViewer:

    def __init__(self):

        self.lesson = None

    def load_lesson(self, lesson):

        self.lesson = lesson

    def get_lesson_title(self):

        if self.lesson is None:
            return ""

        return self.lesson.metadata.lesson

    def get_content_blocks(self):

        if self.lesson is None:
            return []

        if not self.lesson.learning_units:
            return []

        return self.lesson.learning_units[0].content_blocks