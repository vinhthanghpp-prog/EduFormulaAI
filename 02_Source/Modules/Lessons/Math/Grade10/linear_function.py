"""
EduFormula AI
Lesson Template v1.1
"""

LESSON = {

    # ==========================================================
    # Metadata
    # ==========================================================
    "metadata": {
        "id": "MATH10_CH01_L01",
        "subject": "Toán",
        "grade": 10,
        "chapter": 1,
        "lesson": 1,
        "title": "Hàm số bậc nhất",
        "version": "1.1"
    },

    # ==========================================================
    # Mục tiêu
    # ==========================================================
    "objectives": [
        "Hiểu khái niệm hàm số bậc nhất.",
        "Hiểu ý nghĩa của hệ số a và hệ số b.",
        "Biết nhận dạng đồ thị hàm số bậc nhất."
    ],

    # ==========================================================
    # Gợi mở bài học
    # ==========================================================
    "motivation": {

        "intro":
            """Trong thực tế, rất nhiều hiện tượng thay đổi theo tốc độ không đổi.

Ví dụ:

• Tiền tiết kiệm tăng đều mỗi tháng.
• Quãng đường xe đi được khi chạy đều.
• Mực nước tăng đều.

Những hiện tượng này đều có thể mô tả bằng hàm số bậc nhất.""",

        "question":
            "Vì sao tiền taxi tăng gần như theo một đường thẳng khi quãng đường tăng?"

    },

    # ==========================================================
    # Khái niệm
    # ==========================================================
    "concept": {

        "title": "Khái niệm",

        "content":
            "Hàm số bậc nhất là hàm số có dạng y = ax + b (a ≠ 0). "
            "Đồ thị của hàm số là một đường thẳng."

    },

    # ==========================================================
    # Công thức
    # ==========================================================
    "formula": {

        "expression": "y = ax + b",

        "latex": "y=ax+b",

        "description":
            "Công thức tổng quát của hàm số bậc nhất.",

        "meaning": {

            "a": "Quyết định độ dốc của đường thẳng.",

            "b": "Quyết định vị trí cắt trục Oy."

        }

    },

    # ==========================================================
    # Các biến
    # ==========================================================
    "variables": [

        {

            "symbol": "a",

            "name": "Hệ số góc",

            "meaning":
                "Cho biết độ dốc của đường thẳng.",

            "effect":
                "Nếu a > 0 thì đồ thị đi lên từ trái sang phải.\n"
                "Nếu a < 0 thì đồ thị đi xuống.\n"
                "|a| càng lớn thì đường thẳng càng dốc.",

            "unit": "",

            "color": "#E74C3C",

            "tips": [
                "Nhìn dấu của a để biết đồ thị đi lên hay đi xuống."
            ],

            "common_mistakes": [
                "Nhầm hệ số a với hệ số b."
            ]

        },

        {

            "symbol": "b",

            "name": "Tung độ gốc",

            "meaning":
                "Là tung độ của điểm mà đồ thị cắt trục Oy.",

            "effect":
                "Khi b thay đổi, đường thẳng dịch chuyển lên hoặc xuống "
                "mà không làm thay đổi độ dốc.",

            "unit": "",

            "color": "#3498DB",

            "tips": [
                "Muốn tìm b hãy cho x = 0."
            ],

            "common_mistakes": [
                "Cho rằng b làm thay đổi độ dốc của đường thẳng."
            ]

        }

    ],

    # ==========================================================
    # Minh họa
    # ==========================================================
    "visualization": {

        "graph": None,

        "animation": None,

        "interactive": False

    },

    # ==========================================================
    # Ví dụ
    # ==========================================================
    "example": {

        "title": "Ví dụ",

        "content":
            "Cho hàm số y = 2x + 3. "
            "Hệ số a = 2 nên đồ thị đi lên từ trái sang phải. "
            "Hệ số b = 3 nên đồ thị cắt trục Oy tại điểm (0;3)."

    },

    # ==========================================================
    # Hướng dẫn giải từng bước (NEW)
    # ==========================================================
    "worked_examples": [

        {

            "title": "Ví dụ 1",

            "problem":
                "Cho hàm số y = 2x + 3. Hãy xác định đồ thị đi lên hay đi xuống.",

            "steps": [

                {

                    "step": 1,

                    "title": "Xác định hệ số a",

                    "explanation":
                        "Trong công thức y = ax + b, hệ số a quyết định chiều của đồ thị.",

                    "result":
                        "a = 2"

                },

                {

                    "step": 2,

                    "title": "So sánh với 0",

                    "explanation":
                        "Ta có 2 > 0.",

                    "result":
                        "a > 0"

                },

                {

                    "step": 3,

                    "title": "Kết luận",

                    "explanation":
                        "Vì a > 0 nên đồ thị đi lên từ trái sang phải.",

                    "result":
                        "Đồ thị đi lên."

                }

            ]

        }

    ],

    # ==========================================================
    # Tổng kết
    # ==========================================================
    "summary": [

        "Hàm số bậc nhất có dạng y = ax + b (a ≠ 0).",

        "Đồ thị là một đường thẳng.",

        "a quyết định độ dốc.",

        "b quyết định giao điểm với trục Oy."

    ],

    # ==========================================================
    # Mẹo
    # ==========================================================
    "tips": [

        "Muốn biết đồ thị đi lên hay đi xuống, hãy nhìn dấu của a.",

        "Muốn biết đồ thị cắt trục Oy ở đâu, hãy nhìn giá trị b.",

        "Hai đường thẳng có cùng hệ số a sẽ song song với nhau."

    ],

    # ==========================================================
    # Sai lầm thường gặp
    # ==========================================================
    "common_mistakes": [

        "Cho rằng a = 0 vẫn là hàm số bậc nhất.",

        "Nhầm vai trò của hệ số a và hệ số b.",

        "Kết luận sai chiều của đồ thị khi a âm.",

        "Quên điều kiện a ≠ 0."

    ],

    # ==========================================================
    # Câu hỏi kiểm tra
    # ==========================================================
    "quiz": [

        {

            "question":
                "Trong hàm số y = ax + b, hệ số nào quyết định độ dốc của đường thẳng?",

            "options": [

                "A. b",

                "B. a",

                "C. x",

                "D. y"

            ],

            "answer": "B"

        }

    ]

}


def get_lesson():
    return LESSON