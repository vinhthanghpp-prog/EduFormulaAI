"""
init_db.py
Khởi tạo cơ sở dữ liệu EduFormula AI
"""

from datetime import datetime

from Database.connection import get_connection
from Database.schema import DATABASE_SCHEMA


DB_VERSION = "1.0.0"
DB_DESCRIPTION = "Initial Database"


def initialize_database():
    """Tạo toàn bộ cấu trúc CSDL"""

    conn = get_connection()
    cursor = conn.cursor()

    try:
        # Tạo các bảng
        for sql in DATABASE_SCHEMA:
            cursor.execute(sql)

        # Kiểm tra database_info đã có dữ liệu chưa
        cursor.execute("SELECT COUNT(*) FROM database_info")
        count = cursor.fetchone()[0]

        if count == 0:
            now = datetime.now().isoformat(timespec="seconds")

            cursor.execute(
                """
                INSERT INTO database_info
                (
                    version,
                    description,
                    created_at,
                    updated_at
                )
                VALUES (?, ?, ?, ?)
                """,
                (
                    DB_VERSION,
                    DB_DESCRIPTION,
                    now,
                    now,
                ),
            )

        conn.commit()

        print("===================================")
        print("EduFormula AI Database Initialized")
        print(f"Database Version : {DB_VERSION}")
        print("Status           : SUCCESS")
        print("===================================")

    except Exception as ex:
        conn.rollback()

        print("Database initialization failed!")
        print(ex)

        raise

    finally:
        conn.close()


if __name__ == "__main__":
    initialize_database()