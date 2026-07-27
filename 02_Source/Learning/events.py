"""
Runtime Events
"""

from enum import Enum


class RuntimeEvent(str, Enum):

    LESSON_LOADED = "lesson_loaded"

    LESSON_STARTED = "lesson_started"

    STEP_CHANGED = "step_changed"

    QUIZ_STARTED = "quiz_started"

    QUIZ_FINISHED = "quiz_finished"

    AI_REQUEST = "ai_request"

    LESSON_COMPLETED = "lesson_completed"

    SESSION_RESET = "session_reset"