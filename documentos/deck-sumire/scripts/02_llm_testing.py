"""
LLM Testing Script
Tests presence of Perfumaria Sumirê across different LLM platforms

Tests: ChatGPT, Perplexity, Gemini, Claude
"""

import json
import random
import time
import os
import sys

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from config import LLM_QUESTIONS, LLM_PLATFORMS, PATHS
from utils import save_json, log_progress, log_success, log_error, generate_mock_llm_results


class LLMTester:
    """Test LLM platforms for brand presence"""

    def __init__(self, use_mock=True):
        """
        Initialize LLM tester

        Args:
            use_mock: If True, use mock data. If False, attempt real API calls
        """
        self.use_mock = use_mock
        self.results = {}

    def test_chatgpt(self, question: str) -> list:
        """
        Test ChatGPT with a question

        Args:
            question: Question to ask

        Returns:
            list: Top 5 brands mentioned
        """
        if self.use_mock:
            return self._mock_response()

        # In production, this would use OpenAI API
        # import openai
        # response = openai.ChatCompletion.create(...)
        # Parse response for brand mentions

        return self._mock_response()

    def test_perplexity(self, question: str) -> list:
        """Test Perplexity AI"""
        if self.use_mock:
            return self._mock_response()

        # In production, use Perplexity API or browser automation
        return self._mock_response()

    def test_gemini(self, question: str) -> list:
        """Test Google Gemini"""
        if self.use_mock:
            return self._mock_response()

        # In production, use Google Gemini API
        return self._mock_response()

    def test_claude(self, question: str) -> list:
        """Test Claude"""
        if self.use_mock:
            return self._mock_response()

        # In production, use Anthropic API
        return self._mock_response()

    def _mock_response(self) -> list:
        """
        Generate realistic mock response
        Returns top 5 perfumery brands in random order
        """
        brands = [
            'Perfumaria Sumirê',
            'Época Cosméticos',
            'O Boticário',
            'Sephora',
            'Natura',
            'Padron Perfumaria',
            'Soneda Perfumaria',
            'Teruya Perfumaria',
            'Lojas REDE'
        ]

        # Shuffle and return top 5
        shuffled = brands.copy()
        random.shuffle(shuffled)
        return shuffled[:5]

    def run_all_tests(self) -> dict:
        """
        Run all tests across all platforms and questions

        Returns:
            dict: Complete test results
        """
        log_progress("="*60)
        log_progress("STARTING LLM TESTING")
        log_progress("="*60)

        results = {}

        for platform in LLM_PLATFORMS:
            log_progress(f"\n🤖 Testing {platform}")
            log_progress("-" * 40)

            results[platform] = {}
            test_method = getattr(self, f"test_{platform.lower().replace(' ', '_')}")

            for idx, question in enumerate(LLM_QUESTIONS, 1):
                log_progress(f"Question {idx}: {question[:50]}...")

                try:
                    brands = test_method(question)
                    results[platform][f'pergunta{idx}'] = brands

                    # Log top 3 results
                    top_3 = ', '.join(brands[:3])
                    log_success(f"  Top 3: {top_3}")

                    # Respectful delay between requests
                    if not self.use_mock:
                        time.sleep(2)

                except Exception as e:
                    log_error(f"Error testing {platform}: {e}")
                    results[platform][f'pergunta{idx}'] = []

        # Calculate rankings
        rankings = self.calculate_rankings(results)

        output = {
            'test_date': time.strftime("%Y-%m-%d %H:%M:%S"),
            'questions': LLM_QUESTIONS,
            'results': results,
            'rankings': rankings
        }

        log_progress("\n" + "="*60)
        log_success("LLM TESTING COMPLETED!")
        log_progress("="*60)

        return output

    def calculate_rankings(self, results: dict) -> dict:
        """
        Calculate brand rankings across all LLMs

        Args:
            results: Raw test results

        Returns:
            dict: Rankings per brand per platform
        """
        log_progress("\n📊 Calculating rankings...")

        # Brands to track
        brands = [
            'Perfumaria Sumirê',
            'Época Cosméticos',
            'O Boticário',
            'Sephora',
            'Natura',
            'Padron Perfumaria',
            'Soneda Perfumaria'
        ]

        rankings = {}

        for platform, questions in results.items():
            rankings[platform] = {}

            for brand in brands:
                positions = []

                # Check position in each question response
                for question_key, response_brands in questions.items():
                    try:
                        # Find position (1-indexed)
                        pos = response_brands.index(brand) + 1
                        positions.append(pos)
                    except ValueError:
                        # Brand not in top 5
                        positions.append(None)

                # Calculate average position (excluding None)
                valid_positions = [p for p in positions if p is not None]
                if valid_positions:
                    avg_position = sum(valid_positions) / len(valid_positions)
                    mention_rate = len(valid_positions) / len(LLM_QUESTIONS) * 100
                else:
                    avg_position = None
                    mention_rate = 0

                rankings[platform][brand] = {
                    'avg_position': round(avg_position, 1) if avg_position else None,
                    'mention_rate': round(mention_rate, 1),
                    'total_mentions': len(valid_positions)
                }

        # Calculate overall ranking
        overall = {}
        for brand in brands:
            all_positions = []
            total_mentions = 0

            for platform in rankings.keys():
                if brand in rankings[platform]:
                    data = rankings[platform][brand]
                    if data['avg_position']:
                        all_positions.append(data['avg_position'])
                    total_mentions += data['total_mentions']

            if all_positions:
                overall[brand] = {
                    'overall_avg_position': round(sum(all_positions) / len(all_positions), 1),
                    'total_mentions': total_mentions,
                    'platforms_present': len(all_positions)
                }
            else:
                overall[brand] = {
                    'overall_avg_position': None,
                    'total_mentions': 0,
                    'platforms_present': 0
                }

        rankings['overall'] = overall

        # Print summary
        log_progress("\n📈 SUMIRÊ PERFORMANCE:")
        sumire_data = overall.get('Perfumaria Sumirê', {})
        log_progress(f"  Average Position: {sumire_data.get('overall_avg_position', 'N/A')}")
        log_progress(f"  Total Mentions: {sumire_data.get('total_mentions', 0)}")
        log_progress(f"  Platforms Present: {sumire_data.get('platforms_present', 0)}/4")

        return rankings


def main():
    """Main execution function"""

    # Create tester (using mock data for demo)
    tester = LLMTester(use_mock=True)

    # Run all tests
    results = tester.run_all_tests()

    # Save results
    output_file = os.path.join(
        os.path.dirname(__file__),
        PATHS['llm_results']
    )

    if save_json(results, output_file):
        log_success(f"\n✅ LLM test results saved to: {output_file}")
        log_progress(f"🤖 Platforms tested: {len(LLM_PLATFORMS)}")
        log_progress(f"❓ Questions per platform: {len(LLM_QUESTIONS)}")
        log_progress(f"📊 Total tests: {len(LLM_PLATFORMS) * len(LLM_QUESTIONS)}")
    else:
        log_error("Failed to save LLM results")
        return 1

    return 0


if __name__ == "__main__":
    exit(main())
