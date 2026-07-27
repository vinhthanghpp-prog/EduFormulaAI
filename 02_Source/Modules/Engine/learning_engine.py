"""
EduFormula AI
Learning Engine
Version 1.0
"""

from Modules.Engine.problem_parser import ProblemParser
from Modules.Engine.problem_analyzer import ProblemAnalyzer
from Modules.Engine.knowledge_mapper import KnowledgeMapper
from Modules.Engine.learning_path_planner import LearningPathPlanner
from Modules.Engine.learning_session import LearningSession


class LearningEngine:
    """
    Điều phối toàn bộ Learning Pipeline.
    """

    def __init__(self):

        self.parser = ProblemParser()

        self.analyzer = ProblemAnalyzer()

        self.mapper = KnowledgeMapper()

        self.planner = LearningPathPlanner()

    # -----------------------------------------------------

    def start(self, lesson, problem):

        # 1. Parser
        parser_result = self.parser.parse(problem)

        # 2. Analyzer
        analysis = self.analyzer.analyze(
            lesson,
            problem
        )

        # 3. Mapper
        knowledge = self.mapper.map(
            lesson,
            parser_result
        )

        # 4. Planner
        learning_path = self.planner.create_path(
            knowledge
        )

        # 5. Session
        session = LearningSession(
            learning_path
        )

        return session