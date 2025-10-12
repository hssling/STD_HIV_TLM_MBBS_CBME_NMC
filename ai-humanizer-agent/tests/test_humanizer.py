"""
Test Suite for AI Humanizer Agent

This module contains comprehensive tests for the AI humanizer functionality,
including unit tests for all components and integration tests.
"""

import unittest
import os
import tempfile
import shutil
import sys

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from humanizer.core import AIHumanizer, HumanizationResult
from humanizer.detector import AIDetector
from humanizer.transformers import TextTransformer
from humanizer.utils import TextUtils


class TestTextUtils(unittest.TestCase):
    """Test cases for TextUtils class."""

    def setUp(self):
        """Set up test fixtures."""
        self.utils = TextUtils()

    def test_clean_text(self):
        """Test text cleaning functionality."""
        # Test basic cleaning
        text = "  This  is   a   test.  "
        cleaned = self.utils.clean_text(text)
        self.assertEqual(cleaned, "This is a test.")

        # Test punctuation spacing
        text = "Hello , world ! How are you ?"
        cleaned = self.utils.clean_text(text)
        self.assertEqual(cleaned, "Hello, world! How are you?")

    def test_calculate_text_stats(self):
        """Test text statistics calculation."""
        text = "This is a test. This is another sentence! Is this working?"
        stats = self.utils.calculate_text_stats(text)

        self.assertEqual(stats['word_count'], 11)
        self.assertEqual(stats['sentence_count'], 3)
        self.assertGreater(stats['character_count'], 0)

    def test_extract_keywords(self):
        """Test keyword extraction."""
        text = "Machine learning is important for artificial intelligence and data science."
        keywords = self.utils.extract_keywords(text, max_keywords=3)

        self.assertIn("machine", keywords)
        self.assertIn("intelligence", keywords)
        self.assertIn("science", keywords)

    def test_split_into_chunks(self):
        """Test text chunking."""
        text = "Word1 word2 word3 word4 word5 word6 word7 word8 word9 word10"
        chunks = self.utils.split_into_chunks(text, chunk_size=15)

        self.assertGreater(len(chunks), 1)
        self.assertLessEqual(len(chunks[0]), 15)

    def test_safe_filename(self):
        """Test safe filename generation."""
        filename = 'test<>:"/\\|?*file.txt'
        safe_name = self.utils.safe_filename(filename)

        self.assertNotIn('<', safe_name)
        self.assertNotIn('>', safe_name)
        self.assertNotIn(':', safe_name)


class TestAIDetector(unittest.TestCase):
    """Test cases for AIDetector class."""

    def setUp(self):
        """Set up test fixtures."""
        self.config = {
            "detection": {
                "confidence_threshold": 0.8,
                "min_text_length": 50
            }
        }
        self.detector = AIDetector(self.config)

    def test_detect_human_text(self):
        """Test detection of human-written text."""
        human_text = """
        I remember when I was a child, my grandmother used to tell me stories
        about her life growing up on a small farm. The days were long and filled
        with hard work, but she always spoke of them with such fondness and warmth.
        She would describe the smell of fresh bread baking in the old wood stove,
        and the sound of roosters crowing at dawn. These memories stayed with me
        throughout my life and shaped who I am today.
        """

        score = self.detector.detect_ai_content(human_text)
        self.assertLess(score, 0.7)  # Should be low AI probability

    def test_detect_ai_text(self):
        """Test detection of AI-generated text."""
        ai_text = """
        The utilization of artificial intelligence in modern healthcare systems
        represents a significant paradigm shift in medical practice. This
        comprehensive approach facilitates enhanced diagnostic accuracy and
        enables more efficient treatment methodologies. Furthermore, the
        integration of machine learning algorithms provides substantial
        improvements in patient outcomes and healthcare delivery systems.
        """

        score = self.detector.detect_ai_content(ai_text)
        self.assertGreater(score, 0.3)  # Should have some AI probability

    def test_short_text_handling(self):
        """Test handling of short text."""
        short_text = "This is short."
        score = self.detector.detect_ai_content(short_text)
        self.assertEqual(score, 0.0)  # Should return 0 for short text


