import customtkinter as ctk

import customtkinter as ctk

from UI.Components import VariableViewer


variables = [

    {

        "symbol":"a",

        "name":"Hệ số góc"

    },

    {

        "symbol":"b",

        "name":"Tung độ gốc"

    }

]


app = ctk.CTk()

app.geometry("450x300")

viewer = VariableViewer(app)

viewer.pack(
    fill="both",
    expand=True
)

viewer.load_variables(
    variables
)

app.mainloop()