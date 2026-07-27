"""
EduFormula AI

Subsystem:
Visualization

Module:
Visualization Script

Version:
1.0

Status:
Development
"""


class VisualizationScript:

    def __init__(self):

        self.type = ""

        self.action = ""

        self.parameters = {}

        self.caption = ""

        self.voice = ""

    def to_dict(self):

        return {

            "type": self.type,

            "action": self.action,

            "parameters": self.parameters,

            "caption": self.caption,

            "voice": self.voice

        }