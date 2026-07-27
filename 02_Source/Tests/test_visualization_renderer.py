from Modules.Visualization import (
    VisualizationFactory,
    VisualizationRenderer
)

factory = VisualizationFactory()

renderer = VisualizationRenderer()

context = {

    "a": 2,

    "b": 3

}

script = factory.create_linear_function(
    context
)

renderer.render(script)