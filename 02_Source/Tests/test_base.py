"""
test_base.py

Base class for repository tests.
"""

from __future__ import annotations

import sqlite3
import unittest
from datetime import datetime

from Database.schema import DATABASE_SCHEMA

class RepositoryTestCase(unittest.TestCase):
    """Base test case for Repository layer."""

    def setUp(self) -> None:
        """Create an in-memory database and initialize schema."""

        self.conn = sqlite3.connect(":memory:")
        self.conn.row_factory = sqlite3.Row

        cursor = self.conn.cursor()

        for sql in DATABASE_SCHEMA:
            cursor.execute(sql)

        self.conn.commit()

    def tearDown(self) -> None:
        """Close database connection."""

        if getattr(self, "conn", None):
            self.conn.close()

    # ------------------------------------------------------------------
    # Helper methods
    # ------------------------------------------------------------------

    def execute(self, sql: str, params: tuple = ()) -> None:
        """Execute SQL and commit."""

        cur = self.conn.cursor()
        cur.execute(sql, params)
        self.conn.commit()

    def fetch_one(self, sql: str, params: tuple = ()):
        """Fetch one row."""

        cur = self.conn.cursor()
        cur.execute(sql, params)
        return cur.fetchone()

    def fetch_all(self, sql: str, params: tuple = ()):
        """Fetch all rows."""

        cur = self.conn.cursor()
        cur.execute(sql, params)
        return cur.fetchall()

    def now(self) -> str:
        """Return current timestamp."""
        return datetime.now().isoformat()

    def create_subject(
        self,
        code: str = "MATH",
        name: str = "Mathematics",
        description: str = "",
        icon: str = "",
        color: str = "#2196F3",
        status: int = 1,
    ) -> int:

        cursor = self.conn.cursor()

        now = self.now()

        cursor.execute(
            """
            INSERT INTO subjects
            (
                code,
                name,
                description,
                icon,
                color,
                status,
                created_at,
                updated_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                code,
                name,
                description,
                icon,
                color,
                status,
                now,
                now,
            ),
        )

        self.conn.commit()

        return cursor.lastrowid

    def create_grade(
        self,
        subject_id: int,
        code: str = "G10",
        name: str = "Grade 10",
        status: int = 1,
    ) -> int:

        cursor = self.conn.cursor()

        now = self.now()

        cursor.execute(
            """
            INSERT INTO grades
            (
                subject_id,
                code,
                name,
                status,
                created_at,
                updated_at
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                subject_id,
                code,
                name,
                status,
                now,
                now,
            ),
        )

        self.conn.commit()

        return cursor.lastrowid

    def create_chapter(
        self,
        grade_id: int,
        code: str = "CH01",
        name: str = "Functions",
        description: str = "",
        sort_order: int = 1,
        status: int = 1,
    ) -> int:

        cursor = self.conn.cursor()

        now = self.now()

        cursor.execute(
            """
            INSERT INTO chapters
            (
                grade_id,
                code,
                name,
                description,
                sort_order,
                status,
                created_at,
                updated_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                grade_id,
                code,
                name,
                description,
                sort_order,
                status,
                now,
                now,
            ),
        )

        self.conn.commit()

        return cursor.lastrowid

    def create_lesson(
        self,
        chapter_id: int,
        code: str = "L01",
        name: str = "Lesson 1",
        description: str = "",
        learning_time: int = 45,
        sort_order: int = 1,
        status: int = 1,
    ) -> int:

        cursor = self.conn.cursor()

        now = self.now()

        cursor.execute(
            """
            INSERT INTO lessons
            (
                chapter_id,
                code,
                name,
                description,
                learning_time,
                sort_order,
                status,
                created_at,
                updated_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                chapter_id,
                code,
                name,
                description,
                learning_time,
                sort_order,
                status,
                now,
                now,
            ),
        )

        self.conn.commit()

        return cursor.lastrowid


    def create_knowledge(
        self,
        lesson_id: int,
        code: str = "KN01",
        title: str = "Knowledge",
        description: str = "",
        knowledge_type: str = "formula",
        difficulty_level: int = 1,
        sort_order: int = 1,
        status: int = 1,
    ) -> int:
        pass

    def assertChapterExists(self, chapter_id: int):
        chapter = self.repo.get_by_id(chapter_id)
        self.assertIsNotNone(chapter)
        return chapter

    def assertChapterStatus(self, chapter_id: int, status: int):
        chapter = self.repo.get_by_id(chapter_id)
        self.assertIsNotNone(chapter)
        self.assertEqual(chapter.status, status)