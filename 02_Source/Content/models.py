from dataclasses import dataclass, field
from Content.blocks import ContentBlock


@dataclass
class Metadata:
    subject: str = ""
    grade: str = ""
    chapter: str = ""
    lesson: str = ""


@dataclass
class LearningUnit:
    title: str = ""
    explanation: str = ""
    content_blocks: list["ContentBlock"] = field(default_factory=list)


@dataclass
class LearningContent:
    metadata: Metadata = field(default_factory=Metadata)
    learning_units: list["LearningUnit"] = field(default_factory=list)