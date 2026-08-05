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

        if source is None:
            source = ""

        result = []

        sections = source.strip().split("\n\n")

        for section in sections:

            block_type = "content"
            content = ""

            if "[CONCEPT]" in section:
                block_type = "concept"
                content = self._extract_content(section)

            elif "[FORMULA]" in section:
                block_type = "formula"
                content = self._extract_content(section)

            block = self.factory.create(block_type)
            block.content = content

            result.append(block)

        return result