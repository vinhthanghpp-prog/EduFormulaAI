"""
EduFormula AI

Graph Viewer

Version 1.0
"""

import customtkinter as ctk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from Modules.Visualization import VisualizationRenderer


class GraphViewer(ctk.CTkFrame):

    def __init__(

        self,

        master

    ):

        super().__init__(master)

        self.renderer = VisualizationRenderer()

        self.canvas = None

    def show(

        self,

        visualization_script

    ):

        figure = self.renderer.render(

            visualization_script

        )

        if figure is None:

            return

        if self.canvas:

            self.canvas.get_tk_widget().destroy()

        self.canvas = FigureCanvasTkAgg(

            figure,

            master=self

        )

        self.canvas.draw()

        self.canvas.get_tk_widget().pack(

            fill="both",

            expand=True

        )