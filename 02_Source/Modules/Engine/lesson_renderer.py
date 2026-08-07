"""
EduFormula AI
Dynamic Lesson Renderer
"""

class LessonRenderer:

    def __init__(self):

        pass

    def render(self, learning_content):

        blocks = []

        for unit in learning_content.learning_units:
            blocks.extend(unit.content_blocks)

        return blocks