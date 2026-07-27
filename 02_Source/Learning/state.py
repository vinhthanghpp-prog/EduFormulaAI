"""
Learning Runtime State
EduFormula AI
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class LessonState:
    """
    Lưu trạng thái hiện tại của bài học.
    Không chứa logic xử lý.
    """

    lesson_id: str = ""
    lesson_title: str = ""

    current_step: int = 0
    total_steps: int = 0

    completed: bool = False
    score: float = 0.0

    started_at: Optional[datetime] = None
    finished_at: Optional[datetime] = None

    metadata: dict = field(default_factory=dict)

    @property
    def progress(self) -> float:
        """
        Tiến độ (%)
        """

        if self.total_steps <= 0:
            return 0.0

        return round(
            self.current_step / self.total_steps * 100,
            2
        )