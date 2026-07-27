from pprint import pprint

from Modules.Visualization import VisualizationFactory

context = {

    "a":2,

    "b":3

}

factory = VisualizationFactory()

script = factory.create_linear_function(

    context

)

pprint(

    script.to_dict()

)