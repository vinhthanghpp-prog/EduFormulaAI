from Content.models import Metadata


class MetadataBuilder:

    def build(self, source):

        metadata = Metadata()

        lines = source.strip().splitlines()

        if len(lines) >= 2:
            if lines[0].strip() == "[SUBJECT]":
                metadata.subject = lines[1].strip()

            if lines[0].strip() == "[GRADE]":
                metadata.grade = lines[1].strip()

            if lines[0].strip() == "[CHAPTER]":
                metadata.chapter = lines[1].strip()

            if lines[0].strip() == "[LESSON]":
                metadata.lesson = lines[1].strip()

        return metadata