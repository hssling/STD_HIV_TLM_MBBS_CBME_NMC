"""
Utility Functions Module

This module contains utility functions for text processing,
formatting, and other common operations used by the humanizer.
"""

import re
import os
from typing import Dict, List
from pathlib import Path


class TextUtils:
    """
    Utility class for text processing operations.
    """

    def __init__(self):
        """Initialize the TextUtils class."""
        # Common stop words that don't add much meaning
        self.stop_words = {
            'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from',
            'has', 'he', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the',
            'to', 'was', 'will', 'with', 'would', 'could', 'should', 'may',
            'might', 'must', 'can', 'shall', 'this', 'these', 'those'
        }

        # File extensions for text files
        self.text_extensions = {'.txt', '.md', '.markdown', '.text', '.rtf'}

    def clean_text(self, text: str) -> str:
        """
        Clean and normalize text.

        Args:
            text: Text to clean

        Returns:
            Cleaned text
        """
        if not text:
            return ""

        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text)

        # Remove extra spaces around punctuation
        text = re.sub(r'\s+([,.!?;:])', r'\1', text)
        text = re.sub(r'([,.!?;:])\s+', r'\1 ', text)

        # Fix common spacing issues
        text = re.sub(r'([.!?])\s*([A-Z])', r'\1 \2', text)

        return text.strip()

    def split_into_chunks(self, text: str, chunk_size: int = 1000) -> List[str]:
        """
        Split text into manageable chunks.

        Args:
            text: Text to split
            chunk_size: Maximum size of each chunk

        Returns:
            List of text chunks
        """
        if not text:
            return []

        words = text.split()
        chunks = []
        current_chunk = []

        for word in words:
            current_chunk.append(word)
            if len(' '.join(current_chunk)) >= chunk_size:
                chunks.append(' '.join(current_chunk))
                current_chunk = []

        if current_chunk:
            chunks.append(' '.join(current_chunk))

        return chunks

    def calculate_text_stats(self, text: str) -> Dict:
        """
        Calculate basic statistics about the text.

        Args:
            text: Text to analyze

        Returns:
            Dictionary with text statistics
        """
        if not text:
            return {}

        words = text.split()
        sentences = re.split(r'[.!?]+', text)
        sentences = [s.strip() for s in sentences if s.strip()]

        return {
            'word_count': len(words),
            'sentence_count': len(sentences),
            'character_count': len(text),
            'avg_word_length': sum(len(word) for word in words) / len(words) if words else 0,
            'avg_sentence_length': len(words) / len(sentences) if sentences else 0,
            'paragraph_count': len([p for p in text.split('\n\n') if p.strip()])
        }

    def extract_keywords(self, text: str, max_keywords: int = 10) -> List[str]:
        """
        Extract important keywords from text.

        Args:
            text: Text to analyze
            max_keywords: Maximum number of keywords to return

        Returns:
            List of keywords
        """
        if not text:
            return []

        # Simple keyword extraction based on word frequency
        words = re.findall(r'\b\w+\b', text.lower())
        word_freq = {}

        for word in words:
            if len(word) > 3 and word not in self.stop_words:
                word_freq[word] = word_freq.get(word, 0) + 1

        # Sort by frequency and return top keywords
        keywords = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
        return [keyword for keyword, _ in keywords[:max_keywords]]

    def is_text_file(self, file_path: str) -> bool:
        """
        Check if a file is a text file based on extension.

        Args:
            file_path: Path to the file

        Returns:
            True if file is a text file
        """
        if not file_path:
            return False

        _, ext = os.path.splitext(file_path.lower())
        return ext in self.text_extensions

    def ensure_directory(self, directory: str) -> bool:
        """
        Ensure a directory exists, create if it doesn't.

        Args:
            directory: Directory path

        Returns:
            True if directory exists or was created successfully
        """
        try:
            Path(directory).mkdir(parents=True, exist_ok=True)
            return True
        except Exception:
            return False

    def safe_filename(self, filename: str) -> str:
        """
        Create a safe filename by removing invalid characters.

        Args:
            filename: Original filename

        Returns:
            Safe filename
        """
        if not filename:
            return "output.txt"

        # Remove or replace invalid characters
        safe_name = re.sub(r'[<>:"/\\|?*]', '_', filename)
        safe_name = re.sub(r'_+', '_', safe_name)  # Replace multiple underscores
        safe_name = safe_name.strip('_')  # Remove leading/trailing underscores

        if not safe_name:
            return "output.txt"

        return safe_name

    def format_bytes(self, size_bytes: int) -> str:
        """
        Format bytes into human-readable format.

        Args:
            size_bytes: Size in bytes

        Returns:
            Formatted size string
        """
        if size_bytes == 0:
            return "0 B"

        size_names = ["B", "KB", "MB", "GB", "TB"]
        size_idx = 0
        while size_bytes >= 1024 and size_idx < len(size_names) - 1:
            size_bytes /= 1024.0
            size_idx += 1

        return f"{size_bytes:.1f} {size_names[size_idx]}"

    def truncate_text(self, text: str, max_length: int, suffix: str = "...") -> str:
        """
        Truncate text to maximum length with suffix.

        Args:
            text: Text to truncate
            max_length: Maximum length including suffix
            suffix: Suffix to add when truncating

        Returns:
            Truncated text
        """
        if not text or len(text) <= max_length:
            return text

        return text[:max_length - len(suffix)] + suffix

    def count_occurrences(self, text: str, substring: str) -> int:
        """
        Count occurrences of substring in text.

        Args:
            text: Text to search in
            substring: Substring to count

        Returns:
            Number of occurrences
        """
        return text.count(substring)

    def find_similar_words(self, word: str, word_list: List[str],
                          threshold: float = 0.8) -> List[str]:
        """
        Find words similar to the given word.

        Args:
            word: Target word
            word_list: List of words to search in
            threshold: Similarity threshold (0-1)

        Returns:
            List of similar words
        """
        if not word or not word_list:
            return []

        similar_words = []
        word_lower = word.lower()

        for candidate in word_list:
            candidate_lower = candidate.lower()

            # Simple similarity check based on character overlap
            if len(candidate_lower) > 0 and len(word_lower) > 0:
                overlap = len(set(word_lower) & set(candidate_lower))
                max_len = max(len(word_lower), len(candidate_lower))
                similarity = overlap / max_len

                if similarity >= threshold:
                    similar_words.append(candidate)

        return similar_words

    def extract_sentences(self, text: str) -> List[str]:
        """
        Extract sentences from text.

        Args:
            text: Text to process

        Returns:
            List of sentences
        """
        if not text:
            return []

        # Split on sentence endings
        sentences = re.split(r'[.!?]+', text)
        return [sentence.strip() for sentence in sentences if sentence.strip()]

    def word_count_distribution(self, text: str) -> Dict[int, int]:
        """
        Get distribution of word counts in sentences.

        Args:
            text: Text to analyze

        Returns:
            Dictionary mapping word count to frequency
        """
        sentences = self.extract_sentences(text)
        distribution = {}

        for sentence in sentences:
            words = len(sentence.split())
            distribution[words] = distribution.get(words, 0) + 1

        return distribution

    def get_file_size_info(self, file_path: str) -> Dict:
        """
        Get file size information.

        Args:
            file_path: Path to file

        Returns:
            Dictionary with file size info
        """
        try:
            if not os.path.exists(file_path):
                return {"error": "File not found"}

            size_bytes = os.path.getsize(file_path)
            return {
                "size_bytes": size_bytes,
                "size_formatted": self.format_bytes(size_bytes),
                "exists": True
            }
        except Exception as e:
            return {"error": str(e)}

    def validate_text_length(self, text: str, min_length: int = 10,
                           max_length: int = 10000) -> Dict:
        """
        Validate text length against constraints.

        Args:
            text: Text to validate
            min_length: Minimum allowed length
            max_length: Maximum allowed length

        Returns:
            Dictionary with validation results
        """
        text_length = len(text) if text else 0

        return {
            "valid": min_length <= text_length <= max_length,
            "length": text_length,
            "min_length": min_length,
            "max_length": max_length,
            "too_short": text_length < min_length,
            "too_long": text_length > max_length
        }
