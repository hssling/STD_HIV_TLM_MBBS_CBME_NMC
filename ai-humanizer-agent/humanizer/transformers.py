"""
Text Transformation Module

This module contains various techniques to humanize AI-generated content
by applying natural language transformations.
"""

import random
import re
import logging
from typing import Dict, List, Tuple
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt', quiet=True)

try:
    nltk.data.find('wordnet')
except LookupError:
    nltk.download('wordnet', quiet=True)


class TextTransformer:
    """
    Text transformation engine that applies various humanization techniques
    to make AI-generated content sound more natural and human-like.
    """

    def __init__(self, config: Dict):
        """
        Initialize the Text Transformer.

        Args:
            config: Configuration dictionary
        """
        self.config = config
        self.stats = {
            "total_transformations": 0,
            "successful_transformations": 0,
            "failed_transformations": 0
        }

        # Human-like vocabulary variations
        self.vocabulary_maps = {
            "very": ["really", "quite", "super", "extremely", "incredibly"],
            "good": ["great", "excellent", "fantastic", "wonderful", "awesome"],
            "bad": ["terrible", "awful", "horrible", "dreadful", "lousy"],
            "big": ["huge", "massive", "enormous", "gigantic", "tremendous"],
            "small": ["tiny", "little", "miniature", "compact", "mini"],
            "important": ["crucial", "vital", "essential", "critical", "key"],
            "said": ["mentioned", "stated", "remarked", "commented", "noted"],
            "think": ["believe", "feel", "consider", "reckon", "suppose"],
            "make": ["create", "build", "produce", "generate", "craft"],
            "use": ["utilize", "employ", "apply", "leverage", "harness"]
        }

        # Common filler words and phrases for natural flow
        self.fillers = [
            "you know", "like", "so", "well", "actually", "basically",
            "I mean", "sort of", "kind of", "pretty much", "stuff like that"
        ]

        # Contraction mappings for casual tone
        self.contractions = {
            "I am": "I'm", "you are": "you're", "he is": "he's",
            "she is": "she's", "it is": "it's", "we are": "we're",
            "they are": "they're", "do not": "don't", "does not": "doesn't",
            "did not": "didn't", "cannot": "can't", "will not": "won't",
            "would not": "wouldn't", "should not": "shouldn't",
            "could not": "couldn't", "is not": "isn't", "are not": "aren't",
            "was not": "wasn't", "were not": "weren't", "has not": "hasn't",
            "have not": "haven't", "had not": "hadn't"
        }

        # Idiom and expression database
        self.idioms = [
            "break the ice", "piece of cake", "kick the bucket", "bite the bullet",
            "hit the nail on the head", "throw in the towel", "bend over backwards",
            "jump to conclusions", "miss the boat", "pull someone's leg",
            "raining cats and dogs", "speak of the devil", "time flies",
            "actions speak louder than words", "better late than never"
        ]

        self.logger = logging.getLogger(__name__)

    def humanize_text(self, text: str, context: str = None) -> Tuple[str, List[str]]:
        """
        Apply humanization transformations to text.

        Args:
            text: Text to humanize
            context: Optional context for better transformations

        Returns:
            Tuple of (humanized_text, list_of_transformations_applied)
        """
        if not text or len(text.strip()) < 20:
            return text, []

        self.stats["total_transformations"] += 1
        transformations_applied = []

        try:
            humanized_text = text

            # Apply transformations based on configuration
            techniques = self.config["humanization"]["techniques"]

            if techniques.get("vocabulary_variation", True):
                humanized_text, vocab_transforms = self._apply_vocabulary_variation(humanized_text)
                transformations_applied.extend(vocab_transforms)

            if techniques.get("sentence_structure", True):
                humanized_text, struct_transforms = self._vary_sentence_structure(humanized_text)
                transformations_applied.extend(struct_transforms)

            if techniques.get("punctuation_variation", True):
                humanized_text, punct_transforms = self._add_punctuation_variation(humanized_text)
                transformations_applied.extend(punct_transforms)

            if techniques.get("idiomatic_expressions", True):
                humanized_text, idiom_transforms = self._add_idiomatic_expressions(humanized_text)
                transformations_applied.extend(idiom_transforms)

            if techniques.get("personal_touch", True):
                humanized_text, personal_transforms = self._add_personal_touch(humanized_text)
                transformations_applied.extend(personal_transforms)

            if techniques.get("contextual_awareness", True) and context:
                humanized_text, context_transforms = self._apply_contextual_awareness(humanized_text, context)
                transformations_applied.extend(context_transforms)

            # Apply contractions for casual tone
            humanized_text, contract_transforms = self._apply_contractions(humanized_text)
            transformations_applied.extend(contract_transforms)

            # Add some natural filler words occasionally
            humanized_text, filler_transforms = self._add_filler_words(humanized_text)
            transformations_applied.extend(filler_transforms)

            self.stats["successful_transformations"] += 1
            return humanized_text, transformations_applied

        except Exception as e:
            self.logger.error(f"Error in text transformation: {str(e)}")
            self.stats["failed_transformations"] += 1
            return text, []

    def _apply_vocabulary_variation(self, text: str) -> Tuple[str, List[str]]:
        """Apply vocabulary variations to make text more natural."""
        transformations = []
        words = word_tokenize(text)

        for i, word in enumerate(words):
            if word.lower() in self.vocabulary_maps:
                # 30% chance to replace with variation
                if random.random() < 0.3:
                    variations = self.vocabulary_maps[word.lower()]
                    new_word = random.choice(variations)
                    words[i] = new_word
                    transformations.append(f"vocabulary_variation: '{word}' -> '{new_word}'")

        return ' '.join(words), transformations

    def _vary_sentence_structure(self, text: str) -> Tuple[str, List[str]]:
        """Vary sentence structure for more natural flow."""
        transformations = []
        sentences = sent_tokenize(text)

        for i, sentence in enumerate(sentences):
            # 25% chance to modify sentence structure
            if random.random() < 0.25 and len(sentence) > 20:
                modified_sentence, transform_type = self._modify_sentence_structure(sentence)
                if modified_sentence != sentence:
                    sentences[i] = modified_sentence
                    transformations.append(f"sentence_structure: {transform_type}")

        return ' '.join(sentences), transformations

    def _modify_sentence_structure(self, sentence: str) -> Tuple[str, str]:
        """Modify a single sentence's structure."""
        # Add introductory phrases occasionally
        intro_phrases = [
            "Interestingly,", "Surprisingly,", "Actually,", "Basically,",
            "You know,", "Well,", "So,", "And,"
        ]

        # Break up long sentences
        if len(sentence) > 100 and ',' not in sentence:
            words = sentence.split()
            if len(words) > 15:
                # Split at a random point
                split_point = random.randint(10, len(words) - 5)
                first_part = ' '.join(words[:split_point])
                second_part = ' '.join(words[split_point:])

                # Add transition word
                transitions = ["and", "but", "so", "because", "although", "while"]
                transition = random.choice(transitions)

                return f"{first_part}. {transition.capitalize()} {second_part}", "sentence_splitting"

        # Add introductory phrase
        if not sentence.startswith(tuple(phrase[:-1] for phrase in intro_phrases)):
            phrase = random.choice(intro_phrases)
            return f"{phrase} {sentence}", "introductory_phrase"

        return sentence, "no_change"

    def _add_punctuation_variation(self, text: str) -> Tuple[str, List[str]]:
        """Add punctuation variations for more natural rhythm."""
        transformations = []

        # Occasionally add em-dashes for interruption
        if random.random() < 0.2 and "--" not in text:
            sentences = sent_tokenize(text)
            if len(sentences) > 1:
                # Replace a comma with an em-dash in one sentence
                sentence = random.choice(sentences)
                if "," in sentence:
                    modified = sentence.replace(",", " —", 1)
                    text = text.replace(sentence, modified)
                    transformations.append("punctuation_variation: em-dash")

        # Add occasional exclamation for emphasis
        if random.random() < 0.15 and "!" not in text:
            sentences = sent_tokenize(text)
            # Find a sentence that could use emphasis
            for i, sent in enumerate(sentences):
                if len(sent) > 30 and not sent.endswith("!"):
                    # 50% chance to add exclamation
                    if random.random() < 0.5:
                        new_sent = sent[:-1] + "!"
                        sentences[i] = new_sent
                        transformations.append("punctuation_variation: exclamation")
                        break

            text = ' '.join(sentences)

        return text, transformations

    def _add_idiomatic_expressions(self, text: str) -> Tuple[str, List[str]]:
        """Add idiomatic expressions for more natural language."""
        transformations = []

        # Only add idioms occasionally (15% chance)
        if random.random() < 0.15 and len(text) > 100:
            idiom = random.choice(self.idioms)

            # Find a good place to insert the idiom
            sentences = sent_tokenize(text)
            if len(sentences) > 2:
                # Insert in a random sentence
                insert_idx = random.randint(0, len(sentences) - 1)
                sentence = sentences[insert_idx]

                # Add idiom at the end or beginning of sentence
                if random.random() < 0.5:
                    # At the end
                    new_sentence = sentence[:-1] + f", {idiom}."
                    sentences[insert_idx] = new_sentence
                else:
                    # At the beginning
                    new_sentence = f"{idiom.capitalize()}, {sentence}"
                    sentences[insert_idx] = new_sentence

                transformations.append(f"idiomatic_expression: '{idiom}'")
                text = ' '.join(sentences)

        return text, transformations

    def _add_personal_touch(self, text: str) -> Tuple[str, List[str]]:
        """Add personal elements to make text more human-like."""
        transformations = []

        # 20% chance to add personal touch
        if random.random() < 0.2:
            sentences = sent_tokenize(text)
            if sentences:
                # Modify first sentence to be more personal
                first_sentence = sentences[0]

                # Add personal opener
                openers = [
                    "I think", "In my opinion,", "From what I've seen,",
                    "You know,", "Well,", "So,"
                ]

                if not any(first_sentence.startswith(opener[:-1]) for opener in openers):
                    opener = random.choice(openers)
                    new_first = f"{opener} {first_sentence}"
                    sentences[0] = new_first
                    transformations.append("personal_touch: opener")
                    text = ' '.join(sentences)

        return text, transformations

    def _apply_contextual_awareness(self, text: str, context: str) -> Tuple[str, List[str]]:
        """Apply context-aware transformations."""
        transformations = []

        # Simple context awareness - adjust formality based on context
        context_lower = context.lower()

        # If context suggests casual conversation, make more casual
        if any(word in context_lower for word in ["chat", "conversation", "talk", "discuss"]):
            # Add more casual elements
            text, casual_transforms = self._make_more_casual(text)
            transformations.extend(casual_transforms)

        # If context suggests formal, make more formal
        elif any(word in context_lower for word in ["academic", "professional", "formal", "business"]):
            # Add more formal elements
            text, formal_transforms = self._make_more_formal(text)
            transformations.extend(formal_transforms)

        return text, transformations

    def _make_more_casual(self, text: str) -> Tuple[str, List[str]]:
        """Make text more casual and conversational."""
        transformations = []

        # Add more contractions
        for formal, casual in self.contractions.items():
            if formal in text:
                text = text.replace(formal, casual)
                transformations.append(f"contraction: '{formal}' -> '{casual}'")

        # Add filler words occasionally
        if random.random() < 0.3:
            filler = random.choice(self.fillers)
            sentences = sent_tokenize(text)
            if sentences:
                insert_idx = random.randint(0, len(sentences) - 1)
                sentences[insert_idx] = f"{filler}, {sentences[insert_idx]}"
                text = ' '.join(sentences)
                transformations.append(f"filler_word: '{filler}'")

        return text, transformations

    def _make_more_formal(self, text: str) -> Tuple[str, List[str]]:
        """Make text more formal and professional."""
        transformations = []

        # Expand contractions
        for formal, casual in self.contractions.items():
            if casual in text:
                text = text.replace(casual, formal)
                transformations.append(f"formal_expansion: '{casual}' -> '{formal}'")

        # Use more sophisticated vocabulary
        for simple, sophisticated in self.vocabulary_maps.items():
            if simple in text.lower():
                if random.random() < 0.4:  # 40% chance to use sophisticated version
                    text = re.sub(r'\b' + simple + r'\b', sophisticated[0], text, flags=re.IGNORECASE)
                    transformations.append(f"formal_vocabulary: '{simple}' -> '{sophisticated[0]}'")

        return text, transformations

    def _apply_contractions(self, text: str) -> Tuple[str, List[str]]:
        """Apply contractions for more natural speech patterns."""
        transformations = []

        # Apply contractions based on intensity setting
        intensity = self.config["humanization"]["intensity"]

        for formal, casual in self.contractions.items():
            if formal in text and random.random() < intensity * 0.5:
                text = text.replace(formal, casual)
                transformations.append(f"contraction: '{formal}' -> '{casual}'")

        return text, transformations

    def _add_filler_words(self, text: str) -> Tuple[str, List[str]]:
        """Add filler words for more natural speech patterns."""
        transformations = []

        # Only add fillers occasionally based on intensity
        if random.random() < self.config["humanization"]["intensity"] * 0.3:
            filler = random.choice(self.fillers)
            sentences = sent_tokenize(text)

            if len(sentences) > 1:
                # Insert filler at random position
                insert_idx = random.randint(0, len(sentences) - 1)
                sentences[insert_idx] = f"{filler}, {sentences[insert_idx]}"
                text = ' '.join(sentences)
                transformations.append(f"filler_word: '{filler}'")

        return text, transformations

    def get_stats(self) -> Dict:
        """Get transformation statistics."""
        success_rate = (self.stats["successful_transformations"] /
                       max(self.stats["total_transformations"], 1)) * 100

        return {
            "total_transformations": self.stats["total_transformations"],
            "successful_transformations": self.stats["successful_transformations"],
            "failed_transformations": self.stats["failed_transformations"],
            "success_rate": success_rate
        }
