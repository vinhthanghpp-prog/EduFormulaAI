"""
Content Parser
==============

Parser for converting raw learning content into
ContentBlock objects.
"""

from Content.blocks import ContentBlock
from Content.factory import ContentBlockFactory


class ContentParser:

    def __init__(self):
        self.factory = ContentBlockFactory()

    def parse(self, source):
        return [
            self.factory.create("content")
        ]