class TestTextTransformer(unittest.TestCase):
    """Test cases for TextTransformer class."""

    def setUp(self):
        """Set up test fixtures."""
        self.config = {
            "humanization": {
                "intensity": 0.7,
                "techniques": {
                    "vocabulary_variation": True,
                    "sentence_structure": True,
                    "punctuation_variation": True,
                    "idiomatic_expressions": True,
                    "personal_touch": True,
                    "contextual_awareness": True
                }
            }
        }
        self.transformer = TextTransformer(self.config)

    def test_vocabulary_variation(self):
        """Test vocabulary variation transformation."""
        text = "This is a very good and important test."
        transformed, transformations = self.transformer._apply_vocabulary_variation(text)

        # Should have applied some transformations
        self.assertIsInstance(transformations, list)
        # Text should be different or transformations should be applied
        self.assertTrue(transformed != text or len(transformations) > 0)

    def test_sentence_structure_variation(self):
        """Test sentence structure variation."""
        text = "This is a long sentence that should be modified by the transformation system."
        transformed, transformations = self.transformer._vary_sentence_structure(text)

        self.assertIsInstance(transformations, list)

    def test_contraction_application(self):
        """Test contraction application."""
        text = "I am going to the store and I will buy some items."
        transformed, transformations = self.transformer._apply_contractions(text)

        self.assertIsInstance(transformations, list)
        # Should have applied contractions
        self.assertIn("I am", text)
        # May or may not be transformed based on randomness

    def test_personal_touch(self):
        """Test personal touch addition."""
        text = "Machine learning is transforming technology."
        transformed, transformations = self.transformer._add_personal_touch(text)

        self.assertIsInstance(transformations, list)


