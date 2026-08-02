from Database.Repository.subject_repository import SubjectRepository
from Database.models import Subject

from Services.base_service import BaseService


class SubjectService(BaseService):

    def __init__(self):
        self.repository = SubjectRepository()

    def get_all(self) -> list[Subject]:
        return self.repository.get_all()

    def get_by_id(self, subject_id: int) -> Subject | None:
        self.require_positive(subject_id, "ID môn học")

        return self.repository.get_by_id(subject_id)

    def get_by_code(self, code: str) -> Subject | None:

        code = self.normalize_code(code)

        return self.repository.get_by_code(code)

    def search(self, keyword: str) -> list[Subject]:
        keyword = keyword.strip()

        if not keyword:
            return self.repository.get_all()

        return self.repository.search(keyword)

    def create_subject(
        self,
        code: str,
        name: str,
        description: str = "",
        icon: str = "",
        color: str = "#2196F3",
    ) -> int:

        code = self.normalize_code(code)
        name = self.require_text(name, "Tên môn học")

        self.validate_duplicate(
            self.repository.exists_code(code),
            f"Mã môn học '{code}' đã tồn tại."
        )

        subject = Subject(
            code=code,
            name=name,
            description=description.strip(),
            icon=icon.strip(),
            color=color,
        )

        return self.repository.create(subject)

    def update_subject(self, subject: Subject) -> bool:

        self.require_positive(subject.id, "ID môn học")

        subject.code = self.normalize_code(subject.code)

        subject.name = self.require_text(
            subject.name,
            "Tên môn học",
        )

        current = self.repository.get_by_code(subject.code)

        self.validate_duplicate(
            current is not None and current.id != subject.id,
            f"Mã môn học '{subject.code}' đã tồn tại."
        )

        return self.repository.update(subject)

    def delete_subject(self, subject_id: int) -> bool:

        self.require_positive(subject_id, "ID môn học")

        return self.repository.delete(subject_id)

    def exists_code(self, code: str) -> bool:

        code = self.normalize_code(code)

        return self.repository.exists_code(code)