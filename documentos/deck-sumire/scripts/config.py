"""
Configuration file for Perfumaria Sumirê Digital Analysis
V4 Carvalho Consultoria Digital
"""

# V4 Carvalho Brand Colors
COLORS = {
    'primary': '#FF6B35',      # Vibrant Orange
    'secondary': '#4ECDC4',    # Turquoise
    'accent': '#F7B731',       # Gold Yellow
    'dark': '#2C3E50',         # Dark Blue
    'light': '#ECF0F1',        # Light Gray
    'success': '#27AE60',      # Green
    'warning': '#E67E22',      # Burnt Orange
    'danger': '#E74C3C'        # Red
}

# RGB Color tuples for python-pptx
COLORS_RGB = {
    'primary': (255, 107, 53),
    'secondary': (78, 205, 196),
    'accent': (247, 183, 49),
    'dark': (44, 62, 80),
    'light': (236, 240, 241),
    'success': (39, 174, 96),
    'warning': (230, 126, 34),
    'danger': (231, 76, 60),
    'white': (255, 255, 255),
    'black': (0, 0, 0)
}

# Font configurations
FONTS = {
    'title': {
        'family': 'Arial',
        'size': 28,
        'weight': 'bold'
    },
    'subtitle': {
        'family': 'Arial',
        'size': 18
    },
    'body': {
        'family': 'Arial',
        'size': 14
    },
    'small': {
        'family': 'Arial',
        'size': 11
    }
}

# Chart styling
CHART_STYLE = {
    'dpi': 300,
    'figure_facecolor': 'white',
    'axes_facecolor': 'white',
    'grid_alpha': 0.3,
    'grid_color': '#CCCCCC',
    'line_width': 2.5,
    'marker_size': 8
}

# Company data
SUMIRE = {
    'name': 'Perfumaria Sumirê',
    'founded': 1984,
    'stores': 70,
    'instagram': '@perfumariasumire',
    'followers': 124000,
    'website': 'https://www.perfumariasumire.com.br/',
    'positioning': 'Maior rede de perfumarias do Brasil'
}

# Competitors list
COMPETITORS = [
    {
        'name': 'Época Cosméticos',
        'website': 'https://www.epocacosmeticos.com.br/',
        'notes': 'Magazine Luiza, transição para físico'
    },
    {
        'name': 'Soneda Perfumaria',
        'website': 'https://www.soneda.com.br/',
        'notes': 'R$ 420 milhões faturamento (2023)'
    },
    {
        'name': 'Padron Perfumaria',
        'website': 'https://www.padron.com.br/',
        'notes': '50+ anos, 13 lojas'
    },
    {
        'name': 'Teruya Perfumaria',
        'website': 'https://www.teruya.com.br/',
        'notes': '15+ lojas em SP'
    },
    {
        'name': 'Lojas REDE',
        'website': 'https://www.lojasrede.com.br/',
        'notes': 'Disputa título "maior rede"'
    }
]

# LLM platforms to test
LLM_PLATFORMS = ['ChatGPT', 'Perplexity', 'Gemini', 'Claude']

# Test questions for LLMs
LLM_QUESTIONS = [
    "Quais as melhores perfumarias em São Paulo?",
    "Onde comprar perfumes importados em São Paulo?",
    "Perfumarias com programa de fidelidade em SP",
    "Melhores lojas de cosméticos em São Paulo",
    "Onde encontrar maquiagem profissional em São Paulo?",
    "Lojas de perfumaria no estado de São Paulo",
    "Perfumarias baratas em São Paulo"
]

# File paths
PATHS = {
    'data_dir': '../data/',
    'charts_dir': '../charts/',
    'output_dir': '../output/',
    'sumire_data': '../data/sumire_data.json',
    'competitors_data': '../data/competitors.json',
    'llm_results': '../data/llm_results.json',
    'keywords_data': '../data/trends_keywords.json'
}

# Slide configuration
SLIDE_CONFIG = {
    'width_inches': 10,
    'height_inches': 7.5,
    'total_slides': 13
}

# Chart file names
CHART_FILES = {
    'radar_sumire': '../charts/radar_sumire.png',
    'radar_competitors': '../charts/radar_competitors.png',
    'traffic_12months': '../charts/traffic_12months.png',
    'competitors_channels': '../charts/competitors_channels.png',
    'sankey_flow': '../charts/sankey_flow.png',
    'keywords_table': '../charts/keywords_table.png',
    'demand_trend': '../charts/demand_trend.png'
}

# Browser automation settings
BROWSER_CONFIG = {
    'headless': False,  # Set to True for production
    'timeout': 30000,   # 30 seconds
    'screenshot_delay': 2000,  # 2 seconds
    'retry_attempts': 3
}

# API endpoints (placeholder - replace with actual if available)
API_ENDPOINTS = {
    'pagespeed': 'https://www.googleapis.com/pagespeedonline/v5/runPagespeed',
    'similarweb': 'https://api.similarweb.com/v1/',  # Requires API key
    'ubersuggest': 'https://app.neilpatel.com/api/'  # Requires API key
}
