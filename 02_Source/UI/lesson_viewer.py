"""
Lesson Viewer
BUILD-049A Official Release
"""

from Modules.Renderer.lesson_view_renderer import LessonViewRenderer

class LessonViewer:

    def __init__(self, parent=None):

        self.parent = parent

        self.renderer = LessonViewRenderer(parent)

        self.lesson = None

        self.cards = []

        self.display_cards = []

        self.container = []

    def load_lesson(self, lesson):

        self.lesson = lesson

    def load_content(self, content):

        self.load_lesson(content)

        blocks = self.get_content_blocks()

        self.cards = self.renderer.render(blocks)

        self.display_cards = self.cards

        self.refresh_display()

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

    def get_display_cards(self):

        return self.display_cards

    def refresh_display(self):

        self.refresh_called = True

        # Đồng bộ container với display_cards
        self.container.clear()
        self.container.extend(self.display_cards)

        return self.display_cards