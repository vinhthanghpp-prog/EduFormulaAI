import customtkinter as ctk

from Modules.Visualization import VisualizationFactory

from UI.Components.Graph import GraphViewer

root = ctk.CTk()

root.geometry("700x600")

factory = VisualizationFactory()

context = {

    "a":2,

    "b":3

}

script = factory.create_linear_function(

    context

)

viewer = GraphViewer(root)

viewer.pack(

    fill="both",

    expand=True,

    padx=20,

    pady=20

)

viewer.show(script)

root.mainloop()