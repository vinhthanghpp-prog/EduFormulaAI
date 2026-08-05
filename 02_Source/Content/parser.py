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

    def _extract_content(self, source):
        lines = source.strip().splitlines()

        if len(lines) > 1:
            return lines[1].strip()

        return ""

    def parse(self, source):

        block_type = "content"
        content = ""

        if source:
            if "[CONCEPT]" in source:
                block_type = "concept"
                content = self._extract_content(source)

            elif "[FORMULA]" in source:
                block_type = "formula"
                content = self._extract_content(source)

        block = self.factory.create(block_type)
        block.content = content

        return [block]