import unittest

from Content.metadata_builder import MetadataBuilder


class TestMetadataBuilder(unittest.TestCase):

    def test_builder_can_be_created(self):

        builder = MetadataBuilder()

        self.assertIsNotNone(builder)

    def test_builder_has_build(self):

        builder = MetadataBuilder()

        self.assertTrue(
            hasattr(builder, "build")
        )

    def test_build_accepts_source_parameter(self):

        builder = MetadataBuilder()

        result = builder.build("")

        self.assertIsNotNone(result)

    def test_builder_reads_subject(self):

        builder = MetadataBuilder()

        source = """
    [SUBJECT]
    Toán
    """

        metadata = builder.build(source)

        self.assertEqual(
            metadata.subject,
            "Toán",
        )

    def test_builder_reads_grade(self):

        builder = MetadataBuilder()

        source = """
    [GRADE]
    10
    """

        metadata = builder.build(source)

        self.assertEqual(
            metadata.grade,
            "10",
        )

    def test_builder_reads_chapter(self):

        builder = MetadataBuilder()

        source = """
    [CHAPTER]
    Vector
    """

        metadata = builder.build(source)

        self.assertEqual(
            metadata.chapter,
            "Vector",
        )

    def test_builder_reads_lesson(self):

        builder = MetadataBuilder()

        source = """
    [LESSON]
    Khái niệm Vector
    """

        metadata = builder.build(source)

        self.assertEqual(
            metadata.lesson,
            "Khái niệm Vector",
        )