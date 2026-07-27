"""
EduFormula AI

Visualization Factory

Version 1.0
"""

from Modules.Visualization import VisualizationScript


class VisualizationFactory:

    def create_linear_function(

        self,

        context

    ):

        script = VisualizationScript()

        script.type = "graph"

        script.action = "draw_line"

        script.parameters = {

            "a": context.get("a"),

            "b": context.get("b")

        }

        script.caption = "Đồ thị hàm số"

        script.voice = (

            "Quan sát đồ thị của hàm số."

        )

        return script