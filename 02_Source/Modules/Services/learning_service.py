"""
EduFormula AI

Subsystem:
Service Layer

Module:
Learning Service

Version:
1.0

Status:
Development
"""

from Modules.Pipeline import LearningPipeline


class LearningService:
    """
    Public API cho toàn bộ quá trình học.
    """

    def __init__(self):

        self.pipeline = LearningPipeline()

    # -------------------------------------

    def create_session(
        self,
        lesson,
        problem
    ):
        """
        Tạo một Learning Session mới.
        """

        return self.pipeline.create_session(
            lesson,
            problem
        )

    # -------------------------------------

    def next_step(
        self,
        session
    ):
        return self.pipeline.next_step(
            session
        )