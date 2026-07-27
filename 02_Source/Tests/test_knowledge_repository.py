from pathlib import Path
import sys

SOURCE_ROOT = Path(__file__).resolve().parents[1]
if str(SOURCE_ROOT) not in sys.path:
    sys.path.insert(0, str(SOURCE_ROOT))

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

subject_repo = SubjectRepository()
grade_repo = GradeRepository()
chapter_repo = ChapterRepository()
lesson_repo = LessonRepository()
knowledge_repo = KnowledgeRepository()

print("=" * 60)
print("TEST KNOWLEDGE REPOSITORY")
print("=" * 60)

# ======================================================
# CREATE SUBJECT
# ======================================================

subject = Subject(
    code="TEST_SUBJECT",
    name="Subject Test",
    description="Repository Test",
    icon="test",
    color="#2196F3",
)

if subject_repo.exists_code(subject.code):
    subject = subject_repo.get_by_code(subject.code)
else:
    subject.id = subject_repo.add_subject(subject)
    subject = subject_repo.get_by_id(subject.id)

print(subject)

# ======================================================
# CREATE GRADE
# ======================================================

grade = Grade(
    subject_id=subject.id,
    code="10",
    name="Lớp 10",
)

if grade_repo.exists_code(subject.id, grade.code):
    grade = grade_repo.get_by_code(subject.id, grade.code)
else:
    grade.id = grade_repo.add_grade(grade)
    grade = grade_repo.get_by_id(grade.id)

print(grade)

# ======================================================
# CREATE CHAPTER
# ======================================================

chapter = Chapter(
    grade_id=grade.id,
    code="C01",
    name="Chương 1",
    description="Repository Test",
    sort_order=1,
)

if chapter_repo.exists_code(grade.id, chapter.code):
    chapter = chapter_repo.get_by_code(grade.id, chapter.code)
else:
    chapter.id = chapter_repo.add_chapter(chapter)
    chapter = chapter_repo.get_by_id(chapter.id)

print(chapter)

# ======================================================
# CREATE LESSON
# ======================================================

lesson = Lesson(
    chapter_id=chapter.id,
    code="L01",
    name="Bài 1",
    description="Repository Test",
    learning_time=45,
    sort_order=1,
)

if lesson_repo.exists_code(chapter.id, lesson.code):
    lesson = lesson_repo.get_by_code(chapter.id, lesson.code)
else:
    lesson.id = lesson_repo.add_lesson(lesson)
    lesson = lesson_repo.get_by_id(lesson.id)

print(lesson)

# ======================================================
# CREATE KNOWLEDGE
# ======================================================

knowledge = Knowledge(
    lesson_id=lesson.id,
    code="K001",
    title="Khái niệm",
    description="Kiểm thử Knowledge Repository",
    knowledge_type="concept",
    difficulty_level=1,
    sort_order=1,
)

if knowledge_repo.exists_code(lesson.id, knowledge.code):
    knowledge = knowledge_repo.get_by_code(lesson.id, knowledge.code)
else:
    knowledge.id = knowledge_repo.add_knowledge(knowledge)
    knowledge = knowledge_repo.get_by_id(knowledge.id)

print(knowledge)

# ======================================================
# UPDATE
# ======================================================

knowledge.title = "Khái niệm (Updated)"

ok = knowledge_repo.update(knowledge)

print("Update Knowledge:", ok)
print(knowledge_repo.get_by_id(knowledge.id))

# ======================================================
# SEARCH
# ======================================================

results = knowledge_repo.search("K001", lesson.id)

for item in results:
    print(item)

# ======================================================
# DELETE KNOWLEDGE
# ======================================================

ok = knowledge_repo.delete(knowledge.id)
print("Delete Knowledge:", ok)
print(knowledge_repo.get_by_id(knowledge.id))

# ======================================================
# DELETE LESSON
# ======================================================

print("Delete Lesson:", lesson_repo.delete(lesson.id))

# ======================================================
# DELETE CHAPTER
# ======================================================

print("Delete Chapter:", chapter_repo.delete(chapter.id))

# ======================================================
# DELETE GRADE
# ======================================================

print("Delete Grade:", grade_repo.delete(grade.id))

# ======================================================
# DELETE SUBJECT
# ======================================================

print("Delete Subject:", subject_repo.delete(subject.id))

print("\n===== ALL TESTS COMPLETED =====")