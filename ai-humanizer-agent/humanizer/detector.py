"""
AI Content Detection Module

This module contains various methods to detect AI-generated content
using multiple detection strategies and models.
"""

import re
import logging
from typing import Dict
from collections import Counter
import math

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
import numpy as np

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt', quiet=True)

try:
    nltk.data.find('tokenizers/punkt_tab')
except LookupError:
    nltk.download('punkt_tab', quiet=True)


class AIDetector:
    """
    AI Content Detector using multiple detection strategies.

    This class implements various methods to detect AI-generated content:
    1. Linguistic pattern analysis
    2. Statistical analysis
    3. Repetition detection
    4. Vocabulary analysis
    """

    def __init__(self, config: Dict):
        """
        Initialize the AI Detector.

        Args:
            config: Configuration dictionary
        """
        self.config = config
        self.stats = {
            "total_detections": 0,
            "ai_detected": 0,
            "human_detected": 0
        }

        # AI-generated content indicators
        self.ai_indicators = {
            "repetition_score": 0,
            "vocabulary_richness": 0,
            "sentence_complexity": 0,
            "pattern_consistency": 0,
            "determiner_usage": 0,
            "adverb_frequency": 0
        }

        self.logger = logging.getLogger(__name__)

    def detect_ai_content(self, text: str) -> float:
        """
        Detect if text is AI-generated using multiple strategies.

        Args:
            text: Text to analyze

        Returns:
            Probability score (0.0 = human, 1.0 = AI-generated)
        """
        if not text or len(text.strip()) < self.config["detection"]["min_text_length"]:
            return 0.0

        self.stats["total_detections"] += 1

        try:
            # Multiple detection strategies
            scores = []

            # 1. Linguistic pattern analysis
            pattern_score = self._analyze_linguistic_patterns(text)
            scores.append(pattern_score)

            # 2. Statistical analysis
            statistical_score = self._analyze_statistical_features(text)
            scores.append(statistical_score)

            # 3. Repetition analysis
            repetition_score = self._analyze_repetition(text)
            scores.append(repetition_score)

            # 4. Vocabulary analysis
            vocab_score = self._analyze_vocabulary(text)
            scores.append(vocab_score)

            # 5. Sentence structure analysis
            structure_score = self._analyze_sentence_structure(text)
            scores.append(structure_score)

            # 6. Punctuation analysis
            punctuation_score = self._analyze_punctuation_patterns(text)
            scores.append(punctuation_score)

            # Combine scores with weights
            weights = [0.2, 0.25, 0.15, 0.15, 0.15, 0.1]
            final_score = sum(score * weight for score, weight in zip(scores, weights))

            # Update statistics
            if final_score > self.config["detection"]["confidence_threshold"]:
                self.stats["ai_detected"] += 1
            else:
                self.stats["human_detected"] += 1

            return min(final_score, 1.0)  # Cap at 1.0

        except Exception as e:
            self.logger.error(f"Error in AI detection: {str(e)}")
            return 0.5  # Return neutral score on error

    def _analyze_linguistic_patterns(self, text: str) -> float:
        """Analyze linguistic patterns typical of AI-generated content."""
        sentences = sent_tokenize(text)
        words = word_tokenize(text.lower())

        if len(sentences) < 3 or len(words) < 20:
            return 0.5

        # 1. Check for excessive use of certain determiners
        determiners = ["the", "a", "an", "this", "that", "these", "those"]
        determiner_count = sum(1 for word in words if word in determiners)
        determiner_ratio = determiner_count / len(words)

        # AI often uses more determiners
        ai_determiner_score = min(determiner_ratio * 3, 1.0)

        # 2. Check for adverb patterns
        adverbs = [word for word in words if word.endswith('ly')]
        adverb_ratio = len(adverbs) / len(words)

        # AI often uses more adverbs
        ai_adverb_score = min(adverb_ratio * 4, 1.0)

        # 3. Check for sentence length consistency
        sentence_lengths = [len(word_tokenize(sent)) for sent in sentences]
        if sentence_lengths:
            std_dev = np.std(sentence_lengths)
            mean_length = np.mean(sentence_lengths)
            consistency_score = min(std_dev / mean_length, 1.0) if mean_length > 0 else 0.5

            # AI tends to have more consistent sentence lengths
            ai_consistency_score = 1.0 - consistency_score

        # 4. Check for common AI phrases
        ai_phrases = [
            "in conclusion", "furthermore", "moreover", "however",
            "it is important to note", "it should be noted that",
            "one of the key", "it is worth mentioning"
        ]

        phrase_score = 0
        for phrase in ai_phrases:
            if phrase in text.lower():
                phrase_score += 0.1

        phrase_score = min(phrase_score, 1.0)

        # Combine linguistic indicators
        linguistic_score = (ai_determiner_score * 0.3 +
                          ai_adverb_score * 0.25 +
                          ai_consistency_score * 0.25 +
                          phrase_score * 0.2)

        return linguistic_score

    def _analyze_statistical_features(self, text: str) -> float:
        """Analyze statistical features of the text."""
        words = word_tokenize(text.lower())

        if len(words) < 20:
            return 0.5

        # 1. Word frequency analysis
        word_freq = Counter(words)
        most_common = word_freq.most_common(10)

        # Calculate entropy (higher entropy = more diverse vocabulary)
        total_words = len(words)
        entropy = -sum((count / total_words) * math.log2(count / total_words)
                      for count in word_freq.values() if count > 0)

        # Normalize entropy (typical range is 4-12 bits)
        normalized_entropy = entropy / 12.0

        # AI often has lower entropy (more repetitive)
        ai_entropy_score = 1.0 - normalized_entropy

        # 2. Unique word ratio
        unique_words = len(word_freq)
        unique_ratio = unique_words / total_words

        # AI often has lower unique word ratios
        ai_unique_score = 1.0 - min(unique_ratio * 3, 1.0)

        # 3. Very common word analysis
        very_common_words = [word for word, count in most_common if count > total_words * 0.05]
        common_ratio = len(very_common_words) / len(most_common)

        # AI tends to have more very common words
        ai_common_score = min(common_ratio * 2, 1.0)

        # Combine statistical indicators
        statistical_score = (ai_entropy_score * 0.4 +
                           ai_unique_score * 0.35 +
                           ai_common_score * 0.25)

        return statistical_score

    def _analyze_repetition(self, text: str) -> float:
        """Analyze repetition patterns in the text."""
        words = word_tokenize(text.lower())

        if len(words) < 10:
            return 0.5

        # 1. Word repetition analysis
        word_freq = Counter(words)
        repeated_words = [word for word, count in word_freq.items() if count > 1]
        repetition_ratio = len(repeated_words) / len(word_freq)

        # AI often has more repetitive vocabulary
        ai_repetition_score = min(repetition_ratio * 2, 1.0)

        # 2. Phrase repetition (2-grams)
        two_grams = [f"{words[i]} {words[i+1]}" for i in range(len(words)-1)]
        two_gram_freq = Counter(two_grams)
        repeated_phrases = [phrase for phrase, count in two_gram_freq.items() if count > 1]
        phrase_repetition_ratio = len(repeated_phrases) / len(two_gram_freq)

        # AI often repeats phrases
        ai_phrase_score = min(phrase_repetition_ratio * 3, 1.0)

        # 3. Exact sentence repetition
        sentences = sent_tokenize(text)
        sentence_freq = Counter(sentences)
        repeated_sentences = [sent for sent, count in sentence_freq.items() if count > 1]
        sentence_repetition_ratio = len(repeated_sentences) / len(sentences)

        # AI sometimes repeats entire sentences
        ai_sentence_score = min(sentence_repetition_ratio * 5, 1.0)

        # Combine repetition indicators
        repetition_score = (ai_repetition_score * 0.4 +
                          ai_phrase_score * 0.35 +
                          ai_sentence_score * 0.25)

        return repetition_score

    def _analyze_vocabulary(self, text: str) -> float:
        """Analyze vocabulary characteristics."""
        words = word_tokenize(text.lower())

        if len(words) < 20:
            return 0.5

        # 1. Average word length
        avg_word_length = sum(len(word) for word in words) / len(words)

        # AI often uses longer, more complex words
        ai_length_score = min((avg_word_length - 4.5) / 2, 1.0) if avg_word_length > 4.5 else 0.0

        # 2. Complex word ratio (words with 3+ syllables)
        complex_words = 0
        for word in words:
            syllables = self._count_syllables(word)
            if syllables >= 3:
                complex_words += 1

        complex_ratio = complex_words / len(words)

        # AI often uses more complex vocabulary
        ai_complex_score = min(complex_ratio * 3, 1.0)

        # 3. Academic/formal word analysis
        formal_words = [
            "utilize", "facilitate", "implement", "demonstrate", "establish",
            "significant", "substantial", "comprehensive", "methodology",
            "paradigm", "framework", "analysis", "evaluation", "assessment"
        ]

        formal_count = sum(1 for word in words if word in formal_words)
        formal_ratio = formal_count / len(words)

        # AI often uses more formal/academic language
        ai_formal_score = min(formal_ratio * 5, 1.0)

        # Combine vocabulary indicators
        vocab_score = (ai_length_score * 0.3 +
                      ai_complex_score * 0.4 +
                      ai_formal_score * 0.3)

        return vocab_score

    def _analyze_sentence_structure(self, text: str) -> float:
        """Analyze sentence structure patterns."""
        sentences = sent_tokenize(text)

        if len(sentences) < 3:
            return 0.5

        # 1. Sentence length analysis
        word_counts = [len(word_tokenize(sent)) for sent in sentences]
        avg_length = sum(word_counts) / len(word_counts)

        # AI tends to have more uniform sentence lengths
        std_dev = np.std(word_counts)
        uniformity_score = 1.0 - min(std_dev / avg_length, 1.0) if avg_length > 0 else 0.5

        # 2. Sentence type analysis (declarative vs interrogative)
        declarative_count = sum(1 for sent in sentences if sent.strip().endswith('.'))
        interrogative_count = sum(1 for sent in sentences if sent.strip().endswith('?'))

        declarative_ratio = declarative_count / len(sentences)
        interrogative_ratio = interrogative_count / len(sentences)

        # AI tends to use more declarative sentences
        ai_declarative_score = min(declarative_ratio * 1.2, 1.0)

        # 3. Complex sentence ratio
        complex_sentences = sum(1 for sent in sentences if ',' in sent or ';' in sent)
        complex_ratio = complex_sentences / len(sentences)

        # AI often uses more complex sentence structures
        ai_complex_score = min(complex_ratio * 1.5, 1.0)

        # Combine structure indicators
        structure_score = (uniformity_score * 0.3 +
                          ai_declarative_score * 0.3 +
                          ai_complex_score * 0.4)

        return structure_score

    def _analyze_punctuation_patterns(self, text: str) -> float:
        """Analyze punctuation usage patterns."""
        # Count punctuation marks
        punctuation_counts = {
            '.': text.count('.'),
            ',': text.count(','),
            ';': text.count(';'),
            ':': text.count(':'),
            '!': text.count('!'),
            '?': text.count('?'),
            '"': text.count('"'),
            "'": text.count("'")
        }

        total_chars = len(text)
        total_punct = sum(punctuation_counts.values())

        if total_chars == 0:
            return 0.5

        # 1. Comma frequency
        comma_ratio = punctuation_counts[','] / total_chars

        # AI often uses more commas
        ai_comma_score = min(comma_ratio * 100, 1.0)

        # 2. Semicolon usage (more formal)
        semicolon_ratio = punctuation_counts[';'] / total_chars

        # AI often uses more semicolons
        ai_semicolon_score = min(semicolon_ratio * 200, 1.0)

        # 3. Exclamation mark scarcity
        exclamation_ratio = punctuation_counts['!'] / total_chars

        # AI rarely uses exclamation marks
        ai_exclamation_score = 1.0 - min(exclamation_ratio * 50, 1.0)

        # 4. Quote usage patterns
        quote_ratio = (punctuation_counts['"'] + punctuation_counts["'"]) / total_chars

        # AI often uses quotes in a specific way
        ai_quote_score = min(quote_ratio * 50, 1.0)

        # Combine punctuation indicators
        punctuation_score = (ai_comma_score * 0.3 +
                           ai_semicolon_score * 0.25 +
                           ai_exclamation_score * 0.25 +
                           ai_quote_score * 0.2)

        return punctuation_score

    def _count_syllables(self, word: str) -> int:
        """Count syllables in a word."""
        word = word.lower()
        if not word:
            return 0

        # Remove common endings
        word = re.sub(r'(?:[^laeiouy]es|ed|[^laeiouy]e)$', '', word)
        word = re.sub(r'^y', '', word)

        # Count vowel groups
        syllables = 0
        prev_vowel = False

        for char in word:
            is_vowel = char in 'aeiouy'
            if is_vowel and not prev_vowel:
                syllables += 1
            prev_vowel = is_vowel

        # Handle silent e
        if word.endswith('e'):
            syllables -= 1

        # Handle special cases
        if word.endswith('le') and len(word) > 2 and word[-3] not in 'aeiouy':
            syllables += 1

        return max(1, syllables)

    def get_stats(self) -> Dict:
        """Get detection statistics."""
        return {
            "total_detections": self.stats["total_detections"],
            "ai_detected": self.stats["ai_detected"],
            "human_detected": self.stats["human_detected"],
            "ai_detection_rate": (self.stats["ai_detected"] / max(self.stats["total_detections"], 1)) * 100,
            "indicators": self.ai_indicators
        }
