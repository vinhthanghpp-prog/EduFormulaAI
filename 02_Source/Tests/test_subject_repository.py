from pathlib import Path
import sys

SOURCE_ROOT = Path(__file__).resolve().parents[1]
if str(SOURCE_ROOT) not in sys.path:
    sys.path.insert(0, str(SOURCE_ROOT))

from Database.Repository.subject_repository import SubjectRepository
from Database.models import Subject

repo = SubjectRepository()

print("=" * 60)
print("TEST SUBJECT REPOSITORY")
print("=" * 60)

# -------------------------------------------------
# 1. CREATE
# -------------------------------------------------
print("\n[1] CREATE")

if repo.exists_code("TEST"):
    subject = repo.get_by_code("TEST")
else:
    subject = Subject(
        code="TEST",
        name="Môn học kiểm thử",
        description="Repository Test",
        icon="test",
        color="#0000FF",
    )
    subject.id = subject_repo.add_subject(subject)
    subject = repo.get_by_id(new_id)

print(subject)

# -------------------------------------------------
# 2. UPDATE
# -------------------------------------------------
print("\n[2] UPDATE")

subject.name = "Môn học kiểm thử (Updated)"

ok = repo.update(subject)

print("Update:", ok)

print(repo.get_by_id(subject.id))

# -------------------------------------------------
# 3. SEARCH
# -------------------------------------------------
print("\n[3] SEARCH")

results = repo.search("TEST")

for item in results:
    print(item)

# -------------------------------------------------
# 4. DELETE
# -------------------------------------------------
print("\n[4] DELETE")

ok = repo.delete(subject.id)

print("Delete:", ok)

print(repo.get_by_id(subject.id))

print("\n===== ALL TESTS COMPLETED =====")