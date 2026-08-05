import unittest

from Content.parser import ContentParser


class TestContentParser(unittest.TestCase):

    def test_parser_can_be_created(self):
        parser = ContentParser()

        self.assertIsNotNone(parser)

    def test_parser_has_parse(self):
        parser = ContentParser()

        self.assertTrue(
            hasattr(parser, "parse")
        )

    def test_parse_accepts_source_parameter(self):
        parser = ContentParser()

        self.assertEqual(
            parser.parse.__code__.co_argcount,
            2,
        )

    def test_parse_returns_list(self):
        parser = ContentParser()

        result = parser.parse(None)

        self.assertIsInstance(
            result,
            list,
        )