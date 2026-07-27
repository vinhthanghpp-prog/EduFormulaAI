from pathlib import Path
import sys

SOURCE_ROOT = Path(__file__).resolve().parents[1]
if str(SOURCE_ROOT) not in sys.path:
    sys.path.insert(0, str(SOURCE_ROOT))

from Services.subject_service import SubjectService

service = SubjectService()

print("=" * 60)
print("TEST SUBJECT SERVICE")
print("=" * 60)

existing = service.repository.get_by_code("MATH")

if existing:
    service.delete_subject(existing.id)

# ======================================================
# CREATE
# ======================================================

code = "MATH"

existing = service.repository.get_by_code(code)

if existing:
    service.delete_subject(existing.id)

subject_id = service.create_subject(
    code=code,
    name="Toán",
    description="Môn học kiểm thử",
)

print("Create:", subject_id)

subject = service.get_by_id(subject_id)

print(subject)

# ======================================================
# CHECK AUTO UPPERCASE
# ======================================================

print("Code:", subject.code)

assert subject.code == "MATH"

# ======================================================
# SEARCH
# ======================================================

results = service.search("Toán")

print("Search:", len(results))

for item in results:
    print(item)

# ======================================================
# UPDATE
# ======================================================

subject.name = "Toán học"

ok = service.update_subject(subject)

print("Update:", ok)

print(service.get_by_id(subject.id))

# ======================================================
# DUPLICATE CODE
# ======================================================

try:

    service.create_subject(
        code="MATH",
        name="Duplicate",
    )

except ValueError as ex:

    print("Duplicate PASS")

    print(ex)

# ======================================================
# EMPTY CODE
# ======================================================

try:

    service.create_subject(
        code="",
        name="Sai",
    )

except ValueError as ex:

    print("Empty Code PASS")

    print(ex)

# ======================================================
# EMPTY NAME
# ======================================================

try:

    service.create_subject(
        code="PHY",
        name="",
    )

except ValueError as ex:

    print("Empty Name PASS")

    print(ex)

# ======================================================
# DELETE
# ======================================================

ok = service.delete_subject(subject.id)

print("Delete:", ok)

print(service.get_by_id(subject.id))

print("\n===== ALL TESTS COMPLETED =====")