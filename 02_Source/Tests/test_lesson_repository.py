from pathlib import Path
import sys

SOURCE_ROOT = Path(__file__).resolve().parents[1]
if str(SOURCE_ROOT) not in sys.path:
    sys.path.insert(0, str(SOURCE_ROOT))

from Database.Repository.subject_repository import SubjectRepository
from Database.Repository.grade_repository import GradeRepository
from Database.Repository.chapter_repository import ChapterRepository
from Database.Repository.lesson_repository import LessonRepository

from Database.models import Subject, Grade, Chapter, Lesson


subject_repo = SubjectRepository()
grade_repo = GradeRepository()
chapter_repo = ChapterRepository()
lesson_repo = LessonRepository()

print("=" * 60)
print("TEST LESSON REPOSITORY")
print("=" * 60)

# ======================================================
# 1. CREATE SUBJECT
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
# 2. CREATE GRADE
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
# 3. CREATE CHAPTER
# ======================================================

chapter = Chapter(
    grade_id=grade.id,
    code="C01",
    name="Chương 1",
    description="Kiểm thử Repository",
    sort_order=1,
)

if chapter_repo.exists_code(grade.id, chapter.code):
    chapter = chapter_repo.get_by_code(grade.id, chapter.code)
else:
    chapter.id = chapter_repo.add_chapter(chapter)
    chapter = chapter_repo.get_by_id(chapter.id)

print(chapter)

# ======================================================
# 4. CREATE LESSON
# ======================================================

lesson = Lesson(
    chapter_id=chapter.id,
    code="L01",
    name="Bài 1",
    description="Kiểm thử Lesson Repository",
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
# 5. UPDATE
# ======================================================

lesson.name = "Bài 1 (Updated)"

ok = lesson_repo.update(lesson)

print("Update Lesson:", ok)

print(lesson_repo.get_by_id(lesson.id))

# ======================================================
# 6. SEARCH
# ======================================================

results = lesson_repo.search("L01", chapter.id)

for item in results:
    print(item)

# ======================================================
# 7. DELETE LESSON
# ======================================================

ok = lesson_repo.delete(lesson.id)

print("Delete Lesson:", ok)

print(lesson_repo.get_by_id(lesson.id))

# ======================================================
# 8. DELETE CHAPTER
# ======================================================

ok = chapter_repo.delete(chapter.id)

print("Delete Chapter:", ok)

# ======================================================
# 9. DELETE GRADE
# ======================================================

ok = grade_repo.delete(grade.id)

print("Delete Grade:", ok)

# ======================================================
# 10. DELETE SUBJECT
# ======================================================

ok = subject_repo.delete(subject.id)

print("Delete Subject:", ok)

print("\n===== ALL TESTS COMPLETED =====")