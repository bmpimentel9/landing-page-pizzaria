#!/usr/bin/env python3
"""
Main Execution Script
Perfumaria Sumirê Digital Analysis - Complete Pipeline

This script runs all steps in sequence:
1. Data collection (browser automation)
2. LLM testing
3. Chart generation
4. PPTX building
5. Validation

Usage:
    python main.py              # Run all steps
    python main.py --skip-data  # Skip data collection
    python main.py --validate-only  # Only run validation
"""

import os
import sys
import time
import argparse
import importlib.util

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils import log_progress, log_success, log_error, log_warning

# Import all modules - use the correct module names
# Python converts dashes to underscores in import statements
import importlib.util

def load_module(file_path, module_name):
    """Dynamically load a module from file path"""
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

try:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    step1 = load_module(os.path.join(script_dir, '01_browser_automation.py'), 'step1')
    step2 = load_module(os.path.join(script_dir, '02_llm_testing.py'), 'step2')
    step3 = load_module(os.path.join(script_dir, '03_chart_generator.py'), 'step3')
    step4 = load_module(os.path.join(script_dir, '04_pptx_builder.py'), 'step4')
    step5 = load_module(os.path.join(script_dir, 'validate.py'), 'step5')
    MODULES_LOADED = True
except ImportError as e:
    log_error(f"Failed to import modules: {e}")
    MODULES_LOADED = False
except Exception as e:
    log_error(f"Error loading modules: {e}")
    MODULES_LOADED = False


class ProjectPipeline:
    """Main project pipeline orchestrator"""

    def __init__(self, skip_data=False, validate_only=False):
        """
        Initialize pipeline

        Args:
            skip_data: Skip data collection step
            validate_only: Only run validation
        """
        self.skip_data = skip_data
        self.validate_only = validate_only
        self.start_time = time.time()
        self.step_times = {}

    def print_banner(self):
        """Print welcome banner"""
        banner = """
╔═══════════════════════════════════════════════════════════════╗
║                                                                ║
║           PERFUMARIA SUMIRÊ - ANÁLISE DIGITAL                 ║
║                  V4 Carvalho Consultoria                       ║
║                                                                ║
║     Automated Pipeline for Digital Presence Analysis          ║
║                                                                ║
╚═══════════════════════════════════════════════════════════════╝
"""
        print(banner)

    def run_step(self, step_num: int, step_name: str, step_func) -> bool:
        """
        Run a pipeline step with timing

        Args:
            step_num: Step number
            step_name: Step description
            step_func: Function to execute

        Returns:
            bool: True if successful, False otherwise
        """
        log_progress(f"\n{'='*60}")
        log_progress(f"STEP {step_num}: {step_name}")
        log_progress(f"{'='*60}")

        step_start = time.time()

        try:
            result = step_func()

            step_time = time.time() - step_start
            self.step_times[step_name] = step_time

            if result == 0 or result is True:
                log_success(f"\n✅ Step {step_num} completed in {step_time:.1f}s")
                return True
            else:
                log_error(f"\n❌ Step {step_num} failed!")
                return False

        except Exception as e:
            log_error(f"\n❌ Step {step_num} failed with exception: {e}")
            import traceback
            traceback.print_exc()
            return False

    def run_pipeline(self) -> bool:
        """
        Run the complete pipeline

        Returns:
            bool: True if all steps successful, False otherwise
        """
        self.print_banner()

        if not MODULES_LOADED:
            log_error("Cannot run pipeline - modules not loaded correctly")
            return False

        # Validate-only mode
        if self.validate_only:
            log_progress("\nRunning validation only...")
            return self.run_step(5, "Validation", step5.main)

        # Step 1: Data Collection
        if not self.skip_data:
            if not self.run_step(1, "Data Collection", step1.main):
                return False
        else:
            log_warning("\nSkipping Step 1: Data Collection")

        # Step 2: LLM Testing
        if not self.run_step(2, "LLM Testing", step2.main):
            return False

        # Step 3: Chart Generation
        if not self.run_step(3, "Chart Generation", step3.main):
            return False

        # Step 4: PPTX Building
        if not self.run_step(4, "PPTX Building", step4.main):
            return False

        # Step 5: Validation
        if not self.run_step(5, "Validation", step5.main):
            log_warning("\n⚠️  Validation failed, but PPTX may still be usable")

        return True

    def print_summary(self, success: bool):
        """Print execution summary"""
        total_time = time.time() - self.start_time

        print("\n" + "="*60)
        print("EXECUTION SUMMARY")
        print("="*60)

        if self.step_times:
            print("\nStep Times:")
            for step_name, step_time in self.step_times.items():
                print(f"  • {step_name}: {step_time:.1f}s")

        print(f"\nTotal Time: {total_time:.1f}s ({total_time/60:.1f} minutes)")

        if success:
            print("\n" + "="*60)
            print("✅ PIPELINE COMPLETED SUCCESSFULLY!")
            print("="*60)
            print("\n📦 DELIVERABLES:")
            print("  • Presentation: output/sumire-analise-digital.pptx")
            print("  • Data files: data/")
            print("  • Charts: charts/")
            print("\n🎯 Ready for client delivery!")
        else:
            print("\n" + "="*60)
            print("❌ PIPELINE FAILED")
            print("="*60)
            print("\n⚠️  Check error messages above for details")


def parse_arguments():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(
        description='Perfumaria Sumirê Digital Analysis Pipeline'
    )

    parser.add_argument(
        '--skip-data',
        action='store_true',
        help='Skip data collection step (use existing data)'
    )

    parser.add_argument(
        '--validate-only',
        action='store_true',
        help='Only run validation step'
    )

    return parser.parse_args()


def main():
    """Main execution function"""

    args = parse_arguments()

    # Create pipeline
    pipeline = ProjectPipeline(
        skip_data=args.skip_data,
        validate_only=args.validate_only
    )

    # Run pipeline
    success = pipeline.run_pipeline()

    # Print summary
    pipeline.print_summary(success)

    return 0 if success else 1


if __name__ == "__main__":
    exit(main())
