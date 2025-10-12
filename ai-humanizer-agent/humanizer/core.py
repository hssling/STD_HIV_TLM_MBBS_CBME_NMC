"""
Core AI Humanizer Engine

This module contains the main AIHumanizer class that orchestrates
AI detection and content humanization processes.
"""

import logging
import yaml
import os
from typing import Dict, List, Optional
from dataclasses import dataclass

from .detector import AIDetector
from .transformers import TextTransformer
from .utils import TextUtils


@dataclass
class HumanizationResult:
    """Result of the humanization process."""
    original_text: str
    humanized_text: str
    ai_probability: float
    transformations_applied: List[str]
    processing_time: float
    success: bool
    error_message: Optional[str] = None


class AIHumanizer:
    """
    Main AI Humanizer class that detects AI-generated content and applies
    humanization techniques to make it undetectable.
    """

    def __init__(self, config_path: str = "config.yaml"):
        """
        Initialize the AI Humanizer.

        Args:
            config_path: Path to configuration file
        """
        self.config = self._load_config(config_path)
        self.detector = AIDetector(self.config)
        self.transformer = TextTransformer(self.config)
        self.utils = TextUtils()

        # Setup logging
        self._setup_logging()

        self.logger = logging.getLogger(__name__)

    def _load_config(self, config_path: str) -> Dict:
        """Load configuration from YAML file."""
        try:
            with open(config_path, 'r', encoding='utf-8') as file:
                return yaml.safe_load(file)
        except Exception as e:
            print(f"Error loading config: {e}")
            # Return default configuration
            return self._get_default_config()

    def _get_default_config(self) -> Dict:
        """Get default configuration if file loading fails."""
        return {
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
            },
            "detection": {
                "confidence_threshold": 0.8,
                "min_text_length": 50
            }
        }

    def _setup_logging(self):
        """Setup logging configuration."""
        log_config = self.config.get("logging", {})
        logging.basicConfig(
            level=getattr(logging, log_config.get("level", "INFO")),
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

    def humanize_text(self, text: str, context: Optional[str] = None) -> HumanizationResult:
        """
        Humanize AI-generated text to make it undetectable.

        Args:
            text: The text to humanize
            context: Optional context for better humanization

        Returns:
            HumanizationResult with the processed text and metadata
        """
        import time
        start_time = time.time()

        try:
            # Check if text is AI-generated
            self.logger.info("Detecting AI content...")
            ai_probability = self.detector.detect_ai_content(text)

            # If not AI-generated or below threshold, return original
            if ai_probability < self.config["detection"]["confidence_threshold"]:
                return HumanizationResult(
                    original_text=text,
                    humanized_text=text,
                    ai_probability=ai_probability,
                    transformations_applied=[],
                    processing_time=time.time() - start_time,
                    success=True
                )

            # Apply humanization transformations
            self.logger.info(f"Humanizing text (AI probability: {ai_probability:.2f})")
            humanized_text, transformations = self.transformer.humanize_text(text, context)

            return HumanizationResult(
                original_text=text,
                humanized_text=humanized_text,
                ai_probability=ai_probability,
                transformations_applied=transformations,
                processing_time=time.time() - start_time,
                success=True
            )

        except Exception as e:
            self.logger.error(f"Error in humanization process: {str(e)}")
            return HumanizationResult(
                original_text=text,
                humanized_text=text,
                ai_probability=0.0,
                transformations_applied=[],
                processing_time=time.time() - start_time,
                success=False,
                error_message=str(e)
            )

    def humanize_file(self, input_path: str, output_path: str, context: Optional[str] = None) -> HumanizationResult:
        """
        Humanize content from a file and save to output path.

        Args:
            input_path: Path to input file
            output_path: Path to save humanized content
            context: Optional context for better humanization

        Returns:
            HumanizationResult with processing metadata
        """
        try:
            # Read input file
            with open(input_path, 'r', encoding='utf-8') as file:
                text = file.read()

            # Humanize the content
            result = self.humanize_text(text, context)

            # Save humanized content
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            with open(output_path, 'w', encoding='utf-8') as file:
                file.write(result.humanized_text)

            return result

        except Exception as e:
            self.logger.error(f"Error processing file: {str(e)}")
            return HumanizationResult(
                original_text="",
                humanized_text="",
                ai_probability=0.0,
                transformations_applied=[],
                processing_time=0.0,
                success=False,
                error_message=str(e)
            )

    def batch_humanize(self, texts: List[str], contexts: Optional[List[str]] = None) -> List[HumanizationResult]:
        """
        Humanize multiple texts in batch.

        Args:
            texts: List of texts to humanize
            contexts: Optional list of contexts

        Returns:
            List of HumanizationResult objects
        """
        results = []

        for i, text in enumerate(texts):
            context = contexts[i] if contexts and i < len(contexts) else None
            result = self.humanize_text(text, context)
            results.append(result)

        return results

    def get_stats(self) -> Dict:
        """Get statistics about the humanizer performance."""
        return {
            "detector_stats": self.detector.get_stats(),
            "transformer_stats": self.transformer.get_stats(),
            "config": self.config
        }
