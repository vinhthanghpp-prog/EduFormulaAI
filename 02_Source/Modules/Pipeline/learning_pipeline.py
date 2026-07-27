"""
EduFormula AI

Subsystem:
Learning Pipeline

Version:
2.0

Status:
Development
"""

from Modules.Engine.problem_parser import ProblemParser
from Modules.Engine.problem_data_extractor import ProblemDataExtractor
from Modules.Engine.knowledge_mapper import KnowledgeMapper
from Modules.Engine.learning_path_planner import LearningPathPlanner
from Modules.Engine.learning_session import LearningSession

from Modules.Teaching import TeachingScriptFactory
from Modules.Learning import LearningStepFactory


class LearningPipeline:

    def __init__(self):

        self.parser = ProblemParser()

        self.extractor = ProblemDataExtractor()

        self.mapper = KnowledgeMapper()

        self.planner = LearningPathPlanner()

        self.step_factory = LearningStepFactory()

    # ==================================================

    def create_session(
        self,
        lesson,
        problem
    ):

        parser_result = self.parser.parse(problem)

        context = self.extractor.extract(problem)

        knowledge = self.mapper.map(
            lesson,
            parser_result
        )

        learning_path = self.planner.create_path(
            knowledge
        )

        session = LearningSession(
            learning_path=learning_path,
            lesson=lesson,
            problem=problem,
            context=context
        )

        return session

    # ==================================================

    def next_step(
        self,
        session
    ):

        step = session.current_step()

        if step is None:
            return None

        learning_step = self.step_factory.create(
            step,
            session.get_lesson(),
            session.get_context()
        )

        session.set_current_script(
            learning_step.script
        )

        return learning_step

    # ==================================================
    # Legacy API
    # ==================================================

    def process(
        self,
        lesson,
        problem
    ):
        """
        Legacy API.
        Chỉ dùng để tương thích với các test cũ.
        """

        session = self.create_session(
            lesson,
            problem
        )

        return self.next_step(session)