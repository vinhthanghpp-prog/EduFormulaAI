from pathlib import Path
import sys

SOURCE_ROOT = Path(__file__).resolve().parents[1]
if str(SOURCE_ROOT) not in sys.path:
    sys.path.insert(0, str(SOURCE_ROOT))

from Database.Repository.subject_repository import SubjectRepository
from Database.Repository.grade_repository import GradeRepository
from Database.Repository.chapter_repository import ChapterRepository

from Database.models import Subject, Grade, Chapter


subject_repo = SubjectRepository()
grade_repo = GradeRepository()
chapter_repo = ChapterRepository()

print("=" * 60)
print("TEST CHAPTER REPOSITORY")
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
# 4. UPDATE
# ======================================================

chapter.name = "Chương 1 (Updated)"

ok = chapter_repo.update(chapter)

print("Update:", ok)

print(chapter_repo.get_by_id(chapter.id))

# ======================================================
# 5. SEARCH
# ======================================================

results = chapter_repo.search("C01", grade.id)

for item in results:
    print(item)

# ======================================================
# 6. DELETE CHAPTER
# ======================================================

ok = chapter_repo.delete(chapter.id)

print("Delete Chapter:", ok)

print(chapter_repo.get_by_id(chapter.id))

# ======================================================
# 7. DELETE GRADE
# ======================================================

ok = grade_repo.delete(grade.id)

print("Delete Grade:", ok)

# ======================================================
# 8. DELETE SUBJECT
# ======================================================

ok = subject_repo.delete(subject.id)

print("Delete Subject:", ok)

print("\n===== ALL TESTS COMPLETED =====")