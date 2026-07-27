"""
EduFormula AI
Question Factory
Version 1.0
"""
from Modules.Teaching import TeachingScript

class QuestionFactory:

    def create(self, step, lesson):

        if step["skill"] == "identify_variable":

            script = TeachingScript()

            script.explanation = (
                "Muốn biết chiều của đồ thị, trước tiên cần xác định hệ số a."
            )

            script.question = (
                "Trong biểu thức y = ax + b, hệ số a là gì?"
            )

            script.answer = "a"

            script.feedback = (
                "🎉 Chính xác! Em đã xác định đúng hệ số a."
            )

            script.hint = (
                "Hãy nhìn ký hiệu đứng trước x."
            )

            script.transition = (
                "Chúng ta cùng sang bước tiếp theo."
            )

            return script

        if step["skill"] == "compare_number":

            script = TeachingScript()

            script.explanation = (
                "Sau khi xác định được hệ số a, hãy so sánh nó với số 0."
            )

            script.question = (
                "Nếu a = 2 thì a lớn hơn hay nhỏ hơn 0?"
            )

            script.answer = "lớn hơn"

            script.feedback = (
                "🎉 Chính xác! Vì 2 > 0."
            )

            script.hint = (
                "So sánh số 2 với 0."
            )

            script.transition = (
                "Bây giờ chúng ta xác định chiều của đồ thị."
            )

            return script

        if step["skill"] == "draw_conclusion":

            script = TeachingScript()

            script.explanation = (
                "Khi đã biết a > 0, ta có thể kết luận chiều của đồ thị."
            )

            script.question = (
                "Nếu a > 0 thì đồ thị đi lên hay đi xuống?"
            )

            script.answer = "đi lên"

            script.feedback = (
                "🎉 Rất tốt! Đồ thị sẽ đi lên từ trái sang phải."
            )

            script.hint = (
                "Hãy nhớ quy tắc về dấu của hệ số a."
            )

            script.transition = (
                "Em đã hoàn thành bài học."
            )

            return script
        
        return None