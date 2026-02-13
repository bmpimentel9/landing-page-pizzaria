"""
Validation Script
Validates that all required files and data are present and correct

Checks:
- Data files exist and are valid JSON
- All charts have been generated
- PPTX file exists and has correct number of slides
"""

import os
import sys
import json

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from config import PATHS, CHART_FILES, SLIDE_CONFIG
from utils import log_progress, log_success, log_error, log_warning

try:
    from pptx import Presentation
    PPTX_AVAILABLE = True
except ImportError:
    PPTX_AVAILABLE = False
    log_warning("python-pptx not installed. Cannot validate PPTX file.")


def validate_json_file(filepath: str, file_description: str) -> bool:
    """
    Validate that a JSON file exists and is valid

    Args:
        filepath: Path to JSON file
        file_description: Description for logging

    Returns:
        bool: True if valid, False otherwise
    """
    full_path = os.path.join(os.path.dirname(__file__), filepath)

    if not os.path.exists(full_path):
        log_error(f"MISSING: {file_description} - {full_path}")
        return False

    try:
        with open(full_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        if not data:
            log_warning(f"EMPTY: {file_description}")
            return False

        log_success(f"✓ {file_description}")
        return True

    except json.JSONDecodeError as e:
        log_error(f"INVALID JSON: {file_description} - {e}")
        return False
    except Exception as e:
        log_error(f"ERROR: {file_description} - {e}")
        return False


def validate_chart_file(filepath: str, chart_name: str) -> bool:
    """
    Validate that a chart image exists

    Args:
        filepath: Path to chart file
        chart_name: Chart name for logging

    Returns:
        bool: True if exists, False otherwise
    """
    full_path = os.path.join(os.path.dirname(__file__), filepath)

    if not os.path.exists(full_path):
        log_error(f"MISSING CHART: {chart_name}")
        return False

    # Check file size (should be > 10KB for a real chart)
    file_size = os.path.getsize(full_path)
    if file_size < 10000:
        log_warning(f"CHART TOO SMALL: {chart_name} ({file_size} bytes)")
        return False

    log_success(f"✓ Chart: {chart_name}")
    return True


def validate_pptx_file() -> bool:
    """
    Validate the final PPTX file

    Returns:
        bool: True if valid, False otherwise
    """
    if not PPTX_AVAILABLE:
        log_warning("Cannot validate PPTX (python-pptx not installed)")
        return False

    pptx_path = os.path.join(
        os.path.dirname(__file__),
        '../output/sumire-analise-digital.pptx'
    )

    if not os.path.exists(pptx_path):
        log_error("MISSING: Final PPTX file")
        return False

    try:
        # Try to open the presentation
        prs = Presentation(pptx_path)

        # Check number of slides
        num_slides = len(prs.slides)
        expected_slides = SLIDE_CONFIG['total_slides']

        if num_slides != expected_slides:
            log_warning(f"PPTX has {num_slides} slides, expected {expected_slides}")
        else:
            log_success(f"✓ PPTX has correct number of slides ({num_slides})")

        # Check file size
        file_size = os.path.getsize(pptx_path)
        file_size_mb = file_size / (1024 * 1024)

        if file_size_mb > 50:
            log_warning(f"PPTX is very large: {file_size_mb:.1f}MB")
        elif file_size_mb < 1:
            log_warning(f"PPTX seems too small: {file_size_mb:.1f}MB")
        else:
            log_success(f"✓ PPTX file size OK: {file_size_mb:.1f}MB")

        log_success(f"✓ PPTX file is valid: {pptx_path}")
        return True

    except Exception as e:
        log_error(f"ERROR opening PPTX: {e}")
        return False


def run_validation() -> bool:
    """
    Run complete validation

    Returns:
        bool: True if all validations pass, False otherwise
    """
    log_progress("="*60)
    log_progress("VALIDATION REPORT")
    log_progress("="*60)

    errors = 0
    warnings = 0

    # Validate data files
    log_progress("\n📊 Validating Data Files...")
    log_progress("-" * 40)

    if not validate_json_file(PATHS['sumire_data'], "Sumirê Data"):
        errors += 1

    if not validate_json_file(PATHS['llm_results'], "LLM Results"):
        errors += 1

    # Validate charts
    log_progress("\n📈 Validating Charts...")
    log_progress("-" * 40)

    chart_checks = [
        ('radar_sumire', 'Radar Sumirê'),
        ('radar_competitors', 'Radar Competitors'),
        ('traffic_12months', 'Traffic 12 Months'),
        ('competitors_channels', 'Competitors Channels'),
        ('sankey_flow', 'Sankey Flow'),
        ('keywords_table', 'Keywords Table'),
        ('demand_trend', 'Demand Trend')
    ]

    for chart_key, chart_name in chart_checks:
        filepath = CHART_FILES.get(chart_key, f'../charts/{chart_key}.png')
        if not validate_chart_file(filepath, chart_name):
            errors += 1

    # Validate PPTX
    log_progress("\n📄 Validating PPTX File...")
    log_progress("-" * 40)

    if not validate_pptx_file():
        errors += 1

    # Summary
    log_progress("\n" + "="*60)

    if errors == 0 and warnings == 0:
        log_success("✅ ALL VALIDATIONS PASSED!")
        log_success("Project is complete and ready for delivery.")
        log_progress("="*60)
        return True
    else:
        if errors > 0:
            log_error(f"\n❌ FOUND {errors} ERROR(S)")
        if warnings > 0:
            log_warning(f"\n⚠️  FOUND {warnings} WARNING(S)")

        log_progress("\n" + "="*60)
        return False


def main():
    """Main execution function"""

    success = run_validation()

    if success:
        log_progress("\n📦 DELIVERABLES:")
        log_progress("  • Presentation: output/sumire-analise-digital.pptx")
        log_progress("  • Data files: data/")
        log_progress("  • Charts: charts/")
        log_progress("\n🎯 Ready for client delivery!")
        return 0
    else:
        log_progress("\n⚠️  Please fix errors before delivery.")
        return 1


if __name__ == "__main__":
    exit(main())
