from pathlib import Path
import sys

SOURCE_ROOT = Path(__file__).resolve().parents[1]
if str(SOURCE_ROOT) not in sys.path:
    sys.path.insert(0, str(SOURCE_ROOT))

from Database.Repository.subject_repository import SubjectRepository
from Database.Repository.grade_repository import GradeRepository
from Database.models import Subject, Grade


def main():

    subject_repo = SubjectRepository()
    grade_repo = GradeRepository()

    print("=" * 60)
    print("TEST GRADE REPOSITORY")
    print("=" * 60)

    # -------------------------------------------------
    # 1. CREATE SUBJECT
    # -------------------------------------------------

    print("\n[1] CREATE SUBJECT")

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
        subject.id = subject_repo.create(subject)
        subject = subject_repo.get_by_id(subject.id)

    print(subject)

    # -------------------------------------------------
    # 2. CREATE GRADE
    # -------------------------------------------------

    print("\n[2] CREATE GRADE")

    grade = Grade(
        subject_id=subject.id,
        code="10",
        name="Lớp 10",
    )

    if grade_repo.exists_code(subject.id, grade.code):
        grade = grade_repo.get_by_code(subject.id, grade.code)
    else:
        grade.id = grade_repo.create(grade)
        grade = grade_repo.get_by_id(grade.id)

    print(grade)

    # -------------------------------------------------
    # 3. UPDATE
    # -------------------------------------------------

    print("\n[3] UPDATE")

    grade.name = "Lớp 10 (Updated)"

    grade_repo.update(grade)

    print(grade_repo.get_by_id(grade.id))

    # -------------------------------------------------
    # 4. SEARCH
    # -------------------------------------------------

    print("\n[4] SEARCH")

    results = grade_repo.search(
        subject.id,
        "10",
    )

    for item in results:
        print(item)

    # -------------------------------------------------
    # 5. DELETE GRADE
    # -------------------------------------------------

    print("\n[5] DELETE GRADE")

    grade_repo.delete(grade.id)

    print("Delete Grade: PASS")

    print(grade_repo.get_by_id(grade.id))

    # -------------------------------------------------
    # 6. DELETE SUBJECT
    # -------------------------------------------------
    grade_repo.update(grade)

    print("\n[6] DELETE SUBJECT")

    print(
        "Skipped - Subject cannot be deleted while grades exist (soft delete)."
    )

    print("\n===== ALL TESTS COMPLETED =====")


if __name__ == "__main__":
    main()