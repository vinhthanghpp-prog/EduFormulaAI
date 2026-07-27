"""
schema.py
Định nghĩa toàn bộ cấu trúc cơ sở dữ liệu SQLite
EduFormula AI
"""

# ==========================================================
# DATABASE VERSION
# ==========================================================

CREATE_DATABASE_INFO = """
CREATE TABLE IF NOT EXISTS database_info
(
    id              INTEGER PRIMARY KEY AUTOINCREMENT,

    version         TEXT NOT NULL,

    description     TEXT,

    created_at      TEXT NOT NULL,

    updated_at      TEXT NOT NULL
);
"""

# ==========================================================
# SUBJECTS
# ==========================================================

CREATE_SUBJECTS = """
CREATE TABLE IF NOT EXISTS subjects
(
    id              INTEGER PRIMARY KEY AUTOINCREMENT,

    code            TEXT NOT NULL UNIQUE,

    name            TEXT NOT NULL,

    description     TEXT,

    icon            TEXT,

    color           TEXT,

    status          INTEGER NOT NULL DEFAULT 1,

    created_at      TEXT NOT NULL,

    updated_at      TEXT NOT NULL
);
"""

# ==========================================================
# GRADES
# ==========================================================

CREATE_GRADES = """
CREATE TABLE IF NOT EXISTS grades
(
    id              INTEGER PRIMARY KEY AUTOINCREMENT,

    subject_id      INTEGER NOT NULL,

    code            TEXT NOT NULL,

    name            TEXT NOT NULL,

    status          INTEGER NOT NULL DEFAULT 1,

    created_at      TEXT NOT NULL,

    updated_at      TEXT NOT NULL,

    FOREIGN KEY(subject_id)
        REFERENCES subjects(id)
);
"""

CREATE_CHAPTERS = """
CREATE TABLE IF NOT EXISTS chapters
(
    id              INTEGER PRIMARY KEY AUTOINCREMENT,

    grade_id        INTEGER NOT NULL,

    code            TEXT NOT NULL,

    name            TEXT NOT NULL,

    description     TEXT,

    sort_order      INTEGER DEFAULT 0,

    status          INTEGER NOT NULL DEFAULT 1,

    created_at      TEXT NOT NULL,

    updated_at      TEXT NOT NULL,

    FOREIGN KEY(grade_id)
        REFERENCES grades(id)
);
"""
CREATE_LESSONS = """
CREATE TABLE IF NOT EXISTS lessons
(
    id              INTEGER PRIMARY KEY AUTOINCREMENT,

    chapter_id      INTEGER NOT NULL,

    code            TEXT NOT NULL,

    name            TEXT NOT NULL,

    description     TEXT,

    learning_time   INTEGER DEFAULT 45,

    sort_order      INTEGER DEFAULT 0,

    status          INTEGER NOT NULL DEFAULT 1,

    created_at      TEXT NOT NULL,

    updated_at      TEXT NOT NULL,

    FOREIGN KEY(chapter_id)
        REFERENCES chapters(id)
);
"""

CREATE_KNOWLEDGE = """
CREATE TABLE IF NOT EXISTS knowledge
(
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,

    lesson_id           INTEGER NOT NULL,

    code                TEXT NOT NULL UNIQUE,

    title               TEXT NOT NULL,

    description         TEXT,

    knowledge_type      TEXT NOT NULL,

    difficulty_level    INTEGER DEFAULT 1,

    sort_order          INTEGER DEFAULT 0,

    status              INTEGER NOT NULL DEFAULT 1,

    created_at          TEXT NOT NULL,

    updated_at          TEXT NOT NULL,

    FOREIGN KEY(lesson_id)
        REFERENCES lessons(id)
);
"""

# ==========================================================
# DATABASE SCHEMA
# ==========================================================

DATABASE_SCHEMA = [
    CREATE_DATABASE_INFO,
    CREATE_SUBJECTS,
    CREATE_GRADES,
    CREATE_CHAPTERS,
    CREATE_LESSONS,
    CREATE_KNOWLEDGE,
]
