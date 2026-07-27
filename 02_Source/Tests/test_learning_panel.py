import customtkinter as ctk

from UI.Components.Learning import LearningPanel

from Modules.Visualization import VisualizationFactory

root = ctk.CTk()

root.geometry("900x700")

panel = LearningPanel(root)

panel.pack(fill="both", expand=True)

factory = VisualizationFactory()

script = factory.create_linear_function(
    {
        "a":2,
        "b":3
    }
)

class DummyStep:

    visualization = script

panel.load_step(DummyStep())

root.mainloop()