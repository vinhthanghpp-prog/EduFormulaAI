import unittest

from Content.parser import ContentParser
from Content.blocks import ContentBlock
from Content.factory import ContentBlockFactory
from unittest.mock import MagicMock


class TestContentParserLogic(unittest.TestCase):

    def test_parse_returns_content_blocks(self):
        parser = ContentParser()

        result = parser.parse(None)

        self.assertIsInstance(
            result,
            list,
        )

    def test_parse_returns_one_content_block(self):
        parser = ContentParser()

        result = parser.parse(None)

        self.assertEqual(
            len(result),
            1,
        )

        self.assertIsInstance(
            result[0],
            ContentBlock,
        )

    def test_parser_uses_factory(self):
        parser = ContentParser()

        self.assertTrue(
            hasattr(parser, "factory")
        )

        self.assertIsInstance(
            parser.factory,
            ContentBlockFactory,
        )

    def test_parse_calls_factory_create(self):
        parser = ContentParser()

        parser.factory.create = MagicMock(return_value=ContentBlock())

        parser.parse(None)

        parser.factory.create.assert_called_once()