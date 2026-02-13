"""
Utility functions for Perfumaria Sumirê Digital Analysis
V4 Carvalho Consultoria Digital
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Any
import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def save_json(data: Dict[str, Any], filepath: str) -> bool:
    """
    Save data to JSON file

    Args:
        data: Dictionary to save
        filepath: Path to save the file

    Returns:
        bool: True if successful, False otherwise
    """
    try:
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        logger.info(f"✅ Saved data to {filepath}")
        return True
    except Exception as e:
        logger.error(f"❌ Error saving {filepath}: {e}")
        return False


def load_json(filepath: str) -> Dict[str, Any]:
    """
    Load data from JSON file

    Args:
        filepath: Path to the JSON file

    Returns:
        dict: Loaded data or empty dict if error
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        logger.info(f"✅ Loaded data from {filepath}")
        return data
    except FileNotFoundError:
        logger.warning(f"⚠️  File not found: {filepath}")
        return {}
    except Exception as e:
        logger.error(f"❌ Error loading {filepath}: {e}")
        return {}


def hex_to_rgb(hex_color: str) -> tuple:
    """
    Convert hex color to RGB tuple

    Args:
        hex_color: Hex color string (e.g., '#FF6B35')

    Returns:
        tuple: RGB values (r, g, b)
    """
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def format_number(num: int) -> str:
    """
    Format large numbers with K/M suffix

    Args:
        num: Number to format

    Returns:
        str: Formatted string (e.g., '1.2M', '450K')
    """
    if num >= 1_000_000:
        return f"{num / 1_000_000:.1f}M"
    elif num >= 1_000:
        return f"{num / 1_000:.0f}K"
    else:
        return str(num)


def calculate_engagement_rate(likes: int, comments: int, followers: int) -> float:
    """
    Calculate Instagram engagement rate

    Args:
        likes: Number of likes
        comments: Number of comments
        followers: Number of followers

    Returns:
        float: Engagement rate as percentage
    """
    if followers == 0:
        return 0.0
    return ((likes + comments) / followers) * 100


def generate_months_list(start_month: str = 'Jan', year: int = 2025) -> List[str]:
    """
    Generate list of month labels

    Args:
        start_month: Starting month abbreviation
        year: Year

    Returns:
        list: List of month labels
    """
    months = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun',
              'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
    return months


def create_mock_traffic_data(base_value: int = 100000, growth_rate: float = 0.05) -> List[int]:
    """
    Generate realistic mock traffic data with growth trend

    Args:
        base_value: Starting traffic value
        growth_rate: Monthly growth rate (0.05 = 5%)

    Returns:
        list: 12 months of traffic data
    """
    import random
    data = []
    current = base_value

    for i in range(12):
        # Add growth trend
        current *= (1 + growth_rate)
        # Add random variation (-10% to +15%)
        variation = random.uniform(-0.10, 0.15)
        value = int(current * (1 + variation))
        data.append(value)

    return data


def create_mock_channel_breakdown(total_traffic: int) -> Dict[str, int]:
    """
    Create realistic channel traffic breakdown

    Args:
        total_traffic: Total traffic value

    Returns:
        dict: Traffic breakdown by channel
    """
    # Typical distribution for e-commerce
    distribution = {
        'direct': 0.40,
        'organic': 0.28,
        'social': 0.15,
        'referral': 0.10,
        'paid': 0.05,
        'email': 0.02
    }

    breakdown = {}
    remaining = total_traffic

    for channel, percentage in distribution.items():
        if channel == 'email':  # Last channel gets remainder
            breakdown[channel] = remaining
        else:
            value = int(total_traffic * percentage)
            breakdown[channel] = value
            remaining -= value

    return breakdown


def validate_file_exists(filepath: str) -> bool:
    """
    Check if file exists

    Args:
        filepath: Path to check

    Returns:
        bool: True if exists, False otherwise
    """
    exists = os.path.exists(filepath)
    if not exists:
        logger.warning(f"⚠️  File not found: {filepath}")
    return exists


def get_timestamp() -> str:
    """
    Get current timestamp as string

    Returns:
        str: Formatted timestamp
    """
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def create_directory_if_not_exists(dirpath: str) -> None:
    """
    Create directory if it doesn't exist

    Args:
        dirpath: Directory path to create
    """
    os.makedirs(dirpath, exist_ok=True)
    logger.info(f"✅ Directory ensured: {dirpath}")


def log_progress(message: str, emoji: str = "🔄") -> None:
    """
    Log progress message with emoji

    Args:
        message: Progress message
        emoji: Emoji to display
    """
    print(f"\n{emoji} {message}")
    logger.info(message)


def log_success(message: str) -> None:
    """Log success message"""
    log_progress(message, "✅")


def log_error(message: str) -> None:
    """Log error message"""
    log_progress(message, "❌")


def log_warning(message: str) -> None:
    """Log warning message"""
    log_progress(message, "⚠️ ")


# Mock data generators for when real data isn't available

def generate_mock_keywords_data(count: int = 15) -> List[Dict[str, Any]]:
    """Generate realistic mock keywords data"""
    import random

    base_keywords = [
        "perfumaria importados sp",
        "comprar perfume importado são paulo",
        "loja cosméticos são paulo",
        "maquiagem profissional sp",
        "perfumaria centro sp",
        "perfumes baratos são paulo",
        "loja perfumes zona sul sp",
        "cosméticos importados sp",
        "perfumaria 24 horas sp",
        "maquiagem sp",
        "loja beleza são paulo",
        "perfumes femininos sp",
        "perfumes masculinos sp",
        "perfumaria shopping sp",
        "cosméticos sp"
    ]

    keywords = []
    for i, kw in enumerate(base_keywords[:count]):
        keywords.append({
            'term': kw,
            'volume': random.randint(500, 15000),
            'cpc': round(random.uniform(0.80, 4.50), 2),
            'position': random.randint(1, 15),
            'difficulty': random.randint(30, 75),
            'trend': random.choice(['up', 'stable', 'down'])
        })

    return keywords


def generate_mock_llm_results() -> Dict[str, Dict[str, List[str]]]:
    """Generate realistic mock LLM test results"""

    brands = ['Época Cosméticos', 'O Boticário', 'Perfumaria Sumirê',
              'Sephora', 'Natura', 'Padron', 'Soneda', 'Teruya']

    results = {}
    for platform in ['ChatGPT', 'Perplexity', 'Gemini', 'Claude']:
        results[platform] = {}
        for i in range(7):
            # Shuffle brands and pick top 5 for each question
            import random
            shuffled = brands.copy()
            random.shuffle(shuffled)
            results[platform][f'pergunta{i+1}'] = shuffled[:5]

    return results


if __name__ == "__main__":
    # Test functions
    print("Testing utility functions...")

    # Test hex to RGB
    rgb = hex_to_rgb('#FF6B35')
    print(f"Hex to RGB: {rgb}")

    # Test number formatting
    formatted = format_number(124000)
    print(f"Format number: {formatted}")

    # Test mock traffic
    traffic = create_mock_traffic_data()
    print(f"Mock traffic (12 months): {traffic[:3]}...")

    print("\n✅ All utility functions working!")
