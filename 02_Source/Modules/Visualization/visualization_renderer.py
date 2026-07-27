"""
EduFormula AI

Subsystem:
Visualization

Module:
Visualization Renderer

Version:
1.0
"""

import numpy as np
import matplotlib.pyplot as plt


class VisualizationRenderer:

    def render(self, visualization_script):

        if visualization_script.type != "graph":
            return None

        if visualization_script.action != "draw_line":
            return None

        a = visualization_script.parameters["a"]
        b = visualization_script.parameters["b"]

        x = np.linspace(-10, 10, 200)
        y = a * x + b

        fig, ax = plt.subplots(figsize=(5, 5))

        ax.plot(x, y)

        ax.axhline(0)

        ax.axvline(0)

        ax.grid(True)

        ax.set_title(
            visualization_script.caption
        )

        return fig