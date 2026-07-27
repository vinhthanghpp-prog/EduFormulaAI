from pathlib import Path
import sqlite3

# Đường dẫn thư mục gốc của dự án
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Đường dẫn tới file SQLite
DATABASE_PATH = PROJECT_ROOT / "05_Database" / "database.db"

# Chế độ debug
DEBUG = False


def get_connection() -> sqlite3.Connection:
    """
    Tạo và trả về kết nối tới cơ sở dữ liệu SQLite.
    """

    # Đảm bảo thư mục Database tồn tại
    DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)

    if DEBUG:
        print(f"Database Path: {DATABASE_PATH}")

    conn = sqlite3.connect(DATABASE_PATH)

    # Cho phép truy cập dữ liệu theo tên cột
    conn.row_factory = sqlite3.Row

    # Bật hỗ trợ Foreign Key
    conn.execute("PRAGMA foreign_keys = ON;")

    return conn