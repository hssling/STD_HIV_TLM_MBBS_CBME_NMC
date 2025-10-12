#!/usr/bin/env python3
"""
AI Humanizer Agent - Main Entry Point

This script provides a command-line interface for the AI humanizer agent
that can detect and humanize AI-generated content.
"""

import argparse
import sys
import os
from pathlib import Path
from typing import List, Optional

# Add current directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from humanizer.core import AIHumanizer, HumanizationResult
from humanizer.utils import TextUtils


def main():
    """Main entry point for the AI Humanizer CLI."""
    parser = argparse.ArgumentParser(
        description="AI Humanizer Agent - Humanize AI-generated content",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py humanize "Your AI text here"
  python main.py humanize-file input.txt output.txt
  python main.py batch file1.txt file2.txt --output-dir results/
  python main.py detect "Text to analyze"
  python main.py stats
        """
    )

    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Humanize text command
    humanize_parser = subparsers.add_parser('humanize', help='Humanize AI-generated text')
    humanize_parser.add_argument('text', help='Text to humanize')
    humanize_parser.add_argument('--context', '-c', help='Context for better humanization')

    # Humanize file command
    file_parser = subparsers.add_parser('humanize-file', help='Humanize content from file')
    file_parser.add_argument('input_file', help='Input file path')
    file_parser.add_argument('output_file', help='Output file path')
    file_parser.add_argument('--context', '-c', help='Context for better humanization')

    # Batch processing command
    batch_parser = subparsers.add_parser('batch', help='Batch process multiple files')
    batch_parser.add_argument('input_files', nargs='+', help='Input file paths')
    batch_parser.add_argument('--output-dir', '-o', required=True, help='Output directory')
    batch_parser.add_argument('--context', '-c', help='Context for better humanization')

    # Detect AI command
    detect_parser = subparsers.add_parser('detect', help='Detect AI-generated content')
    detect_parser.add_argument('text', help='Text to analyze')

    # Stats command
    stats_parser = subparsers.add_parser('stats', help='Show humanizer statistics')

    # Configuration
    parser.add_argument('--config', '-f', default='config.yaml',
                       help='Configuration file path (default: config.yaml)')
    parser.add_argument('--verbose', '-v', action='store_true',
                       help='Verbose output')

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 1

    try:
        # Initialize humanizer
        humanizer = AIHumanizer(args.config)
        utils = TextUtils()

        if args.verbose:
            print(f"Initialized AI Humanizer with config: {args.config}")

        # Process commands
        if args.command == 'humanize':
            result = humanizer.humanize_text(args.text, args.context)
            print_result(result, args.verbose)

        elif args.command == 'humanize-file':
            if not os.path.exists(args.input_file):
                print(f"Error: Input file '{args.input_file}' not found")
                return 1

            result = humanizer.humanize_file(args.input_file, args.output_file, args.context)
            print_result(result, args.verbose)

            if result.success:
                file_size = utils.get_file_size_info(args.output_file)
                print(f"Output saved to: {args.output_file} ({file_size.get('size_formatted', 'unknown size')})")

        elif args.command == 'batch':
            results = process_batch(humanizer, args.input_files, args.output_dir, args.context, args.verbose)

            # Print summary
            successful = sum(1 for r in results if r.success)
            total = len(results)
            print(f"\nBatch processing complete: {successful}/{total} successful")

        elif args.command == 'detect':
            score = humanizer.detector.detect_ai_content(args.text)
            print(f"AI Probability Score: {score:.3f}")
            if score > 0.7:
                print("⚠️  High likelihood of AI-generated content")
            elif score > 0.4:
                print("🤔 Mixed signals - could be AI or human")
            else:
                print("✅ Likely human-generated content")

        elif args.command == 'stats':
            stats = humanizer.get_stats()
            print_stats(stats)

        return 0

    except Exception as e:
        print(f"Error: {str(e)}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        return 1


def process_batch(humanizer: AIHumanizer, input_files: List[str],
                output_dir: str, context: Optional[str] = None,
                verbose: bool = False) -> List[HumanizationResult]:
    """Process multiple files in batch."""
    results = []

    # Ensure output directory exists
    utils = TextUtils()
    utils.ensure_directory(output_dir)

    for input_file in input_files:
        if not os.path.exists(input_file):
            print(f"Warning: File '{input_file}' not found, skipping")
            continue

        # Generate output filename
        filename = Path(input_file).name
        safe_filename = utils.safe_filename(filename)
        output_file = os.path.join(output_dir, f"humanized_{safe_filename}")

        if verbose:
            print(f"Processing: {input_file} -> {output_file}")

        # Humanize file
        result = humanizer.humanize_file(input_file, output_file, context)
        results.append(result)

        # Print individual result
        if result.success:
            print(f"✅ {filename}: {len(result.transformations_applied)} transformations applied")
        else:
            print(f"❌ {filename}: {result.error_message}")

    return results


def print_result(result: HumanizationResult, verbose: bool = False):
    """Print humanization result."""
    if not result.success:
        print(f"❌ Humanization failed: {result.error_message}")
        return

    print("✅ Humanization successful!")
    print(f"📊 AI Probability: {result.ai_probability:.3f}")
    print(f"⏱️  Processing time: {result.processing_time:.2f}s")

    if result.transformations_applied:
        print(f"🔧 Transformations applied: {len(result.transformations_applied)}")
        if verbose:
            for transformation in result.transformations_applied[:10]:  # Show first 10
                print(f"   • {transformation}")
            if len(result.transformations_applied) > 10:
                print(f"   ... and {len(result.transformations_applied) - 10} more")
    else:
        print("📝 No transformations needed (likely human-generated content)")

    print("\n📄 Humanized Text:")
    print("-" * 50)
    print(result.humanized_text)
    print("-" * 50)


def print_stats(stats: dict):
    """Print humanizer statistics."""
    print("🤖 AI Humanizer Statistics")
    print("=" * 40)

    # Detector stats
    detector_stats = stats.get('detector_stats', {})
    print("🔍 Detection Stats:"    print(f"   Total detections: {detector_stats.get('total_detections', 0)}")
    print(f"   AI detected: {detector_stats.get('ai_detected', 0)}")
    print(f"   Human detected: {detector_stats.get('human_detected', 0)}")
    print(f"   AI detection rate: {detector_stats.get('ai_detection_rate', 0):.1f}%")

    # Transformer stats
    transformer_stats = stats.get('transformer_stats', {})
    print("\n🔧 Transformation Stats:"    print(f"   Total transformations: {transformer_stats.get('total_transformations', 0)}")
    print(f"   Successful: {transformer_stats.get('successful_transformations', 0)}")
    print(f"   Failed: {transformer_stats.get('failed_transformations', 0)}")
    print(f"   Success rate: {transformer_stats.get('success_rate', 0):.1f}%")

    # Configuration summary
    config = stats.get('config', {})
    humanization_config = config.get('humanization', {})
    print("
⚙️  Configuration:"    print(f"   Intensity: {humanization_config.get('intensity', 0)}")
    techniques = humanization_config.get('techniques', {})
    enabled_techniques = [k for k, v in techniques.items() if v]
    print(f"   Enabled techniques: {', '.join(enabled_techniques)}")


if __name__ == '__main__':
    exit_code = main()
    sys.exit(exit_code)
