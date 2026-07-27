"""
EduFormula AI

Problem Context

Version 1.0
"""


class ProblemContext:

    def __init__(self):

        self.problem_type = ""

        self.variables = {}

        self.raw_problem = ""

    def get(self, name, default=None):

        return self.variables.get(name, default)

    def set(self, name, value):

        self.variables[name] = value

    def to_dict(self):

        return {

            "problem_type": self.problem_type,

            "variables": self.variables,

            "raw_problem": self.raw_problem

        }