from dataclasses import dataclass


@dataclass(slots=True)
class Subject:
    id: int | None = None
    code: str = ""
    name: str = ""
    description: str = ""
    icon: str = ""
    color: str = ""
    status: int = 1
    created_at: str = ""
    updated_at: str = ""

@dataclass(slots=True)
class Grade:
    id: int | None = None

    code: str = ""

    name: str = ""

    subject_id: int = 0

    status: int = 1

    created_at: str = ""

    updated_at: str = ""

@dataclass(slots=True)
class Chapter:
    id: int | None = None

    grade_id: int = 0

    code: str = ""

    name: str = ""

    description: str = ""

    sort_order: int = 0

    status: int = 1

    created_at: str = ""

    updated_at: str = ""

@dataclass(slots=True)
class Lesson:
    id: int | None = None

    chapter_id: int = 0

    code: str = ""

    name: str = ""

    description: str = ""

    learning_time: int = 45

    sort_order: int = 0

    status: int = 1

    created_at: str = ""

    updated_at: str = ""

@dataclass(slots=True)
class Knowledge:
    id: int | None = None

    lesson_id: int = 0

    code: str = ""

    title: str = ""

    description: str = ""

    knowledge_type: str = ""

    difficulty_level: int = 1

    sort_order: int = 0

    status: int = 1

    created_at: str = ""

    updated_at: str = ""