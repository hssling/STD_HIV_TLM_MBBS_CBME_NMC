#!/usr/bin/env python3
"""
Example Usage of AI Humanizer Agent

This script demonstrates how to use the AI Humanizer Agent
with various types of content and scenarios.
"""

import sys
import os

# Add current directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from humanizer.core import AIHumanizer


def main():
    """Demonstrate AI Humanizer functionality."""
    print("🤖 AI Humanizer Agent - Example Usage")
    print("=" * 50)

    # Initialize humanizer
    humanizer = AIHumanizer("config.yaml")

    # Example 1: Academic text
    print("\n📚 Example 1: Academic Text")
    print("-" * 30)

    academic_text = """
    The implementation of machine learning algorithms in contemporary healthcare
    systems represents a significant advancement in medical technology. This
    approach facilitates enhanced diagnostic accuracy and enables more
    efficient treatment methodologies across various medical disciplines.
    """

    print("Original (AI-like):")
    print(academic_text.strip())

    result = humanizer.humanize_text(academic_text, context="academic")
    print(f"\nAI Probability: {result.ai_probability:.3f}")
    print(f"Transformations: {len(result.transformations_applied)}")

    print("\nHumanized:")
    print(result.humanized_text)

    # Example 2: Business text
    print("\n\n💼 Example 2: Business Text")
    print("-" * 30)

    business_text = """
    Our organization is committed to leveraging innovative solutions to drive
    sustainable growth and maximize stakeholder value. Through strategic
    partnerships and comprehensive market analysis, we continuously optimize
    our operational frameworks to achieve competitive advantages.
    """

    print("Original (AI-like):")
    print(business_text.strip())

    result = humanizer.humanize_text(business_text, context="business")
    print(f"\nAI Probability: {result.ai_probability:.3f}")
    print(f"Transformations: {len(result.transformations_applied)}")

    print("\nHumanized:")
    print(result.humanized_text)

    # Example 3: Casual conversation
    print("\n\n💬 Example 3: Casual Text")
    print("-" * 30)

    casual_text = """
    The utilization of social media platforms has fundamentally transformed
    interpersonal communication dynamics in contemporary society. This
    paradigm shift necessitates comprehensive adaptation strategies.
    """

    print("Original (AI-like):")
    print(casual_text.strip())

    result = humanizer.humanize_text(casual_text, context="conversation")
    print(f"\nAI Probability: {result.ai_probability:.3f}")
    print(f"Transformations: {len(result.transformations_applied)}")

    print("\nHumanized:")
    print(result.humanized_text)

    # Example 4: Human-like text (should remain mostly unchanged)
    print("\n\n✋ Example 4: Human-like Text")
    print("-" * 32)

    human_text = """
    I remember when I was a kid, my grandma used to tell me these amazing
    stories about her childhood. You know, the kind that just stick with you
    forever. She'd talk about playing in the fields and helping with the
    farm work, and I could picture it all so clearly in my mind.
    """

    print("Original (Human-like):")
    print(human_text.strip())

    result = humanizer.humanize_text(human_text)
    print(f"\nAI Probability: {result.ai_probability:.3f}")
    print(f"Transformations: {len(result.transformations_applied)}")

    if len(result.transformations_applied) == 0:
        print("✅ Correctly identified as human-like content!")
    else:
        print("Humanized:")
        print(result.humanized_text)

    # Show statistics
    print("\n\n📊 Final Statistics")
    print("-" * 20)

    stats = humanizer.get_stats()
    detector_stats = stats.get('detector_stats', {})
    transformer_stats = stats.get('transformer_stats', {})

    print(f"Total detections: {detector_stats.get('total_detections', 0)}")
    print(f"AI detected: {detector_stats.get('ai_detected', 0)}")
    print(f"Human detected: {detector_stats.get('human_detected', 0)}")
    print(f"Success rate: {transformer_stats.get('success_rate', 0):.1f}%")

    print("\n🎉 Examples completed! The AI Humanizer Agent is ready to use.")


if __name__ == '__main__':
    main()
