import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../parser")

import strategies.by_regex as by_regex


class TestRegexStrategyMethods(unittest.TestCase):

    def test_is_command(self):
        self.assertTrue(by_regex.is_command("    #!/bin/sh"))

    def test_is_list(self):
        self.assertTrue(by_regex.is_list("  * This is a list"))

    def test_is_paragraph(self):
        self.assertTrue(by_regex.is_paragraph("This is a paragraph block/sentence."))

    def test_is_section(self):
        self.assertTrue(by_regex.is_section("Chapter 1: The Whispering Hallow"))

    def test_is_title(self):
        self.assertTrue(by_regex.is_title("          README         "))

    def test_section_is_not_paragraph(self):
        self.assertTrue(not by_regex.is_paragraph("Chapter 1: The Whispering Hallow"))

    def test_section_is_not_command(self):
        self.assertTrue(not by_regex.is_command("Chapter 1: The Whispering Hallow"))


if __name__ == "__main__":
    unittest.main()
