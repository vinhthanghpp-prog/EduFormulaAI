"""
SubjectRepository
Quản lý dữ liệu bảng subjects
"""

from Database.Repository.base_repository import BaseRepository
from Database.models import Subject
from datetime import datetime


class GradeRepository(BaseRepository):

    def __init__(
        self,
        connection: sqlite3.Connection | None = None,
    ):

        super().__init__(connection)

    def exists_code(self, code: str) -> bool:
        """
        Kiểm tra mã môn học đã tồn tại hay chưa.
        """

        cursor = self.cursor

        cursor.execute(
            """
            SELECT COUNT(*)
            FROM subjects
            WHERE code = ?
            """,
            (code,),
        )

        return cursor.fetchone()[0] > 0

    def add_subject(self, subject: Subject) -> int:
        """
        Thêm một môn học mới.
        Trả về ID của bản ghi vừa tạo.
        """

        if self.exists_code(subject.code):
            raise ValueError(f"Mã môn học '{subject.code}' đã tồn tại.")

        now = datetime.now().isoformat(timespec="seconds")

        cursor = self.cursor

        cursor.execute(
            """
            INSERT INTO subjects
            (
                code,
                name,
                description,
                icon,
                color,
                status,
                created_at,
                updated_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                subject.code,
                subject.name,
                subject.description,
                subject.icon,
                subject.color,
                subject.status,
                now,
                now,
            ),
        )

        self.commit()

        return cursor.lastrowid

    def get_all(self) -> list[Subject]:
        """
        Lấy danh sách tất cả môn học.
        """

        cursor = self.cursor

        cursor.execute(
            """
            SELECT *
            FROM subjects
            ORDER BY code
            """
        )

        rows = cursor.fetchall()

        return [Subject(**dict(row)) for row in rows]

    def get_by_id(self, subject_id: int) -> Subject | None:
        """
        Lấy môn học theo ID.
        """

        cursor = self.cursor

        cursor.execute(
            """
            SELECT *
            FROM subjects
            WHERE id = ?
            """,
            (subject_id,),
        )

        row = cursor.fetchone()

        if row is None:
            return None

        return Subject(**dict(row))

    def get_by_code(self, code: str) -> Subject | None:
        """
        Lấy môn học theo mã.
        """

        cursor = self.cursor

        cursor.execute(
            """
            SELECT *
            FROM subjects
            WHERE code = ?
            """,
            (code,),
        )

        row = cursor.fetchone()

        if row is None:
            return None

        return Subject(**dict(row))

  
    def update(self, subject: Subject) -> bool:
        """
        Cập nhật thông tin môn học.
        Trả về True nếu cập nhật thành công.
        """

        cursor = self.cursor

        cursor.execute(
            """
            SELECT id
            FROM subjects
            WHERE code = ? AND id <> ?
            """,
            (subject.code, subject.id),
        )

        if cursor.fetchone():
            raise ValueError(f"Mã môn học '{subject.code}' đã được sử dụng.")

        now = datetime.now().isoformat(timespec="seconds")

        cursor.execute(
            """
            UPDATE subjects
            SET
                code = ?,
                name = ?,
                description = ?,
                icon = ?,
                color = ?,
                status = ?,
                updated_at = ?
            WHERE id = ?
            """,
            (
                subject.code,
                subject.name,
                subject.description,
                subject.icon,
                subject.color,
                subject.status,
                now,
                subject.id,
            ),
        )

        self.commit()

        return cursor.rowcount > 0

    def delete(self, subject_id: int) -> bool:
        """
        Xóa môn học theo ID.
        """

        cursor = self.cursor

        cursor.execute(
            """
            DELETE FROM subjects
            WHERE id = ?
            """,
            (subject_id,),
        )

        self.commit()

        return cursor.rowcount > 0

    def search(self, keyword: str) -> list[Subject]:
        """
        Tìm kiếm theo mã hoặc tên môn học.
        """

        cursor = self.cursor

        pattern = f"%{keyword}%"

        cursor.execute(
            """
            SELECT *
            FROM subjects
            WHERE code LIKE ?
            OR name LIKE ?
            ORDER BY code
            """,
            (pattern, pattern),
        )

        rows = cursor.fetchall()

        return [Subject(**dict(row)) for row in rows]