"""
EduFormula AI
Teaching Script Factory

Version 1.0
"""

from Modules.Teaching import TeachingScript


class TeachingScriptFactory:

    def create(self, step, lesson=None, context=None):

        script = TeachingScript()

        # -------------------------
        # STEP 1
        # -------------------------

        if step["skill"] == "identify_variable":

            if context is not None:

                a = context.get("a", 0)
                b = context.get("b", 0)

            else:

                a = "a"
                b = "b"

            script.explanation = (
                "Muốn biết chiều của đồ thị, trước tiên cần xác định hệ số a."
            )

            script.question = (
                f"Trong biểu thức y = {a}x + {b}, hệ số a bằng bao nhiêu?"
            )

            script.answer = str(a)

            script.feedback = (
                f"🎉 Chính xác! Hệ số a = {a}."
            )

            script.hint = (
                "Hãy nhìn số đứng trước x."
            )

            script.transition = (
                "Chúng ta cùng sang bước tiếp theo."
            )

            return script

        # -------------------------
        # STEP 2
        # -------------------------

        if step["skill"] == "compare_number":

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

        # -------------------------
        # STEP 3
        # -------------------------

        if step["skill"] == "draw_conclusion":

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