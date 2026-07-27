from pathlib import Path
import sys

SOURCE_ROOT = Path(__file__).resolve().parents[1]
if str(SOURCE_ROOT) not in sys.path:
    sys.path.insert(0, str(SOURCE_ROOT))

from Database.Repository.base_repository import BaseRepository

repo = BaseRepository()

print("=" * 50)
print("TEST BASE REPOSITORY")
print("=" * 50)

print("Connection:", repo.conn is not None)

cursor = repo.cursor

print("Cursor:", cursor is not None)

repo.commit()

print("Commit: PASS")

repo.close()

print("Close: PASS")