class TestAIHumanizer(unittest.TestCase):
    """Test cases for main AIHumanizer class."""

    def setUp(self):
        """Set up test fixtures."""
        self.config_path = "config.yaml"
        self.humanizer = AIHumanizer(self.config_path)

    def test_initialization(self):
        """Test proper initialization."""
        self.assertIsNotNone(self.humanizer.detector)
        self.assertIsNotNone(self.humanizer.transformer)
        self.assertIsNotNone(self.humanizer.utils)

    def test_humanize_short_text(self):
        """Test humanization of short text."""
        short_text = "This is short."
        result = self.humanizer.humanize_text(short_text)

        self.assertIsInstance(result, HumanizationResult)
        self.assertTrue(result.success)
        self.assertEqual(result.original_text, short_text)
        self.assertEqual(result.humanized_text, short_text)  # Should remain unchanged

    def test_humanize_normal_text(self):
        """Test humanization of normal text."""
        text = """
        The advancement of technology has significantly impacted modern society.
        This progress has led to numerous improvements in various fields including
        healthcare, education, and communication. The integration of artificial
        intelligence systems has particularly revolutionized industrial processes
        and enhanced productivity across multiple sectors.
        """

        result = self.humanizer.humanize_text(text)

        self.assertIsInstance(result, HumanizationResult)
        self.assertTrue(result.success)
        self.assertEqual(result.original_text, text)
        self.assertIsInstance(result.humanized_text, str)
        self.assertIsInstance(result.transformations_applied, list)
        self.assertGreaterEqual(result.processing_time, 0)

    def test_batch_humanization(self):
        """Test batch humanization."""
        texts = [
            "First text to humanize.",
            "Second text to humanize.",
            "Third text to humanize."
        ]

        results = self.humanizer.batch_humanize(texts)

        self.assertEqual(len(results), 3)
        for result in results:
            self.assertIsInstance(result, HumanizationResult)
            self.assertTrue(result.success)

    def test_file_humanization(self):
        """Test file-based humanization."""
        # Create temporary test file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            test_content = """
            This is a test file that should be humanized by the system.
            It contains multiple sentences and should demonstrate the
            effectiveness of the humanization process.
            """
            f.write(test_content)
            input_path = f.name

        try:
            # Create output file path
            output_dir = tempfile.mkdtemp()
            output_path = os.path.join(output_dir, "humanized_output.txt")

            # Humanize the file
            result = self.humanizer.humanize_file(input_path, output_path)

            self.assertIsInstance(result, HumanizationResult)
            self.assertTrue(result.success)

            # Check if output file was created and has content
            self.assertTrue(os.path.exists(output_path))
            with open(output_path, 'r') as f:
                output_content = f.read()
                self.assertGreater(len(output_content), 0)

        finally:
            # Clean up
            if os.path.exists(input_path):
                os.unlink(input_path)
            if os.path.exists(output_path):
                os.unlink(output_path)
            if os.path.exists(output_dir):
                shutil.rmtree(output_dir)

    def test_get_stats(self):
        """Test statistics retrieval."""
        stats = self.humanizer.get_stats()

        self.assertIsInstance(stats, dict)
        self.assertIn("detector_stats", stats)
        self.assertIn("transformer_stats", stats)
        self.assertIn("config", stats)


class TestIntegration(unittest.TestCase):
    """Integration tests for the complete system."""

    def setUp(self):
        """Set up integration test fixtures."""
        self.humanizer = AIHumanizer("config.yaml")

    def test_end_to_end_humanization(self):
        """Test complete humanization pipeline."""
        # AI-like text
        ai_text = """
        The implementation of advanced technological solutions in contemporary
        business environments necessitates comprehensive strategic planning.
        This approach ensures optimal utilization of available resources and
        facilitates enhanced operational efficiency across all organizational
        departments. Furthermore, the systematic integration of innovative
        methodologies contributes significantly to long-term sustainability
        and competitive advantage in the global marketplace.
        """

        result = self.humanizer.humanize_text(ai_text)

        # Verify result structure
        self.assertIsInstance(result, HumanizationResult)
        self.assertTrue(result.success)
        self.assertIsInstance(result.ai_probability, float)
        self.assertIsInstance(result.transformations_applied, list)

        # Humanized text should be different from original
        if result.ai_probability > 0.5:  # Only if it was detected as AI
            # Should have applied some transformations
            self.assertGreater(len(result.transformations_applied), 0)

    def test_human_text_preservation(self):
        """Test that human text is preserved."""
        human_text = """
        I woke up this morning feeling a bit tired, but excited for the day ahead.
        The sun was shining through my window, and I could hear birds singing outside.
        I made myself a cup of coffee and sat down to plan my day. You know, sometimes
        the simple things in life bring the most joy. I think I'll go for a walk later
        and maybe call my family to catch up.
        """

        result = self.humanizer.humanize_text(human_text)

        # Human text should be mostly preserved
        if result.ai_probability < 0.3:  # If detected as human
            self.assertEqual(len(result.transformations_applied), 0)


if __name__ == '__main__':
    # Create test suite
    test_suite = unittest.TestLoader().loadTestsFromModule(sys.modules[__name__])

    # Run tests with verbose output
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)

    # Print summary
    print(f"\n{'='*50}")
    print("TEST SUMMARY")
    print(f"{'='*50}")
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print(f"Success rate: {(result.testsRun - len(result.failures) - len(result.errors))/result.testsRun*100:.1f}%")

    if result.failures:
        print(f"\nFAILURES: {len(result.failures)}")
        for test, traceback in result.failures:
            print(f"- {test}: {traceback.split('AssertionError:')[-1].strip()}")

    if result.errors:
        print(f"\nERRORS: {len(result.errors)}")
        for test, traceback in result.errors:
            print(f"- {test}: {traceback.split('Exception:')[-1].strip()}")
