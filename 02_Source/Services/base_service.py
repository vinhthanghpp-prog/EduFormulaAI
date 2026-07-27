class BaseService:
    """
    Base Service
    Chứa các hàm kiểm tra dữ liệu dùng chung cho toàn bộ Service.
    """

    @staticmethod
    def require_text(value: str, field_name: str) -> str:
        if value is None:
            raise ValueError(f"{field_name} không được để trống.")

        value = value.strip()

        if not value:
            raise ValueError(f"{field_name} không được để trống.")

        return value

    @staticmethod
    def require_positive(value, field_name: str):
        if value is None:
            raise ValueError(f"{field_name} không được để trống.")

        if value <= 0:
            raise ValueError(f"{field_name} phải lớn hơn 0.")

        return value

    @staticmethod
    def normalize_code(code: str) -> str:
        """
        Chuẩn hóa mã:
        - bỏ khoảng trắng đầu/cuối
        - chuyển chữ hoa
        """
        code = BaseService.require_text(code, "Mã")

        return code.upper()

    @staticmethod
    def require_entity(entity, message="Không tìm thấy dữ liệu."):
        if entity is None:
            raise ValueError(message)

        return entity

    @staticmethod
    def validate_duplicate(exists: bool, message: str):
        if exists:
            raise ValueError(message)