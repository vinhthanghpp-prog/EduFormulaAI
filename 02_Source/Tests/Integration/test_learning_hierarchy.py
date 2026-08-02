import unittest

from Database.Repository.subject_repository import SubjectRepository
from Database.Repository.grade_repository import GradeRepository
from Database.Repository.chapter_repository import ChapterRepository
from Database.Repository.lesson_repository import LessonRepository
from Database.Repository.knowledge_repository import KnowledgeRepository

from Database.models import (
    Subject,
    Grade,
    Chapter,
    Lesson,
    Knowledge,
)

from Tests.test_base import RepositoryTestCase


class TestLearningHierarchy(RepositoryTestCase):

    def setUp(self):

        super().setUp()

        self.subject_repo = SubjectRepository(self.conn)
        self.grade_repo = GradeRepository(self.conn)
        self.chapter_repo = ChapterRepository(self.conn)
        self.lesson_repo = LessonRepository(self.conn)
        self.knowledge_repo = KnowledgeRepository(self.conn)

    def test_complete_learning_hierarchy(self):

        subject = Subject(
            code="MATH",
            name="Mathematics",
        )

        subject.id = self.subject_repo.create(subject)

        self.assertIsNotNone(
            self.subject_repo.get_by_id(subject.id)
        )

        grade = Grade(
            subject_id=subject.id,
            code="G10",
            name="Grade 10",
        )

        grade.id = self.grade_repo.create(grade)

        self.assertEqual(
            subject.id,
            self.grade_repo.get_by_id(
                grade.id
            ).subject_id,
        )

        chapter = Chapter(
            grade_id=grade.id,
            code="CH01",
            name="Functions",
        )

        chapter.id = self.chapter_repo.create(chapter)

        lesson = Lesson(
            chapter_id=chapter.id,
            code="L01",
            name="Introduction",
        )

        lesson.id = self.lesson_repo.create(lesson)

        knowledge = Knowledge(
            lesson_id=lesson.id,
            code="KN01",
            title="Definition",
            knowledge_type="concept",
        )

        knowledge.id = self.knowledge_repo.create(
            knowledge
        )

        saved = self.knowledge_repo.get_by_id(
            knowledge.id
        )

        self.assertEqual(
            lesson.id,
            saved.lesson_id,
        )

        self.assertEqual(
            "Definition",
            saved.title,
        )