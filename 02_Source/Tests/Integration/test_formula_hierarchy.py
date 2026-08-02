import unittest

from Database.Repository.subject_repository import SubjectRepository
from Database.Repository.grade_repository import GradeRepository
from Database.Repository.chapter_repository import ChapterRepository
from Database.Repository.lesson_repository import LessonRepository
from Database.Repository.knowledge_repository import KnowledgeRepository
from Database.Repository.formula_repository import FormulaRepository

from Database.models import (
    Subject,
    Grade,
    Chapter,
    Lesson,
    Knowledge,
    Formula,
)

from Tests.test_base import RepositoryTestCase


class TestFormulaHierarchy(RepositoryTestCase):

    def test_complete_formula_hierarchy(self):

        subject_repo = SubjectRepository(self.conn)
        grade_repo = GradeRepository(self.conn)
        chapter_repo = ChapterRepository(self.conn)
        lesson_repo = LessonRepository(self.conn)
        knowledge_repo = KnowledgeRepository(self.conn)
        formula_repo = FormulaRepository(self.conn)

        subject = Subject(
            code="MATH",
            name="Mathematics",
        )
        subject.id = subject_repo.create(subject)

        grade = Grade(
            subject_id=subject.id,
            code="G10",
            name="Grade 10",
        )
        grade.id = grade_repo.create(grade)

        chapter = Chapter(
            grade_id=grade.id,
            code="CH01",
            name="Functions",
        )
        chapter.id = chapter_repo.create(chapter)

        lesson = Lesson(
            chapter_id=chapter.id,
            code="L01",
            name="Introduction",
        )
        lesson.id = lesson_repo.create(lesson)

        knowledge = Knowledge(
            lesson_id=lesson.id,
            code="KN01",
            title="Definition",
            knowledge_type="concept",
        )
        knowledge.id = knowledge_repo.create(knowledge)

        formula = Formula(
            knowledge_id=knowledge.id,
            code="F01",
            name="Newton Second Law",
            expression="F = m * a",
        )
        formula.id = formula_repo.create(formula)

        self.assertIsNotNone(subject_repo.get_by_id(subject.id))
        self.assertIsNotNone(grade_repo.get_by_id(grade.id))
        self.assertIsNotNone(chapter_repo.get_by_id(chapter.id))
        self.assertIsNotNone(lesson_repo.get_by_id(lesson.id))
        self.assertIsNotNone(knowledge_repo.get_by_id(knowledge.id))
        self.assertIsNotNone(formula_repo.get_by_id(formula.id))