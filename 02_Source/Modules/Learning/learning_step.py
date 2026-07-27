"""
EduFormula AI

Subsystem:
Learning

Module:
Learning Step

Version:
1.0

Status:
Development
"""


class LearningStep:
    """
    Đại diện cho một bước học hoàn chỉnh.
    """

    def __init__(self):

        # Nội dung giảng dạy
        self.script = None

        # Minh họa
        self.visualization = None

        # Kết quả đánh giá
        self.evaluation = None

        # Chẩn đoán nhận thức
        self.diagnosis = None

        # Trạng thái
        self.state = "pending"

        # Thống kê
        self.attempts = 0

        self.elapsed_time = 0

        # Dữ liệu mở rộng
        self.metadata = {}

    def to_dict(self):

        return {

            "state": self.state,

            "attempts": self.attempts,

            "elapsed_time": self.elapsed_time,

            "metadata": self.metadata

        }