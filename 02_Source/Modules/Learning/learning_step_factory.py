"""
EduFormula AI

Subsystem:
Learning

Module:
Learning Step Factory

Version:
1.0
"""

from Modules.Learning import LearningStep
from Modules.Teaching import TeachingScriptFactory
from Modules.Visualization import VisualizationFactory


class LearningStepFactory:

    def __init__(self):

        self.script_factory = TeachingScriptFactory()
        self.visual_factory = VisualizationFactory()

    def create(
        self,
        step,
        lesson,
        context
    ):

        learning_step = LearningStep()

        # Teaching Script
        learning_step.script = self.script_factory.create(
            step,
            lesson,
            context
        )

        # Visualization
        learning_step.visualization = (
            self.visual_factory.create_linear_function(
                context
            )
        )

        return learning